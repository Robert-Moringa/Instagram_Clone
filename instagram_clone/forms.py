from django import forms
from .models import Image,Comment

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'post_date', 'likes', 'comments']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_on', 'user')