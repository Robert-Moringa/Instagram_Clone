from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    image_path = models.ImageField(upload_to = 'uploads/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.ForeignKey('Likes', on_delete=models.CASCADE)
    comments=models.ForeignKey('Comments', on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, caption):
        update = cls.objects.filter(id = id).update(caption=caption)
        update.save()
    
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'profile/')
    bio=models.TextField()

class Like(models.Model):
    like= models.IntegerField()

    def __str__(self):
        return str(self.like)

class Comment(models.Model):
    comment= models.TextField()

    def add_comment(self):
        self.save()
    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments
