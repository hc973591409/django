from django.core.paginator import *
from django.shortcuts import render

from .models import *

# Create your views here.


def index(request):
    hero_list = Hero.objects.all()
    # 创建一个分页对象, 一页放置5个
    paginator = Paginator(hero_list, 5)
    # 取出第一页内容
    p = paginator.page(1)
    context = {'p': p}

    return render(request, 'booktest/index.html', context)
