from django.db import models
from django.template.defaultfilters import slugify
from . import choices as ch

from django.contrib.auth.models import User, AbstractUser
# on_delete=models.CASCADE it will delete all the data when ForeignKey table was deleted
# on_delete=models.SET_NULL it will not delete all the data even when ForeignKey table was deleted


# Create your models here.

class AddUser(AbstractUser):
	email  = models.EmailField(max_length=255, null=False)
	# username   = models.CharField(max_length=255, unique=True, null=True)
	# password = models.CharField(max_length=255, null=False)
	# is_active   = models.BooleanField(default=True)  
	# slug = models.SlugField(max_length=255,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(AddUser, self).save(*args, **kwargs)
		if self.username:
			self.slug = slugify(self.username)
			super(AddUser, self).save()

	class Meta:
		db_table = "AddUser"
		verbose_name="AddUser"
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):

		return "{0}".format(self.email)
		
class Role(models.Model):
	role = models.CharField(max_length=255, null=False)
	slug = models.SlugField(max_length=255,null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(Role, self).save(*args, **kwargs)
		if self.role:
			self.slug = slugify(self.role)
			super(Role, self).save()

	class Meta:
		db_table = "Role"
		verbose_name = "Role"

	def __str__(self):
		return "{0}".format(self.role)


class UserRole(models.Model):
	user = models.ForeignKey(AddUser, on_delete=models.CASCADE)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=255,null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(UserRole, self).save(*args, **kwargs)
		if self.role:
			self.slug = slugify(self.role)
			super(UserRole, self).save()

	class Meta:
		db_table = "UserRole"
		verbose_name = "UserRole"


class Package(models.Model):
	function_name = models.CharField(max_length=100, null=False)
	amount     = models.IntegerField(default=0)
	number_of_days = models.IntegerField(default=0)
	slug = models.SlugField(max_length=255,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(Package, self).save(*args, **kwargs)
		if self.function_name:
			self.slug = slugify(self.function_name)
			super(Package, self).save()

	class Meta:
		db_table = "Package"

	def __str__(self):
		return "{0}".format(self.function_name)


class Events(models.Model):
	package = models.ForeignKey(Package, on_delete=models.CASCADE)
	event_name = models.CharField(max_length=100)
	images = models.ImageField(null=True, upload_to='event_images/')
	slug =  models.SlugField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	class Meta:
		db_table = "Events"
		verbose_name= "Events"

	def save(self, *args, **kwargs):
		super(Events, self).save(*args, **kwargs)
		if self.event_name:
			self.slug = slugify(self.event_name)
			super(Events, self).save()


	def __str__(self):
		return "{0}".format(self.event_name)


class Equipment(models.Model):
	package = models.ForeignKey(Package, on_delete=models.CASCADE)
	event = models.ForeignKey(Events, on_delete=models.CASCADE)
	equipment_name = models.TextField(null=False)
	equipment_model = models.TextField(null=False)
	images = models.ImageField(null=True, upload_to='equipment_images/')
	slug = models.SlugField(max_length=255,null=True)
	album_detail = models.TextField(null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)


	class Meta:
		db_table = "Equipment"
		verbose_name= "Equipment"

	def save(self, *args, **kwargs):
		super(Equipment, self).save(*args, **kwargs)
		if self.equipment_name:
			self.slug = slugify(self.equipment_name)
			super(Equipment, self).save()

	def __str__(self):
		return "{0}".format(self.equipment_name)


class PriceList(models.Model):
	user = models.ForeignKey(AddUser, on_delete=models.CASCADE)
	package = models.ForeignKey(Package, on_delete=models.CASCADE)
	event = models.ForeignKey(Events, on_delete=models.CASCADE)
	equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=255,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(PriceList, self).save(*args, **kwargs)
		if self.package:
			self.slug = slugify(self.package)
			super(PriceList, self).save()

class Post(models.Model):
	user = models.ForeignKey(AddUser, on_delete=models.CASCADE)
	category = models.CharField(max_length=200)
	video_url = models.URLField(max_length=300, null=True)
	short_description = models.TextField(null=True)
	detail_description = models.TextField(null=True)
	image = models.ImageField(null=False, upload_to="admin_post_img/")
	slug = models.SlugField(max_length=255,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(Post, self).save(*args, **kwargs)
		if self.category:
			self.slug = slugify(self.category)
			super(Post, self).save()

	class Meta:
		db_table = "Post"
		verbose_name= "Post"

	def __str__(self):
		return "{0}".format(self.category)

class Gallery(models.Model):
	user = models.ForeignKey(AddUser, on_delete=models.CASCADE)
	category = models.CharField(null=False, max_length=255)
	slug = models.SlugField(max_length=255,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	def save(self, *args, **kwargs):
		super(Gallery, self).save(*args, **kwargs)
		if self.category:
			self.slug = slugify(self.category)
			super(Gallery, self).save()

	class Meta:
		db_table = "Gallery"
		verbose_name= "Gallery"

class Photos(models.Model):
	gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
	images = models.FileField(null=False, upload_to="gallery_images/")
	category = models.CharField(null=False, max_length=255)
	slug = models.SlugField(max_length=255,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)


	def save(self, *args, **kwargs):
		super(Photos, self).save(*args, **kwargs)
		if self.category:
			self.slug = slugify(self.category)
			super(Photos, self).save()

	class Meta:
		db_table = "Photos"
		verbose_name= "Photos"


class Banner(models.Model):
	banner_video = models.URLField(null=True, max_length=252, blank=True)
	banner_category = models.CharField(max_length=200)
	banner_image = models.ImageField(null=False, upload_to="blog_images/")
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)

	datamode = models.CharField(max_length=257, default='Active', choices=ch.DATAMODE_CHOICES)

	class Meta:
		db_table = "banner_model"

	def __str__(self):
		return "{0}".format(self.banner_category)

class AboutUs(models.Model):
	company_name = models.CharField(null=True,max_length=200)
	company_detail = models.TextField(null=True)
	about_you = models.TextField(null=True)
	image = models.ImageField(null=True, upload_to="about_us/")
	contact_name=models.CharField(null=True,max_length=200)
	contact_no= models.CharField(null=True, max_length=10)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)
	
	class Meta:
		db_table = "about_us"

class ImageDuplicate(models.Model):
	image_name = models.CharField(null=True, max_length=255)
	image_url = models.CharField(null=True, max_length=255)
	data_from = models.CharField(null=False, max_length=255)
	data_from_id = models.CharField(null=False, max_length=255)
	image_signature = models.CharField(null=False, max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "ImageDuplicate"
		verbose_name="ImageDuplicate"

class Profile(models.Model):
	email = models.EmailField(null=True, blank=True,max_length=255)
	username = models.CharField(null=True, blank=True,max_length=255)
	profile_pic = models.FileField(null=True, upload_to="profile_images/")
	phone_no = models.IntegerField(null=True,default=0)
	address = models.TextField(null=True)
	city= models.CharField(null=True, blank=True,max_length=255)
	state = models.CharField(null=True, blank=True,max_length=255)
	country = models.CharField(null=True, blank=True,max_length=255)
	pincode= models.IntegerField(null=True,default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	created_by = models.CharField(null=True, max_length=255)
	updated_by = models.CharField(null=True, max_length=255)
	updated_on = models.DateTimeField(auto_now=True)


	class Meta:
		db_table = "Profile"
		verbose_name="Profile"
		
	def __str__(self):
		return "{0}".format(self.email)		
