from django.test import TestCase
from .models import Image, Comment

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.comment = Comment(name="This is great")
        self.comment.save_comment()

        self.image = Image(name='Anniversary', caption='The best way to have today', comment=self.comment)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)