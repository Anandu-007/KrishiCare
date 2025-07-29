
from django.urls import path
from .import views

urlpatterns = [
    # Admin URLs (when accessed via /admin/)
    path('', views.admin_dashboard, name='AdminDashboard'),  # /admin/ goes to custom dashboard
    path('dashboard/', views.admin_dashboard, name='AdminDashboard'),
    path('farmers/', views.view_farmers, name='ViewFarmers'),
    path('users/', views.view_users, name='ViewUsers'),
    path('inventory/seed/', views.inventory_seed, name='InventorySeed'),
    path('inventory/fertilizer/', views.inventory_fertilizer, name='InventoryFertilizer'),
    path('inventory/tool/', views.inventory_tool, name='InventoryTool'),
    path('scheme/add/', views.scheme_add, name='SchemeAdd'),
    path('scheme/applications/', views.scheme_applications, name='SchemeApplications'),
    path('complaints/', views.complaints_view, name='ComplaintsView'),
    path('approve-farmers/', views.approve_farmers, name='approve_farmers'),
    path('farmer-products/<int:farmer_id>/', views.farmer_products, name='farmer_products'),

    # Non-admin URLs (when accessed via root /)
    path('home/',views.home,name='home'),
    path('login/',views.login,name='Login'),
    path('register_user/', views.register_user, name='RegisterUser'),
    path('register_farmer/', views.register_farmer, name='RegisterFarmer'),
    
    # Farmers Module URLs
    path('farmers-dashboard/', views.farmers_dashboard, name='farmers_dashboard'),
    path('farmers/plant-detection/', views.plant_detection, name='plant_detection'),
]
