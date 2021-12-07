from django.test import TestCase
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text

# Create your tests here.
# current_site = get_current_site(request)
					# mail_subject = " Welcome to Light vision Photography. Please activate your account. "
					# message = render_to_string('acc_active_email.html', {
					# 		'user': user,
					# 		'domain': current_site.domain,
					# 		'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					# 		'token': account_activation_token.make_token(user),
					# 	})
					# send_email=EmailMessage(mail_subject, message, MY_MAIL, [to_email_id])
					# send_email.send()
					# return HttpResponse('Please confirm your email address to complete the registration')

# def activate(request, uidb64, token):
# 	User = get_user_model()
# 	try:
# 		uid = force_text(urlsafe_base64_decode(uidb64))
# 		user = AddUser.objects.get(pk=uid)
# 	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
# 		user = None
# 	if user is not None and account_activation_token.check_token(user, token):
# 		user.is_active = True
# 		user.save()
# 		return redirect('login_page')

# 		# return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
# 	else:
# 		return HttpResponse('Activation link is invalid!')

# # My mail 
# MY_MAIL = "diliplj5@gmail.com"

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = MY_MAIL
# EMAIL_HOST_PASSWORD = 'xdxauijjaibxrihm'
# EMAIL_PORT = 587

# AUTH_USER_MODEL = 'admin_app.AddUser'

# def package_detail(request):
# 	try:
# 		template = "package_detail.html"
# 		package = PackageForm()
# 		events = EventsForm()
# 		equipment = EquipmentForm()

# 		if request.method == "POST":
# 			package =PackageForm(request.POST)
# 			events = EventsForm(request.POST)
# 			equipment = EquipmentForm(request.POST)
# 			if package.is_valid():
# 				data = package.cleaned_data.get('function_name')
# 				if not Package.objects.filter(function_name =data, datamode="Active").exists():
# 					package.save()
# 				else:
# 					return HttpResponse("Function name is already exists")
# 			if events.is_valid():
# 				events.save()
# 			if equipment.is_valid():	
# 				equipment.save()
# 			return redirect('home')
			
# 		context={
# 			'package' : package,
# 			'events' : events,
# 			'equipment' : equipment
# 		}
# 	except Exception as e:
# 		print(e)
	
# 	return render(request, template, context)


# def login_page(request):
# 	try:
# 		template = 'login.html'
# 		form = LoginForm()
# 		if request.method =="POST":
# 			form = LoginForm(request.POST)	
# 			if form.is_valid():
# 				email = form.cleaned_data.get('email')
# 				password = form.cleaned_data.get('password')
# 				if AddUser.objects.filter(email=email).exists():
# 					user_data = AddUser.objects.get(email=email)
# 					if check_password(password,user_data.password):
# 						user = authenticate(request,username=user_data.username, password=password)
# 						if user: 
# 							if user_data.is_active:
# 								login(request, user_data)
# 								return redirect('home')
# 							else:
# 								return HttpResponse("Email address not found")	
# 						else:
# 							return redirect('login')
# 				else:
# 					return HttpResponse("Email or password invalid")
# 		else:
# 			form = LoginForm()
# 		context = {	
# 			"form" : form,
# 			'page_url' : seo.page_kwargs['static_url']
# 		}				
# 	except Exception as e:
# 		print("error---",e)
# 	return render(request,template,context)
	
# def logout_page(request):
# 	try:
# 		logout(request)	
# 	except Exception as e:
# 		print("error",e)
# 	return redirect('login')


# def add_user_password_change(request, id):
# 	try:
# 		template = "add_user_password_change.html"
# 		if id and AddUser.objects.filter(id=id).exists():
# 			form = ChangePasswordForm()
# 			if request.method =="POST":
# 				form = ChangePasswordForm(request.POST)
# 				if form.is_valid():
# 					verify_password = form.cleaned_data.get('old_password')
# 					confirm_password = form.cleaned_data.get('confirm_password')
# 					user = AddUser.objects.filter(id=id).last()
# 					if check_password(verify_password,user.password):
# 						AddUser.objects.filter(id=id).update(password=make_password(confirm_password, confirm_password))	
# 						return redirect('login')
# 					else:
# 						return HttpResponse("password wrong")
# 		else:
# 			return HttpResponse("User not found")
# 		context = {
# 			'form':form
# 		}
# 	except Exception as e:
# 		print("eee",e)
# 	return render(request, template, context)  
