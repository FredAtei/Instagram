from django.shortcuts import render
from .models  import Picture

# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    ctx = {'pictures': pictures}
    return render(request, 'profile/index.html', ctx)