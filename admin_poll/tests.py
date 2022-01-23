# from django.test import TestCase

# # Create your tests here.
# # for img in request.FILES.getlist('banner_image'):
# # 					destination = open(settings.MEDIA_ROOT, 'wb+')
# # 					for chunk in img.chunks():
# # 						destination.write(chunk)
# # 					destination.close()



#     # <form method="POST" enctype="multipart/form-data">
#     #     {{request.user}}-----    
#     #     {% csrf_token %}

#     #     <h3>Gallery View</h3>

#     #     {% for data in gallery_data %}
        
#     #         <div>{{data.label}}</div>
#     #         <div>{{data.user}}</div>
#     #         <div>{{data.category}}</div> 
#     #         <div>{{data.short_description}}</div>
#     #         <div>{{data.detail_description}}</div>
#     #         <a href="{% url 'edit_gallery' data.id %}"> Edit Gallery </a>
#     #         <a href="{% url 'delete_gallery' data.id %}"> Delete Gallery </a>
#     #     {% endfor %}
        
#     #     {% for photo in photos %}
#     #     <div><img src="{{ photo.images.url }}" class="img-responsive" style="width: 100%; float: left; margin-right: 10px;" /></div>
#     #     {% endfor %}

#     #     {% for data in post_data %}
#     #         <div>{{data.label}}</div>
#     #         <div>{{data.user}}</div>
#     #         <div>{{data.category}}</div>
#     #         <div><img src="{{ data.image.url }}" class="img-responsive" style="width: 100%; float: left; margin-right: 10px;" /></div>
#     #         <div>{{data.short_description}}</div>
#     #         <div>{{data.detail_description}}</div>
#     #         <a href="{% url 'edit_post' data.id %}"> Edit Post </a>
#     #         <a href="{% url 'delete_post' data.id %}"> Delete Post </a>
#     #     {% endfor %}

#     #     <h3>Banner View</h3>

#     #     {% for data in form %}
#     #         <div>{{data.label}}</div>
#     #         <div>{{data.category}}</div>
#     #         {{ data.banner_image.url }}
        
#     #         <img src="{{ data.banner_image.url }}" class="img-responsive" style="width: 100%; float: left; margin-right: 10px;" />
#     #         <!-- <video width="500" height="500" controls >
#     #             <source src="{{data.banner_video.url}}" type="video/mp4">
#     #             <b>{{video.title}}</b>
#     #         </video> -->
            
#     #         <a href="{% url 'edit_banner' data.id %}">Edit Banner </a>
#     #             <br>
#     #         <a href="{% url 'banner_delete' data.id %}">Delete Banner </a>    
#     #     {% endfor %}
#     #     <a href="{% url 'banner_add' %}"> Banner Add </a>  

#     #     <br>
#     #     {% comment %}
#     #     <!-- <a href="{% url 'add_user_password_change' request.user.id %}"> Change My Password </a> -->
#     #     {% endcomment %}
#     # </form>


# # Home

# #     <!-- {% extends 'base.html' %}

# # {% block title %} Admin Home {% endblock %}

# # {% block content %}
# #     <h3 class="text-center">Admin Home View</h3>
    
# #     <a href="{% url 'login' %}"> Already have an account? </a> <br>
# #     <a href="{% url 'add_user' %}"> Add new user </a> <br>
# #     <a href="{% url 'post' %}"> Add post </a> <br>
# #     <a href="{% url 'gallery' %}"> Add Gallery </a> <br>
# #     <a href="{% url 'package' %}"> Add Package   </a> <br>
# #     <a href="{% url 'events' %}"> Add Events   </a> <br>
# #     <a href="{% url 'password_reset' %}"> password_reset   </a> <br>
# #     <a href="{% url 'logout' %}">Logout</a>
# # </div>
# # </div>
# # {% endblock %} -->





# <style>
#  #sidebarMenu {
#   padding-left: 1ch;
#   color: #393a3d !important;
# }
# .nav-item:hover{
#   padding-left: .2ch;
  
# }
# .nav-link:hover{
# color: black;
# font-family:sans-serif;
# }
# /* .nav-link{
# font-family:sans-serif;
# } */
# </style>
# <!--- side bar -->
# <div id="sidebarMenu" class="flex-grow-0 position-absolute shadow-sm border-white" style="min-width:250px; line-height:2.5; background-color: #ffffff; border-right: 1px solid #ffffff;">
#   <div class="d-grid p-3 mt-1">
#     <img src="{{page_kwargs}}image/logo.png" width="180px" class="me-4" alt="...">
#     <!-- <button type="button" class="btn btn-block btn-lg" data-bs-toggle="modal" data-bs-target="#AddStory" style="background-color: #247CF0; font-size:large; font-weight: 500; color: white;"><i class="bi bi-plus-lg fs-7 me-2"></i>Lights Vision</button> -->
#   </div>
#   <div class="p-3 px-1 mt-1">
#     <p class="text-uppercase text-dark px-2">Home</p>
#     <ul class="navbar-nav nav-pills">
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'home' %}active{% else %}text-dark{% endif %}" aria-current="page" href="{% url 'home' %}" data-bs-toggle="modal" data-bs-target="#AddStory"><i class="bi bi-plus-lg fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/dashboard.svg" width="20px" class="me-4" alt="...">
#           Dashboard</a>
#       </li>

