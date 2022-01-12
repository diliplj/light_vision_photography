from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import django.views.static as django_static_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html',extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),name='login'),

	path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html',extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),name='logout'),

	path('accounts/password/reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_email.html',extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}), name='password_reset'),
	
	path('accounts/password/reset/done/',auth_views.PasswordResetDoneView.as_view(extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}), 
	name='password_reset_done'),
	
	
	path('accounts/password/reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),
		  name='password_reset_confirm'),
	
	path('accounts/password/reset/complete/',auth_views.PasswordResetCompleteView.as_view(extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),
	name='password_reset_complete'),
	
	path('accounts/change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html',extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),name='password_change'),
	
	path('accounts/change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html',extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),
		name='password_change_done'),

	path('admin/', admin.site.urls),
	
	path('admin_page/',include("admin_poll.urls")),
	# path('user/',include("client_app.urls")),
	# url(r'%s(?P<path>.*)$/'%(settings.STATIC_URL), django_static_view.serve, {'document_root': settings.STATIC_ROOT }),

    # url(r'^media/(?P<path>.*)$', django_static_view.serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', django_static_view.serve, {'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
