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
    """Simple farmers dashboard"""
    categories = Category.objects.all()[:5]
    schemes = Scheme.objects.filter(is_active=True)[:3]
    products = Product.objects.filter(is_available=True)[:6]
    
    context = {
        'categories': categories,
        'schemes': schemes,
        'products': products,
    }
    return render(request, 'farmers/dashboard.html', context)

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
