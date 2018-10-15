from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^area$', views.area, name='area'),
        url(r'^pro/$', views.pro, name='pro'),
        url(r'^city(\d+)/$', views.city, name='city'),
    ]

