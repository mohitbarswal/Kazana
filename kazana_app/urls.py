from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home_page_fun),
    path('login/', views.login_fun, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    
    path('createsubadmin/', views.create_subadmin_fun, name="createsubadmin"),
    path('updatesubadmin/<int:id>/', views.update_subadmin_fun, name="updatesubadmin"),
    path('deletesubadmin/<int:id>/', views.delete_subadmin_fun, name="deletesubadmin"),

    path('createuser/', views.create_user_fun, name="createuser"),

]