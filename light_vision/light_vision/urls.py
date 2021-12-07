from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import django.views.static as django_static_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('accounts/login/', auth_views.LoginView.as_view(),name='login'),

	path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
	path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	
	path('accounts/password/reset/done/',auth_views.PasswordResetDoneView.as_view(), 
	name='password_reset_done'),
	
	
	path('accounts/password/reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
		  name='password_reset_confirm'),
	
	path('accounts/password/reset/complete/',auth_views.PasswordResetCompleteView.as_view(),
	name='password_reset_complete'),
	
	path('accounts/change-password/',auth_views.PasswordChangeView.as_view(),name='password_change'),
	
	path('accounts/change-password/done/', auth_views.PasswordChangeDoneView.as_view(),
		name='password_change_done'),

	path('admin/', admin.site.urls),

	path('',include("admin_app.urls")),
	url(r'^static/(?P<path>.*)$', django_static_view.serve,{'document_root', settings.STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', django_static_view.serve,{'document_root', settings.MEDIA_ROOT}),

]
if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							  document_root=settings.MEDIA_ROOT)
			 
