from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'pic'),
    url(r'^new/post/$', views.post, name='post'),
]