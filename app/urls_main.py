from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='Login'),
    path('register_user/', views.register_user, name='RegisterUser'),
    path('register_farmer/', views.register_farmer, name='RegisterFarmer'),
    
    # Farmers Module URLs
    path('farmers/', views.farmers_dashboard, name='farmers_dashboard'),
    path('farmers/plant-detection/', views.plant_detection, name='plant_detection'),
] 