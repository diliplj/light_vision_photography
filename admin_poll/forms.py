
from django.db.models import fields
from django.http import request
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractBaseUser
from django.forms import Widget
import re
from wand.image import Image
from django.contrib.auth.forms import *
# from phonenumber_field.formfields import PhoneNumberField


def password_validator(password):
	err = ''
	if re.search('[a-z]', password) is None:
		err='The password must contain at least one lowercase character.'
		
	if re.search('[A-Z]', password) is None:
		err='The password must contain at least one uppercase character.'
	
	if re.search('[0-9]', password) is None:
		err='The password must contain at least one uppercase character.'
	
	if len(password) <8:
		err="Password length should be atleast 8 "
	return err


class MakeAdminForm(forms.ModelForm):
	user = forms.EmailField(label ='Enter the user email address',required=True, max_length=255)
	role = forms.ModelChoiceField(required=True, queryset=Role.objects.filter(datamode='Active'))
	designation = forms.CharField(label="Designation eg- Photographer",required=True, max_length=255)
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop("request", None)
		kwargs.setdefault('label_suffix', '')
		super(MakeAdminForm, self).__init__(*args, **kwargs)
		self.fields['role'].queryset = Role.objects.filter(datamode='Active')


	class Meta:
		model = UserRole
		fields = ['user', 'role','designation']	

class UserForm(forms.ModelForm):
	# role = forms.ModelChoiceField(required=True, queryset=Role.objects.filter(datamode='A').order_by('role'))
	# def __init__(self, *args, **kwargs):
	# 	self.request = kwargs.pop("request", None)
	# 	kwargs.setdefault('label_suffix', '')
	# 	super(UserForm, self).__init__(*args, **kwargs)
	# 	self.fields['role'].empty_label = 'Select the role for user'
	# 	self.fields['role'].queryset = Role.objects.filter(datamode='Active').order_by('role')

	class Meta:
		model = AddUser
		fields = ['email', 'username' ,'password']	
	
	def clean_password(self):
		password = self.cleaned_data.get('password')
		print("111111password",password)
		err = password_validator(password)
		print("err",err)
		if err:	
			print("errrrrrr")
			raise forms.ValidationError(err)
		return password
		
class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(label="Old Password",required=True, max_length=255)
	new_password = forms.CharField(required=True, max_length=255)
	confirm_password = forms.CharField(required=True, max_length=255)
	
	def clean(self):          
		password1 = self.cleaned_data.get('new_password')
		password2 = self.cleaned_data.get('confirm_password')
		password_validator(password1)
		if password1 != password2:
			raise forms.ValidationError("Password Mismatch")

class LoginForm(forms.Form):
	email = forms.EmailField(required=True, max_length=255) 
	password = forms.CharField(required=True, max_length=255)
			
class BannerForm(forms.ModelForm):
	banner_image = forms.FileField(label="Banner Images",widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model = Banner
		exclude = ['image_list','slug','updated_on','datamode','created_on']			

class EditBannerForm(forms.ModelForm):
	class Meta:
		model = Banner
		exclude = ['slug','updated_on','datamode','created_on']			

class PostForm(forms.ModelForm):
	
	# def __init__(self, *args, **kwargs):
	# 	super(PostForm, self).__init__(*args, **kwargs)
	# 	self.fields['title'].label = "Category"
	
	class Meta:
		model = Post
		exclude = ['user','slug','updated_on','datamode','created_on']			

class EditPostForm(forms.ModelForm):
	
	# def __init__(self, *args, **kwargs):
	# 	super(PostForm, self).__init__(*args, **kwargs)
	# 	self.fields['title'].label = "Category"
	
	class Meta:
		model = Post
		exclude = ['user','slug','updated_on','datamode','created_on']

class GalleryForm(forms.ModelForm):
	images = forms.FileField(label="Images",widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		model = Gallery
		exclude = ['user','slug','updated_on','datamode','created_on']

class EditGalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		exclude = ['user','slug','updated_on','datamode','created_on']

#------------------------------

class PackageForm(forms.ModelForm):
	class Meta:
		model = Package
		exclude = ['slug','updated_on','datamode','created_on']

class EditPackageForm(forms.ModelForm):
	class Meta:
		model = Package
		exclude = ['slug','updated_on','datamode','created_on']

class EventsForm(forms.ModelForm):
	package = forms.ModelChoiceField(required=True, queryset=Package.objects.filter(datamode='A'))

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop("request", None)
		kwargs.setdefault('label_suffix', '')
		super(EventsForm, self).__init__(*args, **kwargs)
		self.fields['package'].empty_label = 'Select the function '
		self.fields['package'].queryset = Package.objects.filter(datamode='Active')

	class Meta:
		model = Events
		exclude = ['slug','updated_on','datamode','created_on']


class EditEventsForm(forms.ModelForm):
	class Meta:
		model = Events
		exclude = ['slug','updated_on','datamode','created_on']

class EquipmentForm(forms.ModelForm):
	package = forms.ModelChoiceField(required=True, queryset=Package.objects.filter(datamode='A'))
	event = forms.ModelChoiceField(required=True, queryset=Events.objects.filter(datamode='A'))	

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop("request", None)
		kwargs.setdefault('label_suffix', '')
		super(EquipmentForm, self).__init__(*args, **kwargs)
		self.fields['package'].empty_label = 'Select the function'
		self.fields['package'].queryset = Package.objects.filter(datamode='Active')
		self.fields['event'].empty_label = 'Select the funtion event'
		self.fields['event'].queryset = Events.objects.filter(datamode='Active')

	class Meta:
		model = Equipment
		exclude = ['slug','updated_on','datamode','created_on']

class EditEquipmentForm(forms.ModelForm):
	class Meta:
		model = Equipment
		exclude = ['slug','updated_on','datamode','created_on']

class PasswordResetConfirmForm(SetPasswordForm):
	def __init__(self, *args, **kwargs):
		super(PasswordResetConfirmForm, self).__init__(*args, **kwargs)

	def clean_new_password2(self):
		password1 = self.cleaned_data.get('new_password1')
		password2 = self.cleaned_data.get('new_password2')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError("Password miss matched")
		return password2	
		
class AboutUsForm(forms.ModelForm):
	class Meta:
		model = AboutUs
		exclude = ['updated_on','created_on']

class EditAboutUsForm(forms.ModelForm):
	class Meta:
		model = AboutUs
		exclude = ['updated_on','created_on']		

#profile
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['updated_on','created_on','created_by','updated_by']


class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['updated_on','created_on','created_by','updated_by']