from django.shortcuts import render, HttpResponse
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def myexp(request):
    return HttpResponse('hello world')

from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from somewhere import handle_uploaded_file

def upload_pic(request):
    return render(request, "booktest/upload_pic.html")


def uploadHandler(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
