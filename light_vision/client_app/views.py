# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse

from admin_app.models import *
from admin_app.forms import *
from admin_app import logger_file as ub 
from light_vision.settings import MY_MAIL
from light_vision import settings
import sys
from admin_app import seo

# Create your views here.
def home(request):
	try:
		print("********")
		template = "client_app/home.html"
		if request.method =="GET":
			data =  Banner.objects.filter(datamode="Active")
			post_data = Post.objects.filter(datamode="Active")
			gallery_data = Gallery.objects.filter(datamode="Active")
			context = {
				"form":data,
				'page_url' : seo.page_kwargs['static_url'],
				"post_data":post_data,
				"gallery_data":gallery_data,
				"photos":Photos.objects.all(),
			} 
	except Exception as e:
		print("eeee",e)
	return render(request, template, context)    

