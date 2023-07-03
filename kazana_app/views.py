from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .models import User_Detail, Category, Products, Product_images, Product_documents, Blog_management, About_us, Contact_us, Upload_document
from .forms import UsercreationForm, Sub_adminfrom, User_form
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
# Create Sub Admin
@login_required(login_url='/login/')
def create_subadmin_fun(request):
    if request.method == "POST":
        Usercreation_form = UsercreationForm(request.POST)
        subadminform = Sub_adminfrom(request.POST)
        if Usercreation_form.is_valid() and subadminform.is_valid():
            adminsave = Usercreation_form.save()
            group = Group.objects.get(name="Subadmin")
            adminsave.groups.add(group)
            subadmin = subadminform.save(commit=False)
            subadmin.user = adminsave
            subadmin.save()
            messages.success(request, "Sub Admin Created Successfully")  
            return HttpResponseRedirect(redirect_to='/createsubadmin/')
    else:
        Usercreation_form = UsercreationForm()
        subadminform = Sub_adminfrom()
        Subadmin_details = User.objects.filter(groups__name="Subadmin")
        return render(request, 'Createsub_admin.html', {'subadminform': subadminform, 'Usercreation_form':Usercreation_form, 'Subadmin_details':Subadmin_details})

# Update Sub Admin
@login_required(login_url='/login/')
def update_subadmin_fun(request, id):
    user_instance = User.objects.get(id=id)
    subadmin_instance = User_Detail.objects.get(user=user_instance.id)
    if request.method == "POST":
        Sub_update_form = UsercreationForm(request.POST, instance=user_instance)
        subdetail_update_form = Sub_adminfrom(request.POST, instance=subadmin_instance)
        if Sub_update_form.is_valid() and subdetail_update_form.is_valid():
            Sub_update_form.save()
            subdetail_update_form.save()
            messages.success(request, "Sub admin Updated Successfully")
            return redirect('createsubadmin')
    else:
        Sub_update_form = UsercreationForm(instance=user_instance)
        subdetail_update_form = Sub_adminfrom(instance=subadmin_instance)
    return render(request, 'Update_subadmin.html', {'Sub_update_form': Sub_update_form, 'subdetail_update_form': subdetail_update_form})

# Delete Sub Admin
@login_required(login_url='/login/')
def delete_subadmin_fun(request, id):
    subadmin_instance = User.objects.get(id=id)
    subadmin_instance.delete()
    messages.success(request, "Sub Admin deleted Successfully")
    return HttpResponseRedirect(redirect_to="/createsubadmin/")

# ----------------------------------------------------------------------------Users-----------------------------------------------------------------------------
# Create User
@login_required(login_url='/login/')
def create_user_fun(request):
    if request.method == "POST":
        Usercreation_form = UsercreationForm(request.POST)
        user_detail_form = User_form(request.POST)
        if Usercreation_form.is_valid() and user_detail_form.is_valid():
            usersave = Usercreation_form.save()
            group = Group.objects.get(name="Users")
            usersave.groups.add(group)
            user_detail = user_detail_form.save(commit=False)
            user_detail.user = usersave
            user_detail.save()
            messages.success(request, "Sub Admin Created Successfully")  
            return HttpResponseRedirect(redirect_to='/createuser/')
    else:
        Usercreation_form = UsercreationForm()
        user_detail_form = User_form()
        user_details = User.objects.filter(groups__name="Users")
        return render(request, 'Create_user.html', {'user_detail_form': user_detail_form, 'Usercreation_form':Usercreation_form, 'user_details':user_details})
