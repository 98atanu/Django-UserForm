from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_user_form, name= "home_user_form"),
    path('delete/<int:pk>/', views.delete_user_form, name= "delete_user_form"),   
    path('update/<int:pk>/', views.update_user_form, name= "update_user_form"),   
       
]
