from django.test import TestCase

# Create your tests here.
# for img in request.FILES.getlist('banner_image'):
# 					destination = open(settings.MEDIA_ROOT, 'wb+')
# 					for chunk in img.chunks():
# 						destination.write(chunk)
# 					destination.close()



    # <form method="POST" enctype="multipart/form-data">
    #     {{request.user}}-----    
    #     {% csrf_token %}

    #     <h3>Gallery View</h3>

    #     {% for data in gallery_data %}
        
    #         <div>{{data.label}}</div>
    #         <div>{{data.user}}</div>
    #         <div>{{data.category}}</div> 
    #         <div>{{data.short_description}}</div>
    #         <div>{{data.detail_description}}</div>
    #         <a href="{% url 'edit_gallery' data.id %}"> Edit Gallery </a>
    #         <a href="{% url 'delete_gallery' data.id %}"> Delete Gallery </a>
    #     {% endfor %}
        
    #     {% for photo in photos %}
    #     <div><img src="{{ photo.images.url }}" class="img-responsive" style="width: 100%; float: left; margin-right: 10px;" /></div>
    #     {% endfor %}

    #     {% for data in post_data %}
    #         <div>{{data.label}}</div>
    #         <div>{{data.user}}</div>
    #         <div>{{data.category}}</div>
    #         <div><img src="{{ data.image.url }}" class="img-responsive" style="width: 100%; float: left; margin-right: 10px;" /></div>
    #         <div>{{data.short_description}}</div>
    #         <div>{{data.detail_description}}</div>
    #         <a href="{% url 'edit_post' data.id %}"> Edit Post </a>
    #         <a href="{% url 'delete_post' data.id %}"> Delete Post </a>
    #     {% endfor %}

    #     <h3>Banner View</h3>

    #     {% for data in form %}
    #         <div>{{data.label}}</div>
    #         <div>{{data.category}}</div>
    #         {{ data.banner_image.url }}
        
    #         <img src="{{ data.banner_image.url }}" class="img-responsive" style="width: 100%; float: left; margin-right: 10px;" />
    #         <!-- <video width="500" height="500" controls >
    #             <source src="{{data.banner_video.url}}" type="video/mp4">
    #             <b>{{video.title}}</b>
    #         </video> -->
            
    #         <a href="{% url 'edit_banner' data.id %}">Edit Banner </a>
    #             <br>
    #         <a href="{% url 'banner_delete' data.id %}">Delete Banner </a>    
    #     {% endfor %}
    #     <a href="{% url 'banner_add' %}"> Banner Add </a>  

    #     <br>
    #     {% comment %}
    #     <!-- <a href="{% url 'add_user_password_change' request.user.id %}"> Change My Password </a> -->
    #     {% endcomment %}
    # </form>


# Home

#     <!-- {% extends 'base.html' %}

# {% block title %} Admin Home {% endblock %}

# {% block content %}
#     <h3 class="text-center">Admin Home View</h3>
    
#     <a href="{% url 'login' %}"> Already have an account? </a> <br>
#     <a href="{% url 'add_user' %}"> Add new user </a> <br>
#     <a href="{% url 'post' %}"> Add post </a> <br>
#     <a href="{% url 'gallery' %}"> Add Gallery </a> <br>
#     <a href="{% url 'package' %}"> Add Package   </a> <br>
#     <a href="{% url 'events' %}"> Add Events   </a> <br>
#     <a href="{% url 'password_reset' %}"> password_reset   </a> <br>
#     <a href="{% url 'logout' %}">Logout</a>
# </div>
# </div>
# {% endblock %} -->