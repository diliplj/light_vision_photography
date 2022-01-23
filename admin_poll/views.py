from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login#, logout
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetView, PasswordChangeView, \
    PasswordResetDoneView

from admin_poll.decorators import *
from admin_poll.models import *
from admin_poll.forms import *
from photography_jan_6 import settings
import sys
import logging
from . import api

"""
NOTE : { Cannot assign "<QuerySet [<Package: Marriage>]>": "Events.package" must be a "Package" instance.   }
 if you are getting these kind of error then use (data = model.objects.get) not (data=model.objects.filter)  

NOTE : In forms you can use form.save() for forms.ModelForm  but for forms.Form you 
cannot use that form.save() so You need to create variable for model 
eg : var = student.objects.get(email=email) and then you should save the variable like 
var.save()
NOTE : make_password('123') # make_password used to encrypt the password 
because User model will allow encrpyt password only
"""
"""
Note : return redirect(request.META['HTTP_REFERER']) to redirect to previous url
"""
logger = logging.getLogger('app')
to_email_id= ""

def add_user(request):
	context = {}
	try:
		template = 'admin_poll/add_admin.html'
		form = UserForm()
		if request.method == "POST":
			form = UserForm(request.POST)
			if form.is_valid():
				to_email_id= form.cleaned_data.get('email')
				name = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				if not AddUser.objects.filter(email=to_email_id, username=name).exists():
					data = form.save(commit=False)
					data.is_active = True
					data.save()
					user_data = AddUser.objects.filter(email=to_email_id,username=name ,datamode="Active").last()
					role_data = Role.objects.filter(role="User", datamode="Active").last()
					msg = api.assign_role(to_email_id,name,password,user_data,role_data)
					if msg:
						return redirect('login')
		
		context={
			'form' : form,
			"page_kwargs" : settings.STATIC_URL,
		}
	except Exception as e:
		print("error----",e)
	return render(request,template,context)

#AddadminForm
@logged_in
@all_admin
def make_admin(request):
	try:
		template = "admin_poll/make_admin.html"
		form = MakeAdminForm()
		if request.method =="POST":
			form = MakeAdminForm(request.POST)
			user=AddUser.objects.get(email=request.POST.get('user'), datamode="Active")
			role_data = Role.objects.get(id=request.POST.get('role'),datamode="Active")
			designation = request.POST.get('designation')
			UserRole.objects.create(
				user=user, role=role_data, designation=designation,
				created_by=request.user.email,updated_by=request.user.email,
				datamode="Active"
			)

			return redirect('home')
		context = {
			"form" : form,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		} 
	except Exception as e:
		print("eeee",e)
	return render(request, template, context)

@logged_in
@all_admin
def home(request):
	try:
		template = "admin_poll/home.html"
		data =  Banner.objects.filter(datamode="Active").order_by('-id')[:3]
		banner_count = Banner.objects.filter(datamode="Active").count()
		user_count = AddUser.objects.filter(datamode="Active")
		team_members = UserRole.objects.all()

		package_count = Package.objects.filter(datamode="Active").count()
		event_count = Events.objects.filter(datamode="Active").count()
		post_data = Post.objects.filter(datamode="Active")
		gallery_data = Gallery.objects.filter(datamode="Active")
		context = {
			"form":data,
			"post_data":post_data,
			"gallery_data":gallery_data,
			"photos":Photos.objects.all(),
			"team_members":	team_members.exclude(slug="user"),
			"page_kwargs" : settings.STATIC_URL,
			"media_kwargs" :settings.MEDIA_URL,
			"banner_count":banner_count,"gallery_count":gallery_data.count(),"post_count":post_data.count(),
			"user_count":user_count,"package_count":package_count,"event_count":event_count,
		} 
	except Exception as e:
		print("eeee",e)
	return render(request, template, context)    


@logged_in
@all_admin
def banner_add(request):
	try:
		template = 'create_banner.html'
		form = BannerForm()
		if request.method == "POST":
			category = request.POST.get('banner_category')
			form = BannerForm(request.POST, request.FILES)
			if form.is_valid():
				image_list = request.FILES.getlist('banner_image')
				for image in image_list:
					Banner.objects.create(
						banner_image = image,banner_video = request.POST.get('banner_video'),
						banner_category =  request.POST.get('banner_category'),
						created_by=to_email_id,updated_by=to_email_id

					)
					img_data =Banner.objects.latest('updated_on')
					data_from = "banner"+str(img_data.id)
					
					result,msg = api.create_signature(img_data.id,category,request.user,data_from)
				return redirect('home')
			else:
				return HttpResponse("Something Worng")
		else:
			form = BannerForm()
		context = {
			"page_kwargs" : settings.STATIC_URL,
			"media_kwargs" :settings.MEDIA_URL,
	
			"form_data":form	
		}    
	except Exception as e:
		print("eee",e)
	
	return render(request, template, context)


