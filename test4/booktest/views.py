from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import *
from django.core.paginator import *
# 导入分页程序
import os

from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world</h1>")


def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')

def upload_handle(request):
    pic1 = request.FILES['pic1']
    pic_name = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(pic_name, 'w') as fpic:
        for c in pic1.chunks():
            fpic.write(c)

    return HttpResponse('<img src="/static/media/%s"/>' %pic1.name)

def page_test(request): 
    """分页练习"""
    h_list = Hero.objects.all()
    # 进行分页，一页放置5个
    page_tor = Paginator(h_list, 5)
    pag = page_tor.page(1)
    context = {'page': pag}
    return render(request, 'booktest/page_test.html', context)

def area2(request, id):
    id1 = int(id)
    if id == 0:
        data = Areas.objects.filter(p__isnull=True)
    else:
        data = [{}]
    li = []
    for area in data:
        li.append([area.id,area.atitle])
    return JsonResponse({'data': list})


