from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'pic'),
    url(r'^new/post/$', views.post, name='post'),
    url(r'^new/profile/$', views.addprofile, name='new-profile'),
]