@logged_in
@all_admin
def edit_banner(request, id):
	try:
		template = "edit_banner.html"
		if id:
			banner_data_obj = get_object_or_404(Banner, id=id)
			form = EditBannerForm(instance=banner_data_obj)
			if request.method == "POST":
				form = EditBannerForm(request.POST,request.FILES,instance=banner_data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				# else:
				# 	form = EditBannerForm()

			context = {
				"form":form,
				
				"obj":banner_data_obj
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)    

@all_admin
def banner_delete(request, id):
	try:
		if id and request.method == "GET":
			datas = Banner.objects.filter(id=id)
			for data in datas:
				value = "banner"+str(data.id)
				ImageDuplicate.objects.filter(data_from=value,data_from_id=data.id).delete()
			Banner.objects.filter(id=id).delete()
			return redirect("home")				
	except Exception as e:
		print("eee",e)
	
@all_admin
def post(request):
	try:
		account_user =AddUser.objects.filter(email=request.user.email, datamode="Active").last()
		template = "add_post.html"
		form = PostForm()
		if request.method == "POST":
			form = PostForm(request.POST, request.FILES)
			if form.is_valid():
				data=form.save(commit=False)
				data.user = account_user
				data.save()
				return redirect('home')
			else:
				form = PostForm()
		
		context = {
			"form":form,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		
			}

	except Exception as e:
		print("error---",e)	
	return render(request, template, context)

@all_admin
def edit_post(request, id):
	try:
		template = "edit_post.html"
		if id:
			data_obj = get_object_or_404(Post, id=id)
			form = EditPostForm(instance=data_obj)
			if request.method == "POST":
				form = EditPostForm(request.POST,request.FILES,instance=data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				else:
					form = EditPostForm()

			context = {
				"form":form,
				"media_kwargs" :settings.MEDIA_URL,
				"page_kwargs" : settings.STATIC_URL,
				"obj":data_obj,
			
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)

@logged_in
@all_admin
def delete_post(request, id):
	try:
		if id:
			if request.method == "GET":
				Post.objects.filter(id=id).delete()
				return redirect("home")				
	except Exception as e:
		print("eee",e)

@logged_in
@all_admin
def gallery(request):
	try:
		account_user =AddUser.objects.filter(email=request.user.email, datamode="Active").last()
		template = "gallery.html"
		form = GalleryForm()
		if request.method == "POST":
			form = GalleryForm(request.POST, request.FILES)
			images= request.FILES.getlist('images')
			category = request.POST['category']
			
			if form.is_valid():
				user = form.save(commit=False)
				user.user = account_user
				user.save()
				for image in images:
					Photos.objects.create(
						gallery = user,
						category= category,
						images= image	
					)

				return redirect('home')
			else:
				form = GalleryForm(request.POST, request.FILES)
		
		context = {
			"form":form,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
			}

	except Exception as e:
		print("error---",e)	
	return render(request, template, context)

@logged_in
@all_admin
def edit_gallery(request, id):
	try:
		template = "edit_post.html"
		if id:
			data_obj = get_object_or_404(Photos, id=id)
			form = EditGalleryForm(instance=data_obj)
			if request.method == "POST":
				form = EditGalleryForm(request.POST,request.FILES,instance=data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				else:
					form = EditGalleryForm()

			context = {
				"form":form,
				"media_kwargs" :settings.MEDIA_URL,
				"page_kwargs" : settings.STATIC_URL,
				"obj":data_obj,
			
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)

@logged_in
@all_admin
def delete_gallery(request, id):
	try:
		if id:
			if request.method == "GET":
				Gallery.objects.filter(id=id).delete()
				return redirect("home")				
	except Exception as e:
		print("eee",e)


@logged_in
@all_admin
def package(request):
	try:
		template = "package.html"
		package = PackageForm()
		if request.method =="POST":
			package = PackageForm(request.POST)
			if package.is_valid():
				data = package.cleaned_data.get('function_name')
				if not Package.objects.filter(function_name =data, datamode="Active").exists():
					package.save()
					return redirect('home')	
				else:
					return HttpResponse("Function name is already exists")
		context ={
			"form" : package,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		
		}	


	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)

@logged_in
@all_admin
def edit_package(request, id):
	try:
		template = "edit_package.html"
		if id:
			data_obj = get_object_or_404(Package, id=id)
			form = EditPackageForm(instance=data_obj)
			if request.method == "POST":
				form = EditPackageForm(request.POST,instance=data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				else:
					form = EditPackageForm()

			context = {
				"form":form,
				"media_kwargs" :settings.MEDIA_URL,
				"page_kwargs" : settings.STATIC_URL,
				"obj":data_obj,
			
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)

@logged_in
@all_admin
def events(request):
	try:
		template = "events.html"
		events_form = EventsForm()
		if request.method =="POST":
			events_form = EventsForm(request.POST, request.FILES)
			images = request.FILES.getlist('images')
			package_name = Package.objects.get(id=request.POST.get('package'),datamode="Active")
			if events_form.is_valid():
				event_data = events_form.save(commit=False)
				event_data.package = package_name
				event_data.event_name = request.POST.get('event_name')
				event_data.created_by =request.user.email, # check this data in model you got bug
				event_data.updated_by = request.user.email,
				event_data.save()
				for image in images:
					EventImages.objects.create(
						event_name = request.POST.get('event_name'),
						images = image,
						created_by =request.user.email,
						updated_by = request.user.email,
					)
				return redirect('home')

		context ={
			"form" : events_form,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		
		}	

	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)

@logged_in
@all_admin
def edit_events(request, id):
	try:
		template = "edit_events.html"
		if id:
			data_obj = get_object_or_404(Events, id=id)
			form = EditEventsForm(instance=data_obj)
			if request.method == "POST":
				form = EditEventsForm(request.POST,request.FILES,instance=data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				else:
					form = EditEventsForm()

			context = {
				"form":form,
				"media_kwargs" :settings.MEDIA_URL,
				"page_kwargs" : settings.STATIC_URL,
				"obj":data_obj,
			
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)


#add_price_list
@logged_in
@all_admin
def add_price_list(request):
	try:
		template = "admin_poll/add_price_list.html"
		form = PriceListForm()
		if request.method =="POST":
			form = PriceListForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('home')

		context ={
			"form" : form,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		}	

	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)



@logged_in
@all_admin
def equipment(request):
	try:
		template = "equipment.html"
		equipment = EquipmentForm()
		if request.method =="POST":
			equipment = EquipmentForm(request.POST,request.FILES)
			if equipment.is_valid():
				equipment.save()
				return redirect('home')

		context ={
			"form" : equipment,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		}	

	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)


@logged_in
@all_admin
def edit_equipment(request, id):
	try:
		template = "edit_equipment.html"
		if id:
			data_obj = get_object_or_404(Equipment, id=id)
			form = EditEquipmentForm(instance=data_obj)
			if request.method == "POST":
				form = EditEquipmentForm(request.POST,request.FILES,instance=data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				else:
					form = EditEquipmentForm()

			context = {
				"form":form,
				"media_kwargs" :settings.MEDIA_URL,
				"page_kwargs" : settings.STATIC_URL,
				"obj":data_obj,
			
			}    

	except Exception as e:
		print("eeee",e)
	return render(request, template, context)


@logged_in
@all_admin
def add_about_us(request):
	try:
		template = "add_about_us.html"
		about_us = AboutUsForm()
		if request.method =="POST":
			about_us = AboutUsForm(request.POST,request.FILES)
			if about_us.is_valid():
				about_us.save()
				return redirect('home')

		context ={
			"form" : about_us,
			"media_kwargs" :settings.MEDIA_URL,
			"page_kwargs" : settings.STATIC_URL,
		}	

	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)


@logged_in
@all_admin
def edit_about_us(request, id):
	try:
		template = "edit_about_us.html"
		if id:
			data_obj = get_object_or_404(AboutUs, id=id)
			form = EditAboutUsForm(instance=data_obj)
			if request.method == "POST":
				form = EditAboutUsForm(request.POST,request.FILES,instance=data_obj)
				if form.is_valid():
					form.save()
					return redirect('home')
				else:
					form = EditAboutUsForm()

			context = {
				"form":form,
				"media_kwargs" :settings.MEDIA_URL,
				"page_kwargs" : settings.STATIC_URL,
				"obj":data_obj,
			
			}    

	except Exception as e:
		print("eeee",e)
	return render(request, template, context)

@logged_in
@all_admin
def delete_about_us(request, id):
	try:
		if id and request.method == "GET":
			AboutUs.objects.filter(id=id).delete()
			return redirect("home")				
	except Exception as e:
		print("eee",e)


@logged_in
@all_admin
def edit_profile_settings(request, email):
	try:
		template = "edit_profile_settings.html"
		profile_obj= Profile.objects.get(email=email)
		form = EditProfileForm(instance=profile_obj)
		if id and request.method == "POST":
			form = EditProfileForm(request.POST,request.FILES,instance=profile_obj)
			if form.is_valid():
				form.save()
				data = Profile.objects.get(email=request.POST.get('email'))
				session_data={
					'image':str(data.profile_pic),
					'email': request.POST.get('email'),
					'username' : request.POST.get('username')
				}
				request.session['profile']=session_data
				return redirect('home')
			else:
				form = EditProfileForm(request.POST,request.FILES,instance=profile_obj)
		context = {
			"form":form,
			"page_kwargs" : settings.STATIC_URL,
			"media_kwargs" :settings.MEDIA_URL,
			"obj":profile_obj,
		
			} 
		
	except Exception as e:
		print("eee",e)
	return render(request, template,context)


class PasswordResetConfirm(PasswordResetConfirmView):
    form_class = PasswordResetConfirmForm

    def __init__(self, *args, **kwargs):
        super(PasswordResetConfirm, self).__init__(*args, **kwargs)