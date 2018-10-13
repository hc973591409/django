from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'), # name用于反向解析
    url(r'^(\d+)/(\d+)$', show, name='show'),
    url(r'^index2$', index2, name='index2'),
    url(r'^user_base$', user_base, name='user_base'),
    url(r'^user1$', user1, name='user1'),
    url(r'^user2$', user2, name='user2'),
    url(r'^htmlTest$', htmlTest, name='htmlTest'),
    
]
