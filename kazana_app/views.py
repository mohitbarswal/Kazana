from django.shortcuts import render

# Create your views here.

def home_page_fun(request):
    return render(request, 'Home.html')