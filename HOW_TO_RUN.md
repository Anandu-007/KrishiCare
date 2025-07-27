# How to Run the Farmers Module

## ✅ Server is Running!

The Django server is now running at: **http://localhost:8000**

## 🚀 Access the Application

### Main Pages:
1. **Home Page**: http://localhost:8000/home/
2. **Farmers Dashboard**: http://localhost:8000/farmers/
3. **Plant Detection (Image Upload)**: http://localhost:8000/farmers/plant-detection/
4. **Admin Dashboard**: http://localhost:8000/admin/dashboard/

### Image Upload Feature:
- Go to: http://localhost:8000/farmers/plant-detection/
- Click "Choose File" to select a plant image
- Add optional notes
- Click "Detect Plant" to upload and process
- View uploaded images in the "Recent Detections" section

## 🎯 Key Features Working:

### ✅ Plant Detection with Image Upload
- Upload plant images
- View uploaded images
- Detection history
- Statistics display

### ✅ Farmers Dashboard
- Overview of modules
- Quick access to features
- Recent schemes and products

### ✅ Admin Panel
- Custom admin dashboard (not Django default)
- Manage schemes, products, categories
- View farmers and users

## 🔧 If You Need to Restart:

```bash
cd project
python manage.py runserver
```

## 📱 Test the Image Upload:

1. Go to: http://localhost:8000/farmers/plant-detection/
2. Upload any image file (JPG, PNG, etc.)
3. Add some notes
4. Click "Detect Plant"
5. See your uploaded image in the Recent Detections section

## 🎉 You're All Set!

The farmers module is now running with full image upload functionality! 