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
