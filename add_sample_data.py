#!/usr/bin/env python
"""
Script to add sample data for the farmers module
Run this after migrations: python add_sample_data.py
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Category, Scheme, Product, Farmer
from django.contrib.auth.models import User

def create_sample_data():
    print("Creating sample data for farmers module...")
    
    # Create categories
    categories_data = [
        {'name': 'Cereals', 'description': 'Grain crops like wheat, rice, corn'},
        {'name': 'Vegetables', 'description': 'Fresh vegetables and greens'},
        {'name': 'Fruits', 'description': 'Fresh fruits and berries'},
        {'name': 'Pulses', 'description': 'Legumes and beans'},
        {'name': 'Oilseeds', 'description': 'Oil-producing crops'},
    ]
    
    categories = []
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        categories.append(category)
        if created:
            print(f"Created category: {category.name}")
    
    # Create schemes
    schemes_data = [
        {
            'scheme_name': 'PM-KISAN',
            'description': 'Direct income support of Rs. 6000 per year to farmers',
            'category': 'Cereals',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2024-12-31'
        },
        {
            'scheme_name': 'Crop Insurance',
            'description': 'Comprehensive crop insurance against natural calamities',
            'category': 'Cereals',
            'eligible_crop': 'Wheat, Rice, Corn',
            'target_region': 'North India',
            'application_deadline': '2024-11-30'
        },
        {
            'scheme_name': 'Fertilizer Subsidy',
            'description': 'Subsidy on fertilizers for small and marginal farmers',
            'category': 'Vegetables',
            'eligible_crop': 'All Vegetables',
            'target_region': 'South India',
            'application_deadline': '2024-10-31'
        }
    ]
    
    for scheme_data in schemes_data:
        category = Category.objects.get(name=scheme_data['category'])
        scheme, created = Scheme.objects.get_or_create(
            scheme_name=scheme_data['scheme_name'],
            defaults={
                'description': scheme_data['description'],
                'category': category,
                'eligible_crop': scheme_data['eligible_crop'],
                'target_region': scheme_data['target_region'],
                'application_deadline': scheme_data['application_deadline']
            }
        )
        if created:
            print(f"Created scheme: {scheme.scheme_name}")
    
    # Create products
    products_data = [
        # Seeds
        {
            'product_name': 'Wheat Seed',
            'product_type': 'seed',
            'description': 'High-yield wheat seed variety',
            'price': 150.00,
            'stock_quantity': 100,
            'category': 'Cereals'
        },
        {
            'product_name': 'Rice Seed',
            'product_type': 'seed',
            'description': 'Premium quality rice seed',
            'price': 200.00,
            'stock_quantity': 80,
            'category': 'Cereals'
        },
        {
            'product_name': 'Tomato Seeds',
            'product_type': 'seed',
            'description': 'Hybrid tomato seeds',
            'price': 50.00,
            'stock_quantity': 150,
            'category': 'Vegetables'
        },
        # Fertilizers
        {
            'product_name': 'Urea',
            'product_type': 'fertilizer',
            'description': 'Nitrogen fertilizer for crops',
            'price': 300.00,
            'stock_quantity': 200,
            'category': 'Cereals'
        },
        {
            'product_name': 'DAP',
            'product_type': 'fertilizer',
            'description': 'Phosphate fertilizer',
            'price': 400.00,
            'stock_quantity': 120,
            'category': 'Cereals'
        },
        {
            'product_name': 'NPK',
            'product_type': 'fertilizer',
            'description': 'Balanced NPK fertilizer',
            'price': 350.00,
            'stock_quantity': 90,
            'category': 'Vegetables'
        },
        # Tools
        {
            'product_name': 'Tractor',
            'product_type': 'tool',
            'description': 'Heavy duty farming tractor',
            'price': 500000.00,
            'stock_quantity': 5,
            'category': 'Cereals'
        },
        {
            'product_name': 'Plough',
            'product_type': 'tool',
            'description': 'Steel plough for tilling',
            'price': 2500.00,
            'stock_quantity': 25,
            'category': 'Cereals'
        },
        {
            'product_name': 'Water Pump',
            'product_type': 'tool',
            'description': 'Electric water pump for irrigation',
            'price': 15000.00,
            'stock_quantity': 15,
            'category': 'Vegetables'
        }
    ]
    
    for product_data in products_data:
        category = Category.objects.get(name=product_data['category'])
        product, created = Product.objects.get_or_create(
            product_name=product_data['product_name'],
            defaults={
                'product_type': product_data['product_type'],
                'description': product_data['description'],
                'price': product_data['price'],
                'stock_quantity': product_data['stock_quantity'],
                'category': category
            }
        )
        if created:
            print(f"Created product: {product.product_name}")
    
    # Create a sample farmer user
    try:
        user = User.objects.create_user(
            username='farmer1',
            email='farmer1@example.com',
            password='farmer123',
            first_name='Ravi',
            last_name='Kumar'
        )
        
        farmer, created = Farmer.objects.get_or_create(
            user=user,
            defaults={
                'phone': '9876543210',
                'address': 'Village A, District B, State C',
                'land_size': 5.5,
                'farmer_type': 'medium'
            }
        )
        if created:
            print(f"Created farmer: {farmer.user.get_full_name()}")
    except:
        print("Farmer user already exists or error creating farmer")
    
    print("\nSample data creation completed!")
    print("You can now access the farmers module at: http://localhost:8000/farmers/")

if __name__ == '__main__':
    create_sample_data() 