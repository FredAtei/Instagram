from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = HTMLField(blank=True,default='Hey There I am using Instagram')

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = HTMLField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0,blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    content = HTMLField()
    created = models.DateTimeField(auto_now_add=True)    
    
  