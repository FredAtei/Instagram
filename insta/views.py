from django.shortcuts import render,redirect
from .models  import Profile,Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPostForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.get_images()
    current_user = request.user
    return render(request, "profile/index.html",{'posts':posts, 'user':current_user})

def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request,'new_post.html', {"form": form})    