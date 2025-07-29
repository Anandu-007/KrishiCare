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
    
    # Users Module URLs
    path('users/', views.users_dashboard, name='users_dashboard'),
    path('users/dashboard/', views.users_dashboard, name='users_dashboard'),
    path('users/schemes/', views.users_schemes, name='users_schemes'),
    path('users/products/', views.users_products, name='users_products'),
    path('users/complaints/view-reply/', views.users_complaints_view, name='users_complaints_view'),
    path('users/complaints/feedback/', views.users_feedback, name='users_feedback'),
    path('users/complaints/new/', views.users_new_complaint, name='users_new_complaint'),
    path('users/plant-detection/', views.users_plant_detection, name='users_plant_detection'),
] 