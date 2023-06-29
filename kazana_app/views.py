from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import User_Detail, Category, Products, Product_images, Product_documents, Blog_management, About_us, Contact_us, Upload_document
from .forms import Sub_adminform
# Create your views here.

# ----------------------------------------------------------------------------Login----------------------------------------------------------------------------------
def login_fun(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Hii {user.first_name} you are logged in!')
            return redirect('/')
        else:
            error_message = 'Invalid username or password !!'
            return render(request, 'Login.html', {'error_message': error_message})
    else:
        return render(request, 'Login.html')
    

# ----------------------------------------------------------------------------Home----------------------------------------------------------------------------------
@login_required(login_url='/login/')
def home_page_fun(request):
    return render(request, 'Home.html')


# ----------------------------------------------------------------------------Sub-admin-----------------------------------------------------------------------------
@login_required(login_url='/login/')
def create_subadmin_fun(request):
    if request.method == "POST":
        subadminform = Sub_adminform(request.POST)
        if subadminform.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            print("username", username)
            print("password", password)
            return HttpResponseRedirect(redirect_to='createsubadmin/')
    else:
        subadminform = Sub_adminform()
    return render(request, 'Createsub_admin.html', {'subadminform': subadminform})
