from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .models import User_Detail, Category, Products, Product_images, Product_documents, Blog_management, About_us, Contact_us, Upload_document



class UsercreationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=10)
    first_name = forms.CharField(label='First Name', min_length=3, max_length=15)
    last_name = forms.CharField(label='Last Name', min_length=3, max_length=15)
    email = forms.EmailField(label='Email Address')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def clean_username(self):
        username = self.cleaned_data['username']
        if self.instance and self.instance.username == username:
            return username
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with that username already exists !!")
        return username
    
class Sub_adminfrom(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = ('phone_no',)

class User_form(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = '__all__'
        exclude = ('user',)
        widgets = {'gender':forms.RadioSelect(),
                   'user_type':forms.RadioSelect(),
                   'date_of_birth':forms.DateInput(attrs={'type':'date'})}

