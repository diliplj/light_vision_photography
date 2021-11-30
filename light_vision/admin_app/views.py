from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .decorators import *
from admin_app.models import *
from admin_app.forms import *
from admin_app import logger_file as ub 
from light_vision.settings import MY_MAIL

import sys
import logging
from . import seo

"""
NOTE : In forms you can use form.save() for forms.ModelForm  but for forms.Form you 
cannot use that form.save() so You need to create variable for model 
eg : var = student.objects.get(email=email) and then you should save the variable like 
var.save()


NOTE : make_password('123') # make_password used to encrypt the password 
because User model will allow encrpyt password only
"""

logger = logging.getLogger('app')

def add_user(request):
	context = {}
	page_kwargs = {}
	page_kwargs['static_root'] = STATIC_ROOT
	page_kwargs['static_url'] = STATIC_URL 
	try:
		to_email_id = None
		template = 'add_admin.html'
		form = UserForm()
		user_data = None
		if request.method == "POST":
			form = UserForm(request.POST)
			if form.is_valid():
				to_email_id= form.cleaned_data.get('email')
				name = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user_role_data = form.cleaned_data.get('role')
				if not AddUser.objects.filter(email=to_email_id, username=name).exists():
					data = form.save(commit=False)
					data.is_active = True
					data.save()
					user_data = AddUser.objects.filter(email=to_email_id,username=name ,datamode="Active").last()
					role_data = Role.objects.filter(role=user_role_data, datamode="Active").last()
					AddUser.objects.filter(email=to_email_id,username=name ,datamode="Active").update(password=make_password(password))
					UserRole.objects.create(user=user_data,role=role_data,datamode="Active")
					return redirect('login')
				else:
					return HttpResponse("This ",to_email_id, " is already exists")
			else:
				return HttpResponse("Something Went Wrong")
		context = {
			'form' :form,
			'page_kwargs' : page_kwargs
		}
	except Exception as e:
		print("error----",e)
	return render(request,template,context)


def add_user_password_change(request, id):
	try:
		template = "add_user_password_change.html"
		if id and AddUser.objects.filter(id=id).exists():
			form = ChangePasswordForm()
			if request.method =="POST":
				form = ChangePasswordForm(request.POST)
				print("111",request.POST)
				if form.is_valid():
					verify_password = form.cleaned_data.get('old_password')
					confirm_password = form.cleaned_data.get('confirm_password')
					print("222")
					user = AddUser.objects.filter(id=id).last()
					if check_password(verify_password,user.password):
						AddUser.objects.filter(id=id).update(password=make_password(confirm_password, confirm_password))	
						return redirect('login')
					else:
						print("4444")
						return HttpResponse("password wrong")
		else:
			print("555")
			return HttpResponse("User not found")
		context = {
			'form':form
		}
	except Exception as e:
		print("eee",e)
	return render(request, template, context)  

def login_page(request):
	try:
		template = 'login.html'
		form = LoginForm()
		if request.method =="POST":
			form = LoginForm(request.POST)	
			if form.is_valid():
				email = form.cleaned_data.get('email')
				password = form.cleaned_data.get('password')
				if AddUser.objects.filter(email=email).exists():
					user_data = AddUser.objects.get(email=email)
					if check_password(password,user_data.password):
						user = authenticate(request,username=user_data.username, password=password)
						if user: 
							if user_data.is_active:
								login(request, user_data)
								return redirect('home')
							else:
								return HttpResponse("Email address not found")	
						else:
							return redirect('login')
				else:
					return HttpResponse("Email or password invalid")
		else:
			form = LoginForm()
		context = {	
			"form" : form,
			'page_url' : seo.page_kwargs['static_url']
		}				
	except Exception as e:
		print("error---",e)
	return render(request,template,context)
	
def logout_page(request):
	try:
		logout(request)	
	except Exception as e:
		print("error",e)
	return redirect('login')


def banner_add(request):
	try:
		template = 'create_banner.html'
		form = BannerForm()
		if request.method == "POST":
			form = BannerForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('home')
			else:
				return HttpResponse("Something Worng")
		else:
			form = BannerForm()
		context = {
			"form_data":form,
			'page_url' : seo.page_kwargs['static_url']
		}    
			
	except Exception as e:
		print("eee",e)
	
	return render(request, template, context)

