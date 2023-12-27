from django.contrib import admin
from django.urls import path
from investments_app import views



#app_name='investments_app'

urlpatterns = [
    path('home/', views.view_home,name='home'),
    path('add-investment/', views.view_add_new_investment,name='add_investment'),
    path('update-investment/<int:pk>', views.update_investment_view,name='update_investment'),
    path('home/<int:pk>', views.delete_investment_view,name='delete_investment'),
    
]