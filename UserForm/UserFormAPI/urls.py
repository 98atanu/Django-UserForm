from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_UserForm, name= "home_UserForm"),
    path('delete/<int:pk>/', views.delete_UserForm, name= "delete_UserForm"),   
    path('update/<int:pk>/', views.update_UserForm, name= "update_UserForm"),   
       
]
