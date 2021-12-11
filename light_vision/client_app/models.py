from django.db import models
from admin_app.models import *

# Create your models here.
class Order_Detail(models.Model):
    package = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    home_address = models.TextField(null=False)
    phone_no = models.IntegerField(null=False)
    your_function_from_date = models.DateField(null=False)
    your_function_to_date = models.DateField(null=False)
    mahal_address = models.TextField(null=False)