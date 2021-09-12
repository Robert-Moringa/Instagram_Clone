from django.shortcuts import render
from .models import Image


# Create your views here.
def welcome(request):
    title="Instagram's finest clone"
    images =Image.objects.all()
    return render(request, 'index.html', {'images': images})
