from django.test import TestCase
from apps.resources import models

class TestTagModel(TestCase):
    
    def setUp(self):
        self.tag_name = 'Hotel'
        self.tag = models.Tag(name=self.tag_name)   
    
    def test_create_tag_object_successfull(self):
        self.assertIsInstance(self.tag, models.Tag)
    
    def test_dunder_str(self):
        self.assertEqual(str(self.tag), self.tag_name)
        
        # test