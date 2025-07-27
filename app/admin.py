from django.contrib import admin
from .models import Category, Scheme, Product, PlantDetection, Farmer

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = ('scheme_name', 'category', 'eligible_crop', 'target_region', 'application_deadline', 'is_active')
    list_filter = ('category', 'is_active', 'application_deadline', 'target_region')
    search_fields = ('scheme_name', 'description', 'eligible_crop')
    date_hierarchy = 'application_deadline'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_type', 'category', 'price', 'stock_quantity', 'is_available')
    list_filter = ('product_type', 'category', 'is_available', 'created_at')
    search_fields = ('product_name', 'description')
    list_editable = ('price', 'stock_quantity', 'is_available')

@admin.register(PlantDetection)
class PlantDetectionAdmin(admin.ModelAdmin):
    list_display = ('plant_name', 'user', 'detection_date', 'confidence_score', 'health_status')
    list_filter = ('detection_date', 'health_status', 'confidence_score')
    search_fields = ('plant_name', 'user__username', 'notes')
    date_hierarchy = 'detection_date'

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'aadhaar_number', 'phone', 'place', 'farmer_type', 'is_approved', 'registered_date')
    list_filter = ('farmer_type', 'is_approved', 'registered_date')
    search_fields = ('name', 'aadhaar_number', 'phone', 'place')
    date_hierarchy = 'registered_date'
