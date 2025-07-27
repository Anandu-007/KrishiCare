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
    return render(request, 'RegisterFarmer.html')

def admin_dashboard(request):
    return render(request, 'admin_home.html')

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
    # Simple view that just renders the template with sample data
    return render(request, 'ViewFarmers.html')

def view_users(request):
    users = [
        {'name': 'Amit Sharma', 'phone': '9876543211', 'address': 'City X'},
        {'name': 'Priya Singh', 'phone': '9123456789', 'address': 'City Y'},
        {'name': 'Rahul Verma', 'phone': '9988776654', 'address': 'City Z'},
    ]
    return render(request, 'ViewUsers.html', {'users': users})

def inventory_seed(request):
    seeds = Product.objects.filter(product_type='seed', is_available=True)
    return render(request, 'InventorySeed.html', {'seeds': seeds})

def inventory_fertilizer(request):
    fertilizers = Product.objects.filter(product_type='fertilizer', is_available=True)
    return render(request, 'InventoryFertilizer.html', {'fertilizers': fertilizers})

def inventory_tool(request):
    tools = Product.objects.filter(product_type='tool', is_available=True)
    return render(request, 'InventoryTool.html', {'tools': tools})

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
    return render(request, 'SchemeAdd.html', {'schemes': schemes, 'categories': categories})

def complaints_view(request):
    complaints = [
        {'id': 1, 'submitted_by': 'Ravi Kumar', 'user_type': 'Farmer', 'subject': 'Water Issue', 'message': 'No water supply for crops.', 'submitted_date': '2024-07-01'},
        {'id': 2, 'submitted_by': 'Amit Sharma', 'user_type': 'User', 'subject': 'Seed Quality', 'message': 'Received poor quality seeds.', 'submitted_date': '2024-07-02'},
    ]
    return render(request, 'ComplaintsView.html', {'complaints': complaints})

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
            'place': 'Village D',
            'phone': '6543210987',
            'farmer_type': 'Organic',
            'registered_date': '2024-12-10'
        },
        {
            'id': 5,
            'name': 'Lakshmi Devi',
            'aadhaar_number': '321098765432',
            'place': 'Village E',
            'phone': '5432109876',
            'farmer_type': 'ST',
            'registered_date': '2024-12-08'
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
    return render(request, 'approve_farmers.html', context)

def farmer_products(request):
    """Display products added by farmers"""
    return render(request, 'farmer_products.html')

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
