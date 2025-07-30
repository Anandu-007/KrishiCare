from django.test import TestCase, Client
from django.urls import reverse
from .models import Farmer
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class FarmerRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_farmer_registration_with_approval_status(self):
        """Test that farmer registration works with approval status"""
        
        # Create a simple test image
        test_image = SimpleUploadedFile(
            "test_photo.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        
        # Test data for farmer registration
        farmer_data = {
            'name': 'Test Farmer',
            'phone': '9876543210',
            'place': 'Test Village',
            'address': 'Test Address',
            'land_size': '5.5',
            'farmer_type': 'small',
            'aadhaar': '123456789012',
            'approval_status': 'pending',
            'photo': test_image,
            'land_photo': test_image,
            'land_tax': test_image,
            'id_proof': test_image,
            'bank_passbook': test_image,
        }
        
        # Submit the form
        response = self.client.post(reverse('RegisterFarmer'), farmer_data)
        
        # Check if farmer was created
        self.assertEqual(Farmer.objects.count(), 1)
        
        # Get the created farmer
        farmer = Farmer.objects.first()
        
        # Check if approval status is set correctly
        self.assertEqual(farmer.name, 'Test Farmer')
        self.assertEqual(farmer.is_approved, False)  # pending should be False
        
        # Test with approved status
        farmer_data['approval_status'] = 'approved'
        farmer_data['name'] = 'Approved Farmer'
        farmer_data['aadhaar'] = '987654321098'
        
        response = self.client.post(reverse('RegisterFarmer'), farmer_data)
        
        # Check if second farmer was created
        self.assertEqual(Farmer.objects.count(), 2)
        
        # Get the approved farmer
        approved_farmer = Farmer.objects.filter(name='Approved Farmer').first()
        self.assertEqual(approved_farmer.is_approved, True)
        
    def test_farmer_model_approval_status(self):
        """Test that Farmer model handles approval status correctly"""
        
        # Test creating farmer with default approval status
        farmer = Farmer.objects.create(
            name='Test Farmer',
            phone='9876543210',
            place='Test Village',
            address='Test Address',
            land_size=5.5,
            farmer_type='small',
            aadhaar_number='123456789012'
        )
        
        # Default should be False
        self.assertFalse(farmer.is_approved)
        
        # Test setting approval status
        farmer.is_approved = True
        farmer.save()
        
        # Refresh from database
        farmer.refresh_from_db()
        self.assertTrue(farmer.is_approved)
