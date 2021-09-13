from django.shortcuts import render, redirect
from .models import Comment, Image
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, NewCommentForm


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

@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    comments =Comment.objects.all()
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
            # article.post = strip_tags(request.POST['post'])
            # article.save()
        return redirect('new_comment')

    else:
        form = NewCommentForm()
    return render(request, 'new-comment.html', {"form": form, "comments": comments})
