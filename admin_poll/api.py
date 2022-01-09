from admin_poll.models import *
from admin_poll.forms import *
from admin_poll.views import *
# from admin_poll import logger_file as ub 
# from photography_jan_6.settings import MY_MAIL
from photography_jan_6 import settings
import sys
import logging
from wand.image import Image


def create_signature(category=None,user_name=None):
    if category and user_name:
        banner_img_data = Banner.objects.filter(banner_category=category)
        for img in banner_img_data:
            img_sign = Image(filename=str(settings.BASE_DIR)+str(img.banner_image.url))
            sign=img_sign.signature
            if not ImageDuplicate.objects.filter(image_signature=sign).exists(): 
                ImageDuplicate.objects.create(image_name=img.banner_image.name,
                    image_url=str(img.banner_image.url),
                    image_signature=sign,created_by=user_name,
                    updated_by=user_name)
            else:
                result= False
                msg= "Image already exists"
                ImageDuplicate.objects.filter(image_name=img.banner_image.name,image_signature=sign).delete()
                Banner.objects.filter(banner_category=category, banner_image=img.banner_image).delete()
                return result , msg
        
        result= False
        msg= "category or user not found"
        return result , msg
    else:
        result= False
        msg= "Category not found"
        return result , msg
