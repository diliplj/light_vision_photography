# from django.shortcuts import render, redirect
# from admin_app.models import *
# from django.conf import settings
# from django.contrib.auth.models import User, Group
# from django.http import HttpResponse

# import pprint

# group = Group.objects.filter(name="admin").last()
# sub_admin = Group.objects.filter(name="sub_admin").last()

# def admin_only(func):
#     def wrapper(request, *args, **kwargs):
#         try:
#             if request.user.is_authenticated:
#                 if User.objects.filter(username= request.user, groups__name=group).exists():
#                     return func(request, *args, **kwargs)
#                 else:
#                     return HttpResponse("Sorry You are not authorized to view this page")   
#             else:
#                 return redirect('login_page')

#         except Exception as e:
#             return HttpResponse(e)
    
#     return wrapper

# def sub_admin_only(func):
#     def wrapper(request, *args, **kwargs):
#         try:
#             if request.user.is_authenticated:
#                 if User.objects.filter(username= request.user, groups__name=sub_admin).exists():
#                     return func(request, *args, **kwargs)
#                 else:
#                     return HttpResponse("Sorry You are not authorized to view this page")   
#             else:
#                 return redirect('login_page')

#         except Exception as e:
#             return HttpResponse(e)
#     return wrapper

# def all_admin(func):
#     def wrapper(request, *args, **kwargs):
#         try:
#             if request.user.is_authenticated:
#                 if User.objects.filter(username= request.user, groups__name=sub_admin).exists() or \
#                     User.objects.filter(username= request.user, groups__name=group).exists():
#                     return func(request, *args, **kwargs)
#                 else:
#                     return HttpResponse("Sorry You are not authorized to view this page")   
#             else:
#                 return redirect('login_page')

#         except Exception as e:
#             return HttpResponse(e)
#     return wrapper
