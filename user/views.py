from django.contrib.auth import logout, login
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.
from user.form import MyUserCreationForm
from user.models import MyUser


def homeView(request,page):
    return None

def loginView(request):
    user = MyUserCreationForm()
    if request.method == 'POST':
        #用户登录
        if request.POST.get('loginUser',''):
            loginUser = request.POST.get('loginUser','')
            password = request.POST.get('password','')
            if MyUser.objects.filter(Q(mobile=loginUser) | Q(username=loginUser)):
                user = MyUser.objects.filter(Q(mobile=loginUser)|Q(username=loginUser)).first()
                if check_password(password,user.password):
                    login(request,user)
                    return redirect('/user/home/1.html')
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        #用户注册
        else:
            user = MyUserCreationForm(request.POST)
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            mobile = request.POST.get('mobile','')
            if user.is_valid():
                user.save()
                tips = '注册成功'
            else:
                if user.errors.get('username',''):
                    tips = user.errors.get('username','注册失败')
                else:
                    tips = user.errors.get('mobile','注册失败')
    return render(request,'login.html',locals())


def logoutView(request):
    logout(request)
    return redirect('/')