# Farmers Module - KrishiCare

This is a comprehensive farmers module for the KrishiCare agricultural platform, featuring categories, schemes, products (seeds, fertilizers, tools), and plant detection functionality.

## Features

### 🏠 **Farmers Dashboard**
- Overview of all modules
- Quick access to categories, schemes, products, and plant detection
- Recent schemes and featured products display

### 📂 **Categories**
- Browse farming categories with dropdown functionality
- Filter and search categories
- Category statistics

### 📋 **Schemes**
- Government schemes and subsidies for farmers
- Search and filter by category, region
- Application deadlines and eligibility criteria
- Scheme statistics

### 🛒 **Products**
- Three product types: Seeds, Fertilizers, Tools
- Product filtering by type
- Search and sort functionality
- Stock management
- Product statistics

### 🌱 **Plant Detection**
- AI-powered plant identification
- Upload plant images for analysis
- Health status detection
- Detection history and statistics

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher

### Step 1: Navigate to Project Directory
```bash
cd project
```

### Step 2: Install Dependencies
```bash
pip install django
pip install Pillow  # For image handling
```

### Step 3: Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Sample Data
```bash
python add_sample_data.py
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

## Accessing the Application

### Main URLs:
- **Home Page**: http://localhost:8000/home/
- **Farmers Dashboard**: http://localhost:8000/farmers/
- **Categories**: http://localhost:8000/farmers/categories/
- **Schemes**: http://localhost:8000/farmers/schemes/
- **Products**: http://localhost:8000/farmers/products/
- **Plant Detection**: http://localhost:8000/farmers/plant-detection/
- **Admin Panel**: http://localhost:8000/admin/

### Sample Login Credentials:
- **Farmer User**: 
  - Username: `farmer1`
  - Password: `farmer123`

## Module Structure

### Models
- **Category**: Farming categories and classifications
- **Scheme**: Government schemes and subsidies
- **Product**: Seeds, fertilizers, and tools
- **PlantDetection**: Plant identification results
- **Farmer**: Farmer user profiles

### Views
- `farmers_dashboard`: Main dashboard view
- `view_categories`: Categories listing with filters
- `view_schemes`: Schemes listing with search
- `view_products`: Products with type filtering
- `plant_detection`: Plant detection functionality

### Templates
- `farmers/dashboard.html`: Main dashboard
- `farmers/categories.html`: Categories page
- `farmers/schemes.html`: Schemes page
- `farmers/products.html`: Products page
- `farmers/plant_detection.html`: Plant detection page

## Features in Detail

### Categories Module
- Dropdown filtering functionality
- Category statistics
- Browse and view details

### Schemes Module
- Search by scheme name
- Filter by category and region
- Application deadlines
- Quick action buttons for different scheme types

### Products Module
- Filter by product type (Seeds, Fertilizers, Tools)
- Search functionality
- Price sorting (Low to High, High to Low)
- Stock filtering (In Stock, Low Stock, Out of Stock)
- Add to cart functionality (placeholder)

### Plant Detection Module
- Image upload for plant detection
- Real-time analysis simulation
- Detection results with confidence scores
- Health status analysis
- Detection history
- Export and sharing capabilities

## Admin Panel Features

Access the admin panel at http://localhost:8000/admin/ to:
- Manage categories, schemes, products
- View plant detections
- Manage farmer profiles
- Add/edit/delete all data

## Customization

### Adding New Categories
1. Go to Admin Panel → Categories
2. Add new category with name and description

### Adding New Schemes
1. Go to Admin Panel → Schemes
2. Fill in scheme details including category, eligible crops, and deadlines

### Adding New Products
1. Go to Admin Panel → Products
2. Select product type (seed/fertilizer/tool)
3. Add product details, price, and stock quantity

## Troubleshooting

### Common Issues:

1. **Migration Errors**
   ```bash
   python manage.py makemigrations --empty app
   python manage.py migrate
   ```

2. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic
   ```

3. **Media Files Not Uploading**
   - Ensure MEDIA_ROOT directory exists
   - Check file permissions

4. **Template Errors**
   - Verify all template files are in correct directories
   - Check for syntax errors in templates

### Database Reset (if needed)
```bash
rm db.sqlite3
python manage.py migrate
python add_sample_data.py
```

## Future Enhancements

- Real AI integration for plant detection
- Payment gateway for product purchases
- Mobile app development
- Weather integration
- Crop advisory system
- Marketplace functionality

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure database migrations are complete
4. Check Django debug logs for errors

---

**Happy Farming! 🌾** 