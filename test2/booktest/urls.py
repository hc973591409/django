from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myexp$', views.myexp),
    url(r'^upload_pic$', views.upload_pic),
    url(r'^uploadHandler/$', views.uploadHandler),
]
