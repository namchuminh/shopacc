from ast import ExceptHandler, Return
import json
from unittest import result
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from home.models import AccFifa
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.utils import convertVND
from user.models import Profile, ShopCart
from .utils import checkemail, checkpassword, checkusername
from django.http import JsonResponse



# Create your views here.

class Userlogin(View):
    template_name =  'user/login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,self.template_name)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        if request.method == 'POST':
            username= request.POST["uname"]
            password = request.POST["psw"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_URL)
            else:
                newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
                result = {'newacc':newacc, 'error': 'Sai tài khoản hoặc mật khẩu! Vui lòng đăng nhập lại!'}     
                return render(request,self.template_name,result)
        else:
            newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
            result = {'newacc':newacc} 
            return render(request,self.template_name,result)

class Userlogout(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        else:
            logout(request)
            return redirect(settings.LOGOUT_URL)

class Userchangeinfo(View):
    template_name =  'user/changeinfo.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        else:
            user = User.objects.all().get(username=request.user.username)
            cartNumber = ShopCart.objects.all().filter(user = user).count()
            newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
            user = User.objects.all().get(pk=request.user.id)
            money = Profile.objects.all().get(user = user).money
            money = convertVND(money)
            result = {'username': user.username,'email': user.email, 'money': money, 'cartNumber':cartNumber }
            return render(request,self.template_name,result)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        else:
            if request.method == 'POST':
                email= request.POST["email"]
                password = request.POST["psw"]
                if(checkemail(email) == False):
                    return render(request,self.template_name,{'error':'Email không hợp lệ! Vui lòng nhập lại!'})

                if(checkpassword(password) == False):
                    user = User.objects.all().get(username=request.user.username)
                    user.email = email
                    user.save()
                    return redirect('change-info')

                user = User.objects.all().get(username=request.user.username)
                user.email = email
                user.set_password(password)
                user.save()
                user = authenticate(request, username=request.user.username, password=password)
                login(request, user)
                return redirect('change-info')
            else:
                user = User.objects.all().get(username=request.user.username)
                newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
                result = {'username': user.username,'email': user.email}
                return render(request,self.template_name,result)

class Usersigup(View):
    template_name =  'user/sigup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,self.template_name)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method == 'POST':
                username = request.POST["uname"]
                email= request.POST["email"]
                password = request.POST["psw"]

                if checkusername(username) == False:
                    result = {'error': 'Vui lòng nhập tài khoản hợp lệ!'}
                    return render(request,self.template_name, result)

                if checkpassword(password) == False:
                    result = {'error': 'Vui lòng nhập mật khẩu hợp lệ!'}
                    return render(request,self.template_name, result)

                if checkemail(email) == False:
                    result = {'error': 'Vui lòng nhập email hợp lệ!'}
                    return render(request,self.template_name, result)

                try:
                    newuser = User.objects.create_user(username, email, password)
                    newuser.save()
                    user = User.objects.all().get(username=username)
                    profile = Profile.objects.create(user=user, money = 0)
                    profile.save()
                    result = {'error': 'Đăng ký thành công! Vui lòng đăng nhập!'}
                    return render(request,self.template_name, result)
                except:
                    result = {'error': 'Tài khoản hoặc email đã tồn tại! Vui lòng đăng nhập!'}
                    return render(request,self.template_name, result)


class Ajax(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            accname = request.POST['accname']
            data = {
                'accname':accname,
                'error':False
            }
            return JsonResponse(data)
