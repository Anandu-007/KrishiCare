from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Scheme(models.Model):
    scheme_name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    eligible_crop = models.CharField(max_length=100)
    target_region = models.CharField(max_length=100)
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.scheme_name

class Product(models.Model):
    PRODUCT_TYPES = [
        ('seed', 'Seeds'),
        ('fertilizer', 'Fertilizers'),
        ('tool', 'Tools'),
    ]
    
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product_name} ({self.get_product_type_display()})"

class PlantDetection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=100)
    detection_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='plant_detections/')
    confidence_score = models.FloatField()
    health_status = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.plant_name} - {self.user.username}"

class Farmer(models.Model):
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True, help_text="12-digit Aadhaar number")
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='farmer_photos/', blank=True, null=True)
    farmer_type = models.CharField(max_length=20, choices=[
        ('small', 'Small'),
        ('marginal', 'Marginal'),
        ('sc', 'SC'),
        ('st', 'ST'),
        ('organic', 'Organic'),
    ])
    land_size = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    address = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    registered_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.aadhaar_number}"