def home(request):
	try:
		template = "home.html"
		if request.method =="GET":
			data =  Banner.objects.filter(datamode="Active")
			post_data = Post.objects.filter(datamode="Active")
			gallery_data = Gallery.objects.filter(datamode="Active")
			context = {
				"form":data,
				'page_url' : seo.page_kwargs['static_url'],
				"post_data":post_data,
				"gallery_data":gallery_data
			} 
	except Exception as e:
		print("eeee",e)
	return render(request, template, context)    


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
				"obj":banner_data_obj,
				'page_url' : seo.page_kwargs['static_url']
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)    


def banner_delete(request, id):
	try:
		if id:
			if request.method == "GET":
				Banner.objects.filter(id=id).delete()
				return redirect("home")				
	except Exception as e:
		print("eee",e)
	

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
				if Post.object.filter(user__email=account_user.email, datamode="Active").exists():
					Post.object.filter(user__email=account_user.email, datamode="Active").update(datamode="Inactive")
				form = PostForm()
		
		context = {
			"form":form,
			'page_url' : seo.page_kwargs['static_url']
			}

	except Exception as e:
		print("error---",e)	
	return render(request, template, context)

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
				"obj":data_obj,
				'page_url' : seo.page_kwargs['static_url']
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)


def delete_post(request, id):
	try:
		if id:
			if request.method == "GET":
				Post.objects.filter(id=id).delete()
				return redirect("home")				
	except Exception as e:
		print("eee",e)


def gallery(request):
	try:
		account_user =AddUser.objects.filter(email=request.user.email, datamode="Active").last()
		template = "gallery.html"
		form = GalleryForm()
		if request.method == "POST":
			form = GalleryForm(request.POST, request.FILES)
			if form.is_valid():
				user = form.save(commit=False)
				user.user = account_user
				user.save()
				return redirect('home')
			else:
				if Gallery.object.filter(user__email=account_user.email, datamode="Active").exists():
					Gallery.object.filter(user__email=account_user.email, datamode="Active").update(datamode="Inactive")
				form = GalleryForm()
		
		context = {
			"form":form,
			'page_url' : seo.page_kwargs['static_url']
			}

	except Exception as e:
		print("error---",e)	
	return render(request, template, context)


def edit_gallery(request, id):
	try:
		template = "edit_post.html"
		if id:
			data_obj = get_object_or_404(Gallery, id=id)
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
				"obj":data_obj,
				'page_url' : seo.page_kwargs['static_url']
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)

def delete_gallery(request, id):
	try:
		if id:
			if request.method == "GET":
				Gallery.objects.filter(id=id).delete()
				return redirect("home")				
	except Exception as e:
		print("eee",e)


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
			"package" : package,
			'page_url' : seo.page_kwargs['static_url']
		}	


	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)

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
				"obj":data_obj,
				'page_url' : seo.page_kwargs['static_url']
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)

def events(request):
	try:
		template = "events.html"
		events = EventsForm()
		if request.method =="POST":
			events = EventsForm(request.POST)
			if events.is_valid():
				events.save()
				return redirect('home')

		context ={
			"events" : events,
			'page_url' : seo.page_kwargs['static_url']
		}	

	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)

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
				"obj":data_obj,
				'page_url' : seo.page_kwargs['static_url']
			}    

	except Exception as e:
		print("eeee",e)
	
	return render(request, template, context)

def equipment(request):
	try:
		template = "equipment.html"
		equipment = EquipmentForm()
		if request.method =="POST":
			equipment = EquipmentForm(request.POST)
			if equipment.is_valid():
				equipment.save()
				return redirect('home')

		context ={
			"equipment" : equipment,
			'page_url' : seo.page_kwargs['static_url']
		}	

	except Exception as e:
		print("Error ----",e)

	return render(request, template, context)

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
				"obj":data_obj,
				'page_url' : seo.page_kwargs['static_url']
			}    

	except Exception as e:
		print("eeee",e)
	return render(request, template, context)
