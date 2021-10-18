from django.test import TestCase
from .models import Image, Profile

# Create your tests here.

class ImageTest(TestCase):
    """A test class for Image Model"""

    def setUp(self):
        self.profile = Profile(name = 'kilonzijnr')
        self.profile.save_profile()
        self.image_test = Image(name= 'codeSetup', caption = 'Gaols', location = self.location, category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after)> 0)
       

