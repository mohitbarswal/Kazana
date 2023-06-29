from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .models import User_Detail, Category, Products, Product_images, Product_documents, Blog_management, About_us, Contact_us, Upload_document



class Sub_adminform(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=10)
    first_name = forms.CharField(label='First Name', min_length=3, max_length=10)
    last_name = forms.CharField(label='Last Name', min_length=3, max_length=10)
    email = forms.EmailField(label='Email Address') 
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    phone_no = forms.IntegerField(label='Phone number')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_no')





# class Bestsellerform(forms.ModelForm):
#     class Meta:
#         model = Bestseller
#         fields = "__all__"