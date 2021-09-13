from django.shortcuts import render, redirect
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm


# Create your views here.
def welcome(request):
    title="Instagram's finest clone"
    images =Image.objects.all()
    return render(request, 'index.html', {'images': images})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            # article.post = strip_tags(request.POST['post'])
            # article.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new-post.html', {"form": form})
