from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page_fun),
    path('createsubadmin/', views.create_subadmin_fun, name="createsubadmin"),
    
    
]