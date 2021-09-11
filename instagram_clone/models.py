from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    image_path = models.ImageField(upload_to = 'uploads/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.ForeignKey('Likes', on_delete=models.CASCADE)
    comments=models.ForeignKey('Comments', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.name

    @classmethod
    def update_caption(cls, caption):
        update = cls.objects.filter(id = id).update(caption=caption)
        update.save()
    
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'profile/')
    bio=models.TextField()
    user = models.OneToOneField(User,related_name='profile' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Like(models.Model):
    like= models.IntegerField()
    user = models.ForeignKey(User, related_name='commented_by', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='likes_for', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.like)

class Comment(models.Model):
    comment= models.TextField()
    user = models.ForeignKey(User, related_name='commenter', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='commentee', on_delete=models.CASCADE)

    def add_comment(self):
        self.save()
    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments
