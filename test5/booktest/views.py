from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')

def area(request):
    return render(request, 'booktest/area.html')

def pro(request):
    data = Areas.objects.filter(p__isnull=True)
    li = []
    for a in data:
        li.append([a.id, a.atitle])

    return JsonResponse({'data': li})

def city(request, cid):
    """获取市区信息"""
    cid = int(cid)
    data = Areas.objects.filter(p_id=cid)      # p是上级对象，获得上级对象的id
    li = []
    for c in data:
        li.append({'id': c.id, 'title': c.atitle})

    return JsonResponse({'data': li})
