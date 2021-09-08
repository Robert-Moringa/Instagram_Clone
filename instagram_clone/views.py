from django.shortcuts import render


# Create your views here.
def welcome(request):
    title="Instagram's finest clone"
    return render(request, 'index.html')
