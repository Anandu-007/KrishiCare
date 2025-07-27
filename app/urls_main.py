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
    path('farmers/dashboard/', views.farmers_dashboard, name='farmers_dashboard'),
    path('farmers/category/<str:category_name>/', views.category_products, name='category_products'),
    path('farmers/seeds-marketplace/', views.seeds_marketplace, name='seeds_marketplace'),
    path('farmers/fertilizers-marketplace/', views.fertilizers_marketplace, name='fertilizers_marketplace'),
    path('farmers/tools-marketplace/', views.tools_marketplace, name='tools_marketplace'),
    path('farmers/schemes/', views.farmer_schemes, name='farmer_schemes'),
    path('farmers/schemes/apply/<int:scheme_id>/', views.apply_scheme, name='apply_scheme'),
    path('farmers/plant-detection/', views.plant_detection, name='plant_detection'),
] 