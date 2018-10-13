from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import *
from . import Checkcode
from io import StringIO

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


def csrf1(request):
    """csrf跨站请求伪造，请求一个表单"""
    return render(request, "booktest/csrf1.html")

def csrf2(request):
    """csrf跨站请求伪造，请求一个表单"""
    uname = request.POST['uname']
    return HttpResponse(uname)



def CheckCode(request):
    mstream = StringIO()
    print("IO")
    validate_code = Checkcode.create_validate_code()
    print("创建图片了吗")
    img = validate_code[0]
    img.save(mstream, "GIF")
    
    #将验证码保存到session
    request.session["CheckCode"] = validate_code[1]
    
    return HttpResponse(mstream.getvalue()) 


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        check_code = request.POST.get('checkcode')
        #从session中获取验证码
        session_code = request.session["CheckCode"]
        if check_code.strip().lower() != session_code.lower():
            return HttpResponse('验证码不匹配')
        else:
            return HttpResponse('验证码正确')          
        
    return render_to_response('login.html',{'error':"",'username':'','pwd':'' })

