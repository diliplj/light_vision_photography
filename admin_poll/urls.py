from admin_poll import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('signup/', views.add_user, name = "add_user"),
    path('make_admin/', views.make_admin, name = "make_admin"),
	path('accounts/password/reset/confirm/<uidb64>/<token>/',views.PasswordResetConfirm.as_view(extra_context={'page_kwargs':{'static_url':settings.STATIC_URL}}),
		  name='password_reset_confirm'),

    path("home/",views.home, name="home"),
    path("banner_add/",views.banner_add, name="banner_add"),
    path("banner_delete/<int:id>/",views.banner_delete, name="banner_delete"),    
    path("edit_banner/<int:id>/", views.edit_banner, name="edit_banner"),

    path("post/",views.post, name="post"),
    path("edit_post/<int:id>/", views.edit_post, name="edit_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),
    
    path("gallery/",views.gallery, name="gallery"),
    path("edit_gallery/<int:id>/", views.edit_gallery, name="edit_gallery"),
    path("delete_gallery/<int:id>/", views.delete_gallery, name="delete_gallery"),

    path("package/", views.package, name="package"),
    path("edit_package/<int:id>/", views.edit_package, name="edit_package"),
    path("events/", views.events, name="events"),
    path("edit_events/<int:id>/", views.edit_events, name="edit_events"),
    path("equipment/", views.equipment, name="equipment"),
    path("edit_equipment/<int:id>/", views.edit_equipment, name="edit_equipment"),
    path("add_about_us/",views.add_about_us, name="about_us"),
    path("edit_about_us/<int:id>/",views.edit_about_us, name="edit_about_us"),
    path("delete_about_us/<int:id>/",views.delete_about_us, name="delete_about_us"),

    # price list
    path("add_price_list/",views.add_price_list, name="price_list"),
    #path("edit_price_list/<int:id>/",views.edit_price_list, name="edit_price_list"),

    # profile settings
    path("edit_profile_settings/<str:email>/",views.edit_profile_settings, name="edit_profile_settings"),
    # path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),

]