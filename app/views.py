from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Scheme, Product, PlantDetection, Farmer
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'Login.html')

def register(request):
    return render(request, 'Register.html')

def register_user(request):
    return render(request, 'RegisterUser.html')

def register_farmer(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            place = request.POST.get('place')
            address = request.POST.get('address')
            land_size = request.POST.get('land_size')
            farmer_type = request.POST.get('farmer_type')
            aadhaar = request.POST.get('aadhaar')
            approval_status = request.POST.get('approval_status')
            
            # Handle file uploads
            photo = request.FILES.get('photo')
            land_photo = request.FILES.get('land_photo')
            land_tax = request.FILES.get('land_tax')
            id_proof = request.FILES.get('id_proof')
            bank_passbook = request.FILES.get('bank_passbook')
            
            # Convert approval status to boolean
            is_approved = False
            if approval_status == 'approved':
                is_approved = True
            elif approval_status == 'rejected':
                is_approved = False
            else:  # pending
                is_approved = False
            
            # Create Farmer object
            farmer = Farmer.objects.create(
                name=name,
                phone=phone,
                place=place,
                address=address,
                land_size=land_size,
                farmer_type=farmer_type,
                aadhaar_number=aadhaar,
                photo=photo,
                is_approved=is_approved
            )
            
            messages.success(request, f'Farmer {name} registered successfully! Approval status: {approval_status.title()}')
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
    
    return render(request, 'RegisterFarmer.html')

def admin_dashboard(request):
    return render(request, 'admin/admin_home.html')

# Farmers Module Views
def farmers_dashboard(request):
    """Farmers dashboard with main functionality"""
    # For now, we'll use dummy data since we're focusing on UI
    context = {
        'farmer_name': 'John Doe',
        'total_earnings': 2450,
        'active_crops': 12,
        'available_schemes': 8,
        'products_listed': 24,
        'plant_detections': 15,
    }
    return render(request, 'farmers/farmers_dashboard.html', context)

def plant_detection(request):
    """Plant detection with image upload"""
    if request.method == 'POST':
        # Handle image upload
        if 'plant_image' in request.FILES:
            image = request.FILES['plant_image']
            notes = request.POST.get('notes', '')
            
            # Create a mock detection result
            detection = PlantDetection.objects.create(
                user=User.objects.first(),  # Use first user as default
                plant_name="Sample Plant",
                image=image,
                confidence_score=85.5,
                health_status="Healthy",
                notes=notes
            )
            messages.success(request, 'Plant detection completed successfully!')
            return redirect('plant_detection')
    
    detections = PlantDetection.objects.all().order_by('-detection_date')[:5]
    return render(request, 'farmers/plant_detection.html', {'detections': detections})

# Admin Views
def view_farmers(request):
    # Sample data for farmers
    farmers = [
        {
            'id': 1,
            'name': 'Rajesh Kumar',
            'aadhaar_number': '123456789012',
            'place': 'Village A, District X',
            'phone': '9876543210',
            'farmer_type': 'Small',
            'land_size': 2.5,
            'is_approved': True,
            'registered_date': '2024-12-15',
            'address': 'House No. 123, Village A, District X, State Y'
        },
        {
            'id': 2,
            'name': 'Priya Sharma',
            'aadhaar_number': '987654321098',
            'place': 'Village B, District Y',
            'phone': '8765432109',
            'farmer_type': 'Marginal',
            'land_size': 1.2,
            'is_approved': False,
            'registered_date': '2024-12-14',
            'address': 'House No. 456, Village B, District Y, State Z'
        },
        {
            'id': 3,
            'name': 'Suresh Patel',
            'aadhaar_number': '456789012345',
            'place': 'Village C, District Z',
            'phone': '7654321098',
            'farmer_type': 'SC',
            'land_size': 3.0,
            'is_approved': True,
            'registered_date': '2024-12-13',
            'address': 'House No. 789, Village C, District Z, State A'
        },
        {
            'id': 4,
            'name': 'Amit Patel',
            'aadhaar_number': '789012345678',
            'place': 'Village D, District A',
            'phone': '6543210987',
            'farmer_type': 'Organic',
            'land_size': 5.5,
            'is_approved': True,
            'registered_date': '2024-12-10',
            'address': 'House No. 101, Village D, District A, State B'
        },
        {
            'id': 5,
            'name': 'Lakshmi Devi',
            'aadhaar_number': '321098765432',
            'place': 'Village E, District B',
            'phone': '5432109876',
            'farmer_type': 'ST',
            'land_size': 1.8,
            'is_approved': False,
            'registered_date': '2024-12-12',
            'address': 'House No. 202, Village E, District B, State C'
        },
        {
            'id': 6,
            'name': 'Ramesh Singh',
            'aadhaar_number': '654321098765',
            'place': 'Village F, District C',
            'phone': '4321098765',
            'farmer_type': 'Small',
            'land_size': 2.8,
            'is_approved': True,
            'registered_date': '2024-12-11',
            'address': 'House No. 303, Village F, District C, State D'
        }
    ]
    return render(request, 'admin/ViewFarmers.html', {'farmers': farmers})

def view_users(request):
    users = [
        {'name': 'Amit Sharma', 'phone': '9876543211', 'address': 'City X'},
        {'name': 'Priya Singh', 'phone': '9123456789', 'address': 'City Y'},
        {'name': 'Rahul Verma', 'phone': '9988776654', 'address': 'City Z'},
    ]
    return render(request, 'admin/ViewUsers.html', {'users': users})

def inventory_seed(request):
    seeds = Product.objects.filter(product_type='seed', is_available=True)
    return render(request, 'admin/InventorySeed.html', {'seeds': seeds})

def inventory_fertilizer(request):
    fertilizers = Product.objects.filter(product_type='fertilizer', is_available=True)
    return render(request, 'admin/InventoryFertilizer.html', {'fertilizers': fertilizers})

def inventory_tool(request):
    tools = Product.objects.filter(product_type='tool', is_available=True)
    return render(request, 'admin/InventoryTool.html', {'tools': tools})

def scheme_add(request):
    if request.method == 'POST':
        scheme_name = request.POST.get('scheme_name')
        description = request.POST.get('description')
        category_name = request.POST.get('category')
        eligible_crop = request.POST.get('eligible_crop')
        target_region = request.POST.get('target_region')
        application_deadline = request.POST.get('application_deadline')
        
        category, created = Category.objects.get_or_create(name=category_name)
        
        Scheme.objects.create(
            scheme_name=scheme_name,
            description=description,
            category=category,
            eligible_crop=eligible_crop,
            target_region=target_region,
            application_deadline=application_deadline
        )
        
        messages.success(request, 'Scheme added successfully!')
        return redirect('SchemeAdd')
    
    schemes = Scheme.objects.all()
    categories = Category.objects.all()
    return render(request, 'admin/SchemeAdd.html', {'schemes': schemes, 'categories': categories})

def scheme_applications(request):
    """View for managing scheme applications"""
    # Sample data for scheme applications
    applications = [
        {
            'id': 'APP-001',
            'farmer_name': 'Rajesh Kumar',
            'aadhaar': '111222333444',
            'village': 'Village A, District X',
            'scheme_name': 'PM-KISAN',
            'scheme_description': 'Direct income support of ₹6000/year',
            'application_date': 'Dec 15, 2024',
            'application_time': '11:45 AM',
            'status': 'Pending Review',
            'status_badge': 'bg-warning',
            'documents': ['Aadhaar Card', 'Land Records', 'Bank Passbook']
        },
        {
            'id': 'APP-002',
            'farmer_name': 'Sunita Devi',
            'aadhaar': '555666777888',
            'village': 'Village B, District Y',
            'scheme_name': 'Crop Insurance',
            'scheme_description': 'Comprehensive crop insurance',
            'application_date': 'Dec 14, 2024',
            'application_time': '3:20 PM',
            'status': 'Approved',
            'status_badge': 'bg-success',
            'documents': ['Aadhaar Card', 'Land Records', 'Crop Details']
        },
        {
            'id': 'APP-003',
            'farmer_name': 'Amit Singh',
            'aadhaar': '999000111222',
            'village': 'Village C, District Z',
            'scheme_name': 'Fertilizer Subsidy',
            'scheme_description': 'Subsidy on fertilizers for small farmers',
            'application_date': 'Dec 13, 2024',
            'application_time': '10:15 AM',
            'status': 'Rejected',
            'status_badge': 'bg-danger',
            'documents': ['Aadhaar Card', 'Land Records', 'Income Certificate']
        },
        {
            'id': 'APP-004',
            'farmer_name': 'Priya Sharma',
            'aadhaar': '333444555666',
            'village': 'Village D, District W',
            'scheme_name': 'Organic Farming Support',
            'scheme_description': 'Support for organic farming practices',
            'application_date': 'Dec 12, 2024',
            'application_time': '5:30 PM',
            'status': 'Pending Review',
            'status_badge': 'bg-warning',
            'documents': ['Aadhaar Card', 'Land Records', 'Organic Certification']
        }
    ]
    
    context = {
        'applications': applications,
        'total_applications': 45,
        'pending_applications': 18,
        'approved_applications': 22,
        'rejected_applications': 5
    }
    
    return render(request, 'admin/SchemeApplications.html', context)

def complaints_view(request):
    complaints = [
        {
            'id': 1, 
            'submitted_by': 'Ravi Kumar', 
            'user_type': 'Farmer', 
            'subject': 'Water Supply Issue', 
            'message': 'No water supply for crops in our village for the past 3 days. This is affecting our crop growth significantly.', 
            'submitted_date': '2024-12-15',
            'status': 'Pending',
            'priority': 'High',
            'category': 'Infrastructure'
        },
        {
            'id': 2, 
            'submitted_by': 'Amit Sharma', 
            'user_type': 'User', 
            'subject': 'Poor Seed Quality', 
            'message': 'Received poor quality seeds from the marketplace. Seeds are not germinating properly.', 
            'submitted_date': '2024-12-14',
            'status': 'In Progress',
            'priority': 'Medium',
            'category': 'Product Quality'
        },
        {
            'id': 3, 
            'submitted_by': 'Priya Patel', 
            'user_type': 'Farmer', 
            'subject': 'Fertilizer Delivery Delay', 
            'message': 'Ordered fertilizers 5 days ago but still no delivery. Need urgent delivery for crop season.', 
            'submitted_date': '2024-12-13',
            'status': 'Resolved',
            'priority': 'High',
            'category': 'Delivery'
        },
        {
            'id': 4, 
            'submitted_by': 'Suresh Verma', 
            'user_type': 'User', 
            'subject': 'App Login Problem', 
            'message': 'Unable to login to the mobile app. Getting error message every time I try.', 
            'submitted_date': '2024-12-12',
            'status': 'Pending',
            'priority': 'Low',
            'category': 'Technical'
        },
        {
            'id': 5, 
            'submitted_by': 'Lakshmi Devi', 
            'user_type': 'Farmer', 
            'subject': 'Scheme Application Rejected', 
            'message': 'My scheme application was rejected without proper reason. Need clarification on rejection criteria.', 
            'submitted_date': '2024-12-11',
            'status': 'In Progress',
            'priority': 'Medium',
            'category': 'Schemes'
        },
        {
            'id': 6, 
            'submitted_by': 'Rajesh Singh', 
            'user_type': 'User', 
            'subject': 'Payment Gateway Issue', 
            'message': 'Payment is not going through when trying to purchase products. Getting transaction failed error.', 
            'submitted_date': '2024-12-10',
            'status': 'Resolved',
            'priority': 'High',
            'category': 'Payment'
        },
        {
            'id': 7, 
            'submitted_by': 'Meera Reddy', 
            'user_type': 'Farmer', 
            'subject': 'Tool Rental Service', 
            'message': 'Requesting tool rental service for harvesting equipment. Currently not available in our area.', 
            'submitted_date': '2024-12-09',
            'status': 'Pending',
            'priority': 'Medium',
            'category': 'Services'
        },
        {
            'id': 8, 
            'submitted_by': 'Vikram Gupta', 
            'user_type': 'User', 
            'subject': 'Weather Information Not Updated', 
            'message': 'Weather information on the platform is not updated for the past week. Need current weather data.', 
            'submitted_date': '2024-12-08',
            'status': 'Resolved',
            'priority': 'Low',
            'category': 'Information'
        }
    ]
    return render(request, 'admin/ComplaintsView.html', {'complaints': complaints})

def approve_farmers(request):
    """View to approve/reject farmers with dummy data"""
    # Dummy data for demonstration
    pending_farmers = [
        {
            'id': 1,
            'name': 'Rajesh Kumar',
            'aadhaar_number': '123456789012',
            'place': 'Village A',
            'phone': '9876543210',
            'farmer_type': 'Small',
            'registered_date': '2024-12-15'
        },
        {
            'id': 2,
            'name': 'Priya Sharma',
            'aadhaar_number': '987654321098',
            'place': 'Village B',
            'phone': '8765432109',
            'farmer_type': 'Marginal',
            'registered_date': '2024-12-14'
        },
        {
            'id': 3,
            'name': 'Suresh Patel',
            'aadhaar_number': '456789012345',
            'place': 'Village C',
            'phone': '7654321098',
            'farmer_type': 'SC',
            'registered_date': '2024-12-13'
        }
    ]
    
    approved_farmers = [
        {
            'id': 4,
            'name': 'Amit Patel',
            'aadhaar_number': '789012345678',
            'place': 'Village D, District A',
            'phone': '6543210987',
            'farmer_type': 'Organic',
            'registered_date': '2024-12-10'
        },
        {
            'id': 5,
            'name': 'Lakshmi Devi',
            'aadhaar_number': '321098765432',
            'place': 'Village E, District B',
            'phone': '5432109876',
            'farmer_type': 'ST',
            'registered_date': '2024-12-08'
        },
        {
            'id': 6,
            'name': 'Ramesh Singh',
            'aadhaar_number': '654321098765',
            'place': 'Village F, District C',
            'phone': '4321098765',
            'farmer_type': 'Small',
            'registered_date': '2024-12-11'
        },
        {
            'id': 7,
            'name': 'Sunita Verma',
            'aadhaar_number': '987654321012',
            'place': 'Village G, District D',
            'phone': '3210987654',
            'farmer_type': 'Marginal',
            'registered_date': '2024-12-09'
        },
        {
            'id': 8,
            'name': 'Vikram Malhotra',
            'aadhaar_number': '456789012345',
            'place': 'Village H, District E',
            'phone': '2109876543',
            'farmer_type': 'SC',
            'registered_date': '2024-12-07'
        },
        {
            'id': 9,
            'name': 'Geeta Sharma',
            'aadhaar_number': '123456789012',
            'place': 'Village I, District F',
            'phone': '1098765432',
            'farmer_type': 'Organic',
            'registered_date': '2024-12-06'
        },
        {
            'id': 10,
            'name': 'Harish Kumar',
            'aadhaar_number': '234567890123',
            'place': 'Village J, District G',
            'phone': '0987654321',
            'farmer_type': 'Small',
            'registered_date': '2024-12-05'
        },
        {
            'id': 11,
            'name': 'Meera Reddy',
            'aadhaar_number': '345678901234',
            'place': 'Village K, District H',
            'phone': '9876543210',
            'farmer_type': 'Marginal',
            'registered_date': '2024-12-04'
        },
        {
            'id': 12,
            'name': 'Prakash Gupta',
            'aadhaar_number': '456789012345',
            'place': 'Village L, District I',
            'phone': '8765432109',
            'farmer_type': 'ST',
            'registered_date': '2024-12-03'
        }
    ]
    
    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')
        action = request.POST.get('action')
        
        if farmer_id and action:
            # Simulate approval/rejection
            if action == 'approve':
                messages.success(request, f'Farmer has been approved successfully!')
            elif action == 'reject':
                messages.warning(request, f'Farmer has been rejected.')
    
    context = {
        'pending_farmers': pending_farmers,
        'approved_farmers': approved_farmers,
    }
    return render(request, 'admin/approve_farmers.html', context)

def farmer_products(request, farmer_id):
    """Display products sold by a specific farmer"""
    # Sample farmer data (this will be replaced with database query later)
    farmer = {
        'id': farmer_id,
        'name': 'Rajesh Kumar',
        'place': 'Village A, District X',
        'aadhaar_number': '123456789012',
        'phone': '9876543210',
        'farmer_type': 'Small',
        'land_size': 2.5,
        'is_approved': True,
        'registered_date': '2024-12-15'
    }
    
    # Sample product statistics
    total_products = 3
    total_sales = 50
    total_revenue = 12500
    active_products = 2
    seed_products = 1
    fertilizer_products = 1
    tool_products = 1
    avg_rating = 4.4
    
    context = {
        'farmer': farmer,
        'total_products': total_products,
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'active_products': active_products,
        'seed_products': seed_products,
        'fertilizer_products': fertilizer_products,
        'tool_products': tool_products,
        'avg_rating': avg_rating,
    }
    
    return render(request, 'admin/FarmerProducts.html', context)

def category_products(request, category_name):
    """Display and manage products for a specific category"""
    # Dummy data for demonstration
    products = [
        {
            'id': 1,
            'product_name': 'Fresh Tomatoes',
            'description': 'Organic red tomatoes, freshly harvested from our farm',
            'price': 45.00,
            'quantity': 25,
            'image': None,
            'created_date': 'Dec 15, 2024'
        },
        {
            'id': 2,
            'product_name': 'Green Peas',
            'description': 'Sweet green peas, perfect for cooking',
            'price': 60.00,
            'quantity': 15,
            'image': None,
            'created_date': 'Dec 14, 2024'
        },
        {
            'id': 3,
            'product_name': 'Carrots',
            'description': 'Fresh orange carrots, rich in vitamins',
            'price': 35.00,
            'quantity': 8,
            'image': None,
            'created_date': 'Dec 13, 2024'
        }
    ]
    
    # Calculate statistics
    total_products = len(products)
    total_value = sum(product['price'] * product['quantity'] for product in products)
    in_stock = len([p for p in products if p['quantity'] > 10])
    low_stock = len([p for p in products if 0 < p['quantity'] <= 10])
    
    context = {
        'category_name': category_name.title(),
        'products': products,
        'total_products': total_products,
        'total_value': total_value,
        'in_stock': in_stock,
        'low_stock': low_stock,
    }
    return render(request, 'farmers/category_products.html', context)

def seeds_marketplace(request):
    """Display seeds marketplace for farmers to buy from Krishi Bhavan"""
    # Dummy data for demonstration
    seeds = [
        {
            'id': 1,
            'name': 'Hybrid Tomato Seeds',
            'description': 'High-yielding hybrid tomato seeds. Disease-resistant, suitable for all seasons.',
            'price': 45.00,
            'quantity': 500,
            'rating': 4.9,
            'stock_status': 'In Stock',
            'germination_rate': '95%',
            'image': 'tomato-seeds.jpg'
        },
        {
            'id': 2,
            'name': 'Green Chilli Seeds',
            'description': 'Spicy green chilli seeds. High heat tolerance, suitable for hot climates.',
            'price': 35.00,
            'quantity': 300,
            'rating': 4.2,
            'stock_status': 'In Stock',
            'germination_rate': '92%',
            'image': 'chilli-seeds.jpg'
        },
        {
            'id': 3,
            'name': 'Lady Finger Seeds',
            'description': 'High-yielding okra seeds. Drought-resistant, perfect for summer cultivation.',
            'price': 40.00,
            'quantity': 400,
            'rating': 4.8,
            'stock_status': 'Low Stock',
            'germination_rate': '90%',
            'image': 'okra-seeds.jpg'
        },
        {
            'id': 4,
            'name': 'Orange Carrot Seeds',
            'description': 'Sweet orange carrot seeds. Rich in vitamins, suitable for winter cultivation.',
            'price': 50.00,
            'quantity': 600,
            'rating': 4.7,
            'stock_status': 'In Stock',
            'germination_rate': '88%',
            'image': 'carrot-seeds.jpg'
        },
        {
            'id': 5,
            'name': 'Spinach Seeds',
            'description': 'Iron-rich spinach seeds. Fast-growing, perfect for leafy greens.',
            'price': 30.00,
            'quantity': 800,
            'rating': 4.1,
            'stock_status': 'In Stock',
            'germination_rate': '85%',
            'image': 'spinach-seeds.jpg'
        },
        {
            'id': 6,
            'name': 'Red Onion Seeds',
            'description': 'High-quality red onion seeds. Long storage life, disease-resistant.',
            'price': 55.00,
            'quantity': 0,
            'rating': 4.9,
            'stock_status': 'Out of Stock',
            'germination_rate': '87%',
            'image': 'onion-seeds.jpg'
        }
    ]
    
    context = {
        'seeds': seeds,
        'total_products': len(seeds),
        'in_stock': len([s for s in seeds if s['stock_status'] == 'In Stock']),
        'low_stock': len([s for s in seeds if s['stock_status'] == 'Low Stock']),
        'out_of_stock': len([s for s in seeds if s['stock_status'] == 'Out of Stock']),
    }
    return render(request, 'farmers/seeds_marketplace.html', context)

def fertilizers_marketplace(request):
    """Display fertilizers marketplace for farmers to buy from Krishi Bhavan"""
    # Dummy data for demonstration
    fertilizers = [
        {
            'id': 1,
            'name': 'NPK 20-20-20',
            'description': 'Balanced NPK fertilizer for all crops. Promotes healthy growth, flowering, and fruiting.',
            'price': 450.00,
            'quantity': 25,
            'rating': 4.8,
            'stock_status': 'In Stock',
            'type': 'NPK',
            'image': 'npk-fertilizer.jpg'
        },
        {
            'id': 2,
            'name': 'Organic Farm Manure',
            'description': 'Pure organic manure from cow dung. Improves soil structure and fertility.',
            'price': 180.00,
            'quantity': 50,
            'rating': 4.3,
            'stock_status': 'In Stock',
            'type': 'Organic',
            'image': 'organic-manure.jpg'
        },
        {
            'id': 3,
            'name': 'Urea 46-0-0',
            'description': 'High nitrogen fertilizer for leafy growth. Essential for vegetative development.',
            'price': 300.00,
            'quantity': 50,
            'rating': 4.7,
            'stock_status': 'Low Stock',
            'type': 'NPK',
            'image': 'urea-fertilizer.jpg'
        },
        {
            'id': 4,
            'name': 'DAP 18-46-0',
            'description': 'High phosphorus fertilizer for root development and flowering.',
            'price': 1200.00,
            'quantity': 50,
            'rating': 4.9,
            'stock_status': 'In Stock',
            'type': 'NPK',
            'image': 'dap-fertilizer.jpg'
        },
        {
            'id': 5,
            'name': 'Azotobacter Bio Fertilizer',
            'description': 'Nitrogen-fixing bio fertilizer. Reduces chemical fertilizer requirement.',
            'price': 80.00,
            'quantity': 1,
            'rating': 4.2,
            'stock_status': 'In Stock',
            'type': 'Bio Fertilizers',
            'image': 'bio-fertilizer.jpg'
        },
        {
            'id': 6,
            'name': 'Micronutrient Mix',
            'description': 'Complete micronutrient package. Contains Zinc, Iron, Manganese, Copper, Boron.',
            'price': 350.00,
            'quantity': 5,
            'rating': 4.8,
            'stock_status': 'Out of Stock',
            'type': 'Micronutrients',
            'image': 'micronutrient-mix.jpg'
        }
    ]
    
    context = {
        'fertilizers': fertilizers,
        'total_products': len(fertilizers),
        'in_stock': len([f for f in fertilizers if f['stock_status'] == 'In Stock']),
        'low_stock': len([f for f in fertilizers if f['stock_status'] == 'Low Stock']),
        'out_of_stock': len([f for f in fertilizers if f['stock_status'] == 'Out of Stock']),
    }
    return render(request, 'farmers/fertilizers_marketplace.html', context)

def tools_marketplace(request):
    """Display tools marketplace for farmers to buy from Krishi Bhavan"""
    # Dummy data for demonstration
    tools = [
        {
            'id': 1,
            'name': 'Heavy Duty Garden Spade',
            'description': 'Professional grade garden spade with wooden handle. Perfect for digging and planting.',
            'price': 850.00,
            'weight': '1.2kg',
            'rating': 4.8,
            'stock_status': 'In Stock',
            'type': 'Hand Tools',
            'image': 'garden-spade.jpg'
        },
        {
            'id': 2,
            'name': 'Plastic Watering Can',
            'description': 'Large capacity watering can with fine rose nozzle. Perfect for garden irrigation.',
            'price': 450.00,
            'capacity': '5L',
            'rating': 4.2,
            'stock_status': 'In Stock',
            'type': 'Irrigation',
            'image': 'watering-can.jpg'
        },
        {
            'id': 3,
            'name': 'Professional Pruning Shears',
            'description': 'High-quality pruning shears for trimming plants and trees.',
            'price': 650.00,
            'weight': '250g',
            'rating': 4.7,
            'stock_status': 'Low Stock',
            'type': 'Garden Tools',
            'image': 'pruning-shears.jpg'
        },
        {
            'id': 4,
            'name': 'Steel Garden Rake',
            'description': 'Heavy-duty steel rake for soil leveling and debris removal.',
            'price': 750.00,
            'weight': '1.5kg',
            'rating': 4.9,
            'stock_status': 'In Stock',
            'type': 'Garden Tools',
            'image': 'garden-rake.jpg'
        },
        {
            'id': 5,
            'name': 'Traditional Garden Hoe',
            'description': 'Classic garden hoe for weeding and soil cultivation.',
            'price': 550.00,
            'weight': '1.8kg',
            'rating': 4.1,
            'stock_status': 'In Stock',
            'type': 'Hand Tools',
            'image': 'garden-hoe.jpg'
        },
        {
            'id': 6,
            'name': 'Traditional Harvesting Sickle',
            'description': 'Traditional curved sickle for harvesting grains and crops.',
            'price': 350.00,
            'weight': '500g',
            'rating': 4.8,
            'stock_status': 'Out of Stock',
            'type': 'Harvesting',
            'image': 'harvesting-sickle.jpg'
        }
    ]
    
    context = {
        'tools': tools,
        'total_products': len(tools),
        'in_stock': len([t for t in tools if t['stock_status'] == 'In Stock']),
        'low_stock': len([t for t in tools if t['stock_status'] == 'Low Stock']),
        'out_of_stock': len([t for t in tools if t['stock_status'] == 'Out of Stock']),
    }
    return render(request, 'farmers/tools_marketplace.html', context)

def farmer_schemes(request):
    """Display government schemes for farmers"""
    # Dummy data for demonstration
    schemes = [
        {
            'id': 1,
            'scheme_name': 'PM-KISAN Scheme',
            'description': 'Direct income support of ₹6,000 per year to eligible farmer families. The amount is transferred in three equal installments of ₹2,000 each.',
            'category': 'Subsidy',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2024-12-31',
            'download_link': '/schemes/pm-kisan-form.pdf',
            'status': 'Active',
            'expires_in': 15,
            'benefits': ['₹6,000 annual support', 'Direct bank transfer', 'No repayment required']
        },
        {
            'id': 2,
            'scheme_name': 'PM Fasal Bima Yojana',
            'description': 'Crop insurance scheme to protect farmers against natural calamities. Covers yield losses due to non-preventable risks.',
            'category': 'Insurance',
            'eligible_crop': 'Food & Oilseeds',
            'target_region': 'All India',
            'application_deadline': '2025-03-15',
            'download_link': '/schemes/fasal-bima-form.pdf',
            'status': 'Active',
            'expires_in': 90,
            'benefits': ['90% premium subsidy', 'Comprehensive coverage', 'Quick claim settlement']
        },
        {
            'id': 3,
            'scheme_name': 'Kisan Credit Card',
            'description': 'Easy credit access for farmers to meet agricultural needs. Includes crop loans, term loans, and working capital.',
            'category': 'Loan',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2025-01-15',
            'download_link': '/schemes/kisan-credit-form.pdf',
            'status': 'Active',
            'expires_in': 30,
            'benefits': ['Up to ₹3 lakh limit', 'Low interest rates', 'Flexible repayment']
        },
        {
            'id': 4,
            'scheme_name': 'PM-KUSUM Scheme',
            'description': 'Solar power scheme for farmers. Install solar pumps and grid-connected solar power plants for irrigation and additional income.',
            'category': 'Technology',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2025-06-30',
            'download_link': '/schemes/pm-kusum-form.pdf',
            'status': 'Active',
            'expires_in': 180,
            'benefits': ['60% subsidy on solar pumps', '30% subsidy on solar plants', 'Additional income from power sale']
        },
        {
            'id': 5,
            'scheme_name': 'Farmer Training Program',
            'description': 'Free training programs on modern farming techniques, organic farming, and digital agriculture. Includes certification and practical sessions.',
            'category': 'Training',
            'eligible_crop': 'All Crops',
            'target_region': 'Kerala',
            'application_deadline': '2025-01-30',
            'download_link': '/schemes/training-form.pdf',
            'status': 'Active',
            'expires_in': 45,
            'benefits': ['Free training programs', 'Certification provided', 'Travel allowance included']
        },
        {
            'id': 6,
            'scheme_name': 'Warehouse Infrastructure',
            'description': 'Subsidy for construction of warehouses and cold storage facilities. Helps farmers store produce and avoid distress sales.',
            'category': 'Infrastructure',
            'eligible_crop': 'Grains & Vegetables',
            'target_region': 'All India',
            'application_deadline': '2025-12-31',
            'download_link': '/schemes/warehouse-form.pdf',
            'status': 'Active',
            'expires_in': 365,
            'benefits': ['50% subsidy on construction', 'Technical support provided', 'Quality certification']
        }
    ]
    
    context = {
        'schemes': schemes,
        'total_schemes': len(schemes),
        'active_schemes': len([s for s in schemes if s['status'] == 'Active']),
        'expiring_soon': len([s for s in schemes if s['expires_in'] <= 30]),
        'categories': ['Subsidy', 'Loan', 'Insurance', 'Training', 'Equipment', 'Infrastructure', 'Technology', 'Marketing']
    }
    return render(request, 'farmers/schemes.html', context)

def apply_scheme(request, scheme_id):
    """Handle scheme application submission"""
    if request.method == 'POST':
        # In a real application, this would process the application form
        # For now, we'll just show a success message
        messages.success(request, f'Application submitted successfully for scheme ID {scheme_id}!')
        return redirect('farmer_schemes')
    
    # For GET requests, redirect back to schemes page
    return redirect('farmer_schemes')

def users_dashboard(request):
    """Users dashboard with main functionality"""
    # For now, we'll use dummy data since we're focusing on UI
    context = {
        'user_name': 'John Doe',
        'user_id': '12345',
        'applied_schemes': 5,
        'orders_placed': 12,
        'active_complaints': 3,
        'resolved_issues': 8,
    }
    return render(request, 'users/users_dashboard.html', context)

def users_schemes(request):
    """Display government schemes for users"""
    # Dummy data for demonstration
    schemes = [
        {
            'id': 1,
            'scheme_name': 'PM-KISAN Scheme',
            'description': 'Direct income support of ₹6,000 per year to eligible farmer families. The amount is transferred in three equal installments of ₹2,000 each.',
            'category': 'Subsidy',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2024-12-31',
            'download_link': '/schemes/pm-kisan-form.pdf',
            'status': 'Active',
            'expires_in': 15,
            'benefits': ['₹6,000 annual support', 'Direct bank transfer', 'No repayment required']
        },
        {
            'id': 2,
            'scheme_name': 'PM Fasal Bima Yojana',
            'description': 'Crop insurance scheme to protect farmers against natural calamities. Covers yield losses due to non-preventable risks.',
            'category': 'Insurance',
            'eligible_crop': 'Food & Oilseeds',
            'target_region': 'All India',
            'application_deadline': '2025-03-15',
            'download_link': '/schemes/fasal-bima-form.pdf',
            'status': 'Active',
            'expires_in': 90,
            'benefits': ['90% premium subsidy', 'Comprehensive coverage', 'Quick claim settlement']
        },
        {
            'id': 3,
            'scheme_name': 'Kisan Credit Card',
            'description': 'Easy credit access for farmers to meet agricultural needs. Includes crop loans, term loans, and working capital.',
            'category': 'Loan',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2025-01-15',
            'download_link': '/schemes/kisan-credit-form.pdf',
            'status': 'Active',
            'expires_in': 30,
            'benefits': ['Up to ₹3 lakh limit', 'Low interest rates', 'Flexible repayment']
        },
        {
            'id': 4,
            'scheme_name': 'PM-KUSUM Scheme',
            'description': 'Solar power scheme for farmers. Install solar pumps and grid-connected solar power plants for irrigation and additional income.',
            'category': 'Technology',
            'eligible_crop': 'All Crops',
            'target_region': 'All India',
            'application_deadline': '2025-06-30',
            'download_link': '/schemes/pm-kusum-form.pdf',
            'status': 'Active',
            'expires_in': 180,
            'benefits': ['60% subsidy on solar pumps', '30% subsidy on solar plants', 'Additional income from power sale']
        },
        {
            'id': 5,
            'scheme_name': 'Farmer Training Program',
            'description': 'Free training programs on modern farming techniques, organic farming, and digital agriculture. Includes certification and practical sessions.',
            'category': 'Training',
            'eligible_crop': 'All Crops',
            'target_region': 'Kerala',
            'application_deadline': '2025-01-30',
            'download_link': '/schemes/training-form.pdf',
            'status': 'Active',
            'expires_in': 45,
            'benefits': ['Free training programs', 'Certification provided', 'Travel allowance included']
        },
        {
            'id': 6,
            'scheme_name': 'Warehouse Infrastructure',
            'description': 'Subsidy for construction of warehouses and cold storage facilities. Helps farmers store produce and avoid distress sales.',
            'category': 'Infrastructure',
            'eligible_crop': 'Grains & Vegetables',
            'target_region': 'All India',
            'application_deadline': '2025-12-31',
            'download_link': '/schemes/warehouse-form.pdf',
            'status': 'Active',
            'expires_in': 365,
            'benefits': ['50% subsidy on construction', 'Technical support provided', 'Quality certification']
        }
    ]
    
    context = {
        'schemes': schemes,
        'total_schemes': len(schemes),
        'active_schemes': len([s for s in schemes if s['status'] == 'Active']),
        'expiring_soon': len([s for s in schemes if s['expires_in'] <= 30]),
        'categories': ['Subsidy', 'Loan', 'Insurance', 'Training', 'Equipment', 'Infrastructure', 'Technology', 'Marketing']
    }
    return render(request, 'users/users_schemes.html', context)

def users_products(request):
    """Display all products added by farmers for users to browse and buy"""
    # Get all available products from the database
    products = Product.objects.filter(is_available=True).order_by('-created_at')
    
    # Get unique categories for filtering
    categories = Category.objects.all()
    
    # Get product type counts for statistics
    seeds_count = products.filter(product_type='seed').count()
    fertilizers_count = products.filter(product_type='fertilizer').count()
    tools_count = products.filter(product_type='tool').count()
    
    # Calculate total value
    total_value = sum(product.price * product.stock_quantity for product in products)
    
    # Get stock statistics
    in_stock = products.filter(stock_quantity__gt=10).count()
    low_stock = products.filter(stock_quantity__gt=0, stock_quantity__lte=10).count()
    out_of_stock = products.filter(stock_quantity=0).count()
    
    context = {
        'products': products,
        'categories': categories,
        'total_products': products.count(),
        'total_value': total_value,
        'seeds_count': seeds_count,
        'fertilizers_count': fertilizers_count,
        'tools_count': tools_count,
        'in_stock': in_stock,
        'low_stock': low_stock,
        'out_of_stock': out_of_stock,
    }
    return render(request, 'users/users_products.html', context)

def users_complaints_view(request):
    """Display user complaints and allow them to view replies"""
    # Sample complaints data for demonstration
    complaints = [
        {
            'id': 1,
            'subject': 'Product Quality Issue',
            'description': 'The wheat seeds I purchased were not germinating properly. Need assistance.',
            'type': 'Product Issue',
            'priority': 'High',
            'status': 'Open',
            'submitted_date': '2024-01-15',
            'replies': [
                {
                    'from': 'Support Team',
                    'message': 'We have received your complaint and are investigating the issue. Our team will contact you within 24 hours.',
                    'date': '2024-01-15'
                }
            ]
        },
        {
            'id': 2,
            'subject': 'Delivery Delay',
            'description': 'My order was supposed to be delivered on 10th January but still not received.',
            'type': 'Delivery Issue',
            'priority': 'Medium',
            'status': 'In Progress',
            'submitted_date': '2024-01-10',
            'replies': [
                {
                    'from': 'Support Team',
                    'message': 'We apologize for the delay. Your order is now in transit and will be delivered by tomorrow.',
                    'date': '2024-01-12'
                },
                {
                    'from': 'User',
                    'message': 'Thank you for the update. Looking forward to receiving my order.',
                    'date': '2024-01-12'
                }
            ]
        },
        {
            'id': 3,
            'subject': 'Website Navigation Issue',
            'description': 'Having trouble finding specific products in the marketplace. The search function is not working properly.',
            'type': 'Technical Issue',
            'priority': 'Low',
            'status': 'Resolved',
            'submitted_date': '2024-01-05',
            'replies': [
                {
                    'from': 'Support Team',
                    'message': 'We have identified and fixed the search functionality issue. Please try again and let us know if you face any problems.',
                    'date': '2024-01-07'
                },
                {
                    'from': 'User',
                    'message': 'The search is working perfectly now. Thank you for the quick resolution!',
                    'date': '2024-01-08'
                }
            ]
        }
    ]
    
    context = {
        'complaints': complaints,
        'total_complaints': len(complaints),
        'open_complaints': len([c for c in complaints if c['status'] == 'Open']),
        'resolved_complaints': len([c for c in complaints if c['status'] == 'Resolved']),
    }
    return render(request, 'users/users_complaints.html', context)

def users_feedback(request):
    """Allow users to submit new complaints and feedback"""
    if request.method == 'POST':
        # Handle form submission
        complaint_type = request.POST.get('complaint_type')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        
        # In a real application, you would save this to the database
        messages.success(request, 'Your complaint has been submitted successfully! We will get back to you soon.')
        return redirect('users_feedback')
    
    context = {
        'complaint_types': ['Product Issue', 'Delivery Issue', 'Payment Issue', 'Technical Issue', 'General Feedback'],
        'priority_levels': ['Low', 'Medium', 'High', 'Urgent']
    }
    return render(request, 'users/users_feedback.html', context)

def users_new_complaint(request):
    """Allow users to submit new complaints"""
    if request.method == 'POST':
        # Handle form submission
        complaint_type = request.POST.get('complaint_type')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        
        # In a real application, you would save this to the database
        messages.success(request, 'Your complaint has been submitted successfully! We will get back to you soon.')
        return redirect('users_complaints_view')
    
    context = {
        'complaint_types': ['Product Issue', 'Delivery Issue', 'Payment Issue', 'Technical Issue', 'General Feedback'],
        'priority_levels': ['Low', 'Medium', 'High', 'Urgent']
    }
    return render(request, 'users/users_new_complaint.html', context)

def users_plant_detection(request):
    """Plant detection functionality for users"""
    if request.method == 'POST':
        # Handle image upload
        if 'plant_image' in request.FILES:
            image = request.FILES['plant_image']
            notes = request.POST.get('notes', '')
            
            # Create a mock detection result
            detection = PlantDetection.objects.create(
                user=User.objects.first(),  # Use first user as default
                plant_name="Sample Plant",
                image=image,
                confidence_score=85.5,
                health_status="Healthy",
                notes=notes
            )
            messages.success(request, 'Plant detection completed successfully!')
            return redirect('users_plant_detection')
    
    detections = PlantDetection.objects.all().order_by('-detection_date')[:5]
    return render(request, 'users/users_plant_detection.html', {'detections': detections})
