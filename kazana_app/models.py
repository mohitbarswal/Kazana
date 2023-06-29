from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
gender =(('M', 'Male'),
        ('F', 'Female'))
usertype = (('company', 'Company'), ('user', 'User'))
payment_type = (('one', 'One Time'), ('recurring', 'Recurring'))
onetoten = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
             ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))
time_period = (('weeks', 'Weeks'), ('months', 'Months'), ('years', 'Years'))
rate_of_return = (('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), 
                  ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), 
                  ('90%', '90%'), ('100%', '100%'))

class User_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_detail_key")
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    gender = models.CharField(choices=gender, max_length=50, blank=True, null=True)
    amount_invested = models.DecimalField( max_digits=7,decimal_places=2, blank=True, null=True)
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    user_type = models.CharField(choices=usertype, max_length=12, blank=True, null=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    enable_category = models.BooleanField(default=True, blank=True, null=True)

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category_product_key")
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_image = models.FileField(upload_to='images/', blank=True, null=True)
    description = models.TextField(max_length=800, blank=True, null=True)
    minimum_amount_invested = models.DecimalField(max_digits=7,decimal_places=2, blank=True, null=True)
    payment_type = models.CharField(choices=payment_type, max_length=20, blank=True, null=True)
    no_of_payments = models.CharField(choices=onetoten, max_length=20, blank=True, null=True)
    time_period = models.CharField(choices=time_period, max_length=20, blank=True, null=True)
    frequency = models.CharField(choices=onetoten, max_length=20, blank=True, null=True)
    rate_of_return = models.CharField(choices=rate_of_return, max_length=20, blank=True, null=True)
    enable_product = models.BooleanField(default=True, blank=True, null=True)
    product_video = models.FileField(upload_to='videos/', blank=True, null=True)

class Product_images(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, related_name="product_images_key")
    add_images = models.FileField(upload_to='images/', blank=True, null=True)

class Product_documents(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, related_name="product_documents_key")
    add_documents = models.FileField(upload_to='documents/', blank=True, null=True)

class Blog_management(models.Model):
    blog_title =  models.CharField(choices=rate_of_return, max_length=100, blank=True, null=True)
    blog_url = models.URLField(blank=True, null=True)
    blog_image = models.FileField(upload_to='images/', blank=True, null=True)
    blog_description = RichTextField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)

class About_us(models.Model):
    content_title = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

class Contact_us(models.Model):
    username = models.CharField(max_length=20,blank=True, null=True)
    email_address = models.EmailField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

class Upload_document(models.Model):
    document_title = models.CharField(max_length=50, blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    description = models.TextField(max_length=800, blank=True)




