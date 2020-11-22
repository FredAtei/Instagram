from django.shortcuts import render
from .models  import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'profile/index.html')