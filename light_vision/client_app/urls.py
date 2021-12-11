from admin_app import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home/",views.home, name="home"),

]