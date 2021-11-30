from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import django.views.static as django_static_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include("admin_app.urls")),

    url(r'^static/(?P<path>.*)$', django_static_view.serve,{'document_root', settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', django_static_view.serve,{'document_root', settings.MEDIA_ROOT}),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
             
