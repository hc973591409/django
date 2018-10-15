from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_pic$', views.upload_pic, name='upload_pic'),
    url(r'^upload_handle$', views.upload_handle, name='upload_handle'),
    url(r'page_test$', views.page_test, name='page_test')
]


