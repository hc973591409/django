from django.shortcuts import render, HttpResponse
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def myexp(request):
    return HttpResponse('hello world')


def upload_pic(request):
    return render(request, "booktest/upload_pic.html")


def uploadHandler(request):
    if request.method == "POST":
        f1 = request.FILES['pic']
        # fname = '%s/cars/%s' % (settings.MEDIA_ROOT,f1.name)
        # with open(fname, 'w') as pic:
        #     for c in f1.chunks():
        #         pic.write(c)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")