#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'banner_add' %}active{% else %}text-dark{% endif %}" aria-current="page" href="{% url 'banner_add' %}" data-bs-toggle="modal" data-bs-target="#AddStory"><i class="bi bi-plus-lg fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/new.svg" width="20px" class="me-4" alt="...">
#           Add Banner</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'post' %}active{% else %}text-dark {% endif %}" aria-current="page" href="{% url 'post' %}"><i class="bi bi-cloud-check fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/post.svg" width="20px" class="me-4" alt="...">
#           Add Post</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'gallery' %}active{% else %}text-dark {% endif %}" aria-current="page" href="{% url 'gallery' %}"><i class="bi bi-clock fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/gallery.svg" width="20px" class="me-4" alt="...">
#           Add Gallery</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'package' %}active{% else %}text-dark{% endif %}" aria-current="page" href="{% url 'package' %}"><i class="bi bi-file-earmark fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/package.svg" width="20px" class="me-4" alt="...">
#           Add Package</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'events' %}active{% else %}text-dark{% endif %}" aria-current="page" href="{% url 'events' %}"><i class="bi bi-file-earmark fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/event.svg" width="20px" class="me-4" alt="...">
#           Add Events</a>
#       </li>
#     </ul>
#   </div>
#   <div class="p-3 my-0">
#     <p class="bi bi-plus-lg fs-7 fw-bold me-2 px-2 text-dark" style="font-size: large;">Account</p>
#     <ul class="navbar-nav nav-pills">
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'add_user' %}active {% else %}text-dark {% endif %}" aria-current="page" href="{% url 'add_user' %}"><i class="bi bi-house-door fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/user.svg" width="20px" class="me-4" alt="...">
#           Add New User</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'password_reset' %}active{% else %}text-dark{% endif %}" aria-current="page" href="{% url 'password_reset' %}"><i class="bi bi-file-earmark fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/password.svg" width="20px" class="me-4 mt-0" alt="...">
#           Password Reset</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'logout' %}active {% else %}text-dark {% endif %}" aria-current="page" href="{% url 'logout' %}"><i class="bi bi-house-door fs-7 fw-bold me-2 ms-2"></i>
#           <img src="{{page_kwargs}}image/logout.svg" width="20px" class="me-4" alt="...">
#           Logout</a>
#       </li>
#     </ul>

#   </div>
# </div>
#   <!-- <div class="p-3">
#     <p class="fs-7 fw-bold text-uppercase text-dark">Library</p>
#     <ul class="navbar-nav nav-pills">
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'videos' %}active{% else %}text-dark {% endif %}" aria-current="page" href="#"><i class="bi bi-camera-reels fs-7 fw-bold me-2 ms-2"></i>Videos</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'images' %}active{% else %}text-dark {% endif %}" aria-current="page" href="#"><i class="bi bi-images fs-7 fw-bold me-2 ms-2"></i>Images</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'audios' %}active{% else %}text-dark {% endif %}" aria-current="page" href="#"><i class="bi bi-music-note-beamed fs-7 fw-bold me-2 ms-2"></i>Audios</a>
#       </li>
#       <li class="nav-item medium">
#         <a class="nav-link text-capitalize {% if active == 'icons' %}active{% else %}text-dark {% endif %}" aria-current="page" href="#"><i class="bi bi-emoji-heart-eyes fs-7 fw-bold me-2 ms-2"></i>Icons</a>
#       </li>
#     </ul>
#   </div> -->
#   <!-- <div class="p-3 pb-5">
#     <p class="fs-7 fw-bold text-uppercase text-dark">Projects</p>
#     <ul class="navbar-nav nav-pills mb-2" id="id_project_side_menu">
#       <li class="nav-item">
#         <a class="nav-link text-capitalize text-dark medium d-flex align-items-center " href="javascript:void(0)" onclick="javascript:load_project_create_form()"  data-bs-toggle="modal" data-bs-target="#NewProject">
#           <i class="bi bi-plus-lg fs-7 fw-bold me-2 ms-2"></i>
#           New
#         </a>
#       </li>
#     </ul>
#   </div> -->
# <!--- side bar -->


# language
# <!-- <div class="dropdown-menu dropdown-menu-end dropdown-menu-animated topbar-dropdown-menu">

            #     <!-- item-->
            #     <a href="javascript:void(0);" class="dropdown-item notify-item">
            #         <img src="{{page_kwargs}}image/flags/germany.jpg" alt="user-image" class="me-1" height="12"> <span
            #             class="align-middle">German</span>
            #     </a>

            #     <!-- item-->
            #     <a href="javascript:void(0);" class="dropdown-item notify-item">
            #         <img src="{{page_kwargs}}image/flags/italy.jpg" alt="user-image" class="me-1" height="12"> <span
            #             class="align-middle">Italian</span>
            #     </a>

            #     <!-- item-->
            #     <a href="javascript:void(0);" class="dropdown-item notify-item">
            #         <img src="{{page_kwargs}}image/flags/spain.jpg" alt="user-image" class="me-1" height="12"> <span
            #             class="align-middle">Spanish</span>
            #     </a>

            #     <!-- item-->
            #     <a href="javascript:void(0);" class="dropdown-item notify-item">
            #         <img src="{{page_kwargs}}image/flags/russia.jpg" alt="user-image" class="me-1" height="12"> <span
            #             class="align-middle">Russian</span>
            #     </a>

            # </div>