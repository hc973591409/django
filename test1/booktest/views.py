from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    # hero = Hero.objects.get(pk=1)
    # get方法获取pk等于1的项目

    hero_list = Hero.objects.filter(isDelete=False)
    context = {'hero_list': hero_list}

    return render(request, 'booktest/index.html', context)


def show(request, id1, id2):
    return render(request, 'booktest/show.html', {'id': [id1, id2]})


# 模板继承练习
def index2(request):
    return render(request, 'booktest/index2.html')


def user_base(request):
    return render(request, 'booktest/base_user.html')


def user1(request):
    return render(request, 'booktest/user1.html', {'username': '老六'})


def user2(request):
    return render(request, 'booktest/user2.html', {'username': '老王'})


def htmlTest(request):
    return render(request, 'booktest/htmlTest.html', {'t1': '<h1>abc</h1>'})