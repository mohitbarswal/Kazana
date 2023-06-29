from django.shortcuts import render

# Create your views here.

def home_page_fun(request):
    return render(request, 'Home.html')

def create_subadmin_fun(request):
    return render(request, 'Createsub_admin.html')