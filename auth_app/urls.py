from django.contrib import admin
from django.urls import path
from auth_app import views

# auth_app/urls.py
#app_name = 'auth_app'

urlpatterns = [
    path('login/', views.view_login_user,name='login'),
    path('logout/', views.view_logout_user,name='logout'),
    path('sign-up/', views.view_register_user,name='sign_up'),
    
]