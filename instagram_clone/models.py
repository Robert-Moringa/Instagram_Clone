from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    image_path = models.ImageField(upload_to = 'uploads/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.ForeignKey('Likes', on_delete=models.CASCADE)
    comments=models.ForeignKey('Comments', on_delete=models.CASCADE)

