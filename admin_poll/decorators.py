from django.shortcuts import render, redirect
from admin_poll.models import *
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib import messages


def logged_in(func):
    def wrapper(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                if UserRole.objects.filter(user= request.user, role__role="Admin").exists() \
                    or UserRole.objects.filter(user= request.user, role__role="Super Admin").exists():
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponse("Sorry You are not authorized to view this page")   
            else:
                messages.error(request,("You are not logged in"))
                return redirect('login')

        except Exception as e:
            return HttpResponse(e)
    
    return wrapper


def admin_only(func):
    def wrapper(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                if UserRole.objects.filter(user= request.user, role__role="Admin").exists():
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponse("Sorry You are not authorized to view this page")   
            else:
                messages.error(request,("You are not logged in"))
                return redirect('login')

        except Exception as e:
            return HttpResponse(e)
    
    return wrapper

def super_admin_only(func):
    def wrapper(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                if UserRole.objects.filter(user= request.user, role__role="Super Admin").exists():
                    return func(request, *args, **kwargs)
                else:
                    return redirect('login')
            else:
                messages.error(request,("You are not logged in"))
                return redirect('login')

        except Exception as e:
            return HttpResponse(e)
    return wrapper

def all_admin(func):
    def wrapper(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                if UserRole.objects.filter(user= request.user, role__role="Admin").exists() or UserRole.objects.filter(user= request.user, role__role="Super Admin").exists():
                    print("1111")
                    return func(request, *args, **kwargs)
                else:
                    print("2222")
                    return HttpResponse("Sorry You are not authorized to view this page")   
            else:
                messages.error(request,("You are not logged in"))
                return redirect('login')

        except Exception as e:
            return HttpResponse(e)
    return wrapper
