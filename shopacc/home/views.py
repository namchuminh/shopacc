from unittest import result
from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.utils import checkPay, convertPrice, convertVND, sendAcc
from .models import AccCategory, AccFifa
from user.models import Profile
from django.views import View
from django.contrib.auth.models import User

# Create your views here.

class index(View):
    template_name =  'home/index.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:    
            allacc = AccFifa.objects.all().filter(product=True)
            newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
            category = AccCategory.objects.all()
            allacc = convertPrice(allacc)
            newacc = convertPrice(newacc) 
            result = {'allacc':allacc, 'newacc':newacc, 'category':category}
            return render(request,self.template_name, result)

class home(View):
    template_name =  'home/home.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        else:
            allacc = AccFifa.objects.all().filter(product=True)
            newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
            category = AccCategory.objects.all()
            allacc = convertPrice(allacc)
            newacc = convertPrice(newacc)
            user = User.objects.all().get(pk=request.user.id)
            money = Profile.objects.all().get(user = user).money
            money = convertVND(money)
            result = {'allacc':allacc, 'newacc':newacc, 'username': request.user.username, 'money': money, 'category':category}
            return render(request,self.template_name, result)

class detail(View):
    template_name =  'home/detail.html'
    def get(self, request, slug):
        if request.user.is_authenticated:
            user = User.objects.all().get(pk=request.user.id)
            money = Profile.objects.all().get(user = user).money
            money = convertVND(money)
            acc = AccFifa.objects.all().get(slug=slug)
            price = convertVND(acc.price)
            sale = convertVND(acc.sale)
            result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price, 'sale':sale}
            return render(request,self.template_name,result)
        else:
            acc = AccFifa.objects.all().get(slug=slug)
            result = {'login' : False, 'acc':acc}
            return render(request,self.template_name,result)

class pay(View):
    template_name =  'home/pay.html'
    def get(self, request, slug):
        if request.user.is_authenticated:
            user = User.objects.all().get(pk=request.user.id)
            money = Profile.objects.all().get(user = user).money
            acc = AccFifa.objects.all().get(slug=slug)
            price = convertVND(acc.price)
            money = convertVND(money)
            result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price}
            return render(request,self.template_name,result)
        else:
            return redirect('user-login')

    def post(self, request,slug):
        if request.user.is_authenticated:
            if request.method == 'POST':
                emailacc = request.POST["emailacc"]
                acc = AccFifa.objects.all().get(slug=slug)
                user = User.objects.all().get(pk=request.user.id)
                money = Profile.objects.all().get(user = user).money
                price = acc.price
                newMoney = checkPay(price,money)
                if (newMoney == False):
                    user = User.objects.all().get(pk=request.user.id)
                    money = Profile.objects.all().get(user = user).money
                    acc = AccFifa.objects.all().get(slug=slug)
                    price = convertVND(acc.price)
                    money = convertVND(money)
                    error = "Số dư không đủ, vui lòng nạp thêm tiền!"
                    result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price, 'error':error}
                    return render(request,self.template_name,result)
                else:
                    if(sendAcc(emailacc, acc.username, acc.password) == True):
                        user = User.objects.all().get(pk=request.user.id)
                        money = Profile.objects.all().get(user = user).money
                        acc = AccFifa.objects.all().get(slug=slug)
                        price = convertVND(acc.price)
                        updateMoney = Profile.objects.all().get(user = user)
                        updateMoney.money = newMoney
                        updateMoney.save()
                        newMoney = convertVND(newMoney)
                        error = "Mua tài khoản thành công, vui lòng kiểm tra email để nhận tài khoản!"
                        result = {'login' : True, 'username': request.user.username, 'money': newMoney, 'acc':acc, 'price': price, 'error':error}
                        return render(request,self.template_name,result)
                    else:
                        user = User.objects.all().get(pk=request.user.id)
                        money = Profile.objects.all().get(user = user).money
                        acc = AccFifa.objects.all().get(slug=slug)
                        price = convertVND(acc.price)
                        money = convertVND(money)
                        error = "Vui lòng nhập vào email hợp lệ! Ví dụ: nguyenvana@gmail.com!"
                        result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price, 'error':error}
                        return render(request,self.template_name,result)

            else:
                user = User.objects.all().get(pk=request.user.id)
                money = Profile.objects.all().get(user = user).money
                acc = AccFifa.objects.all().get(slug=slug)
                price = convertVND(acc.price)
                result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price}
                return render(request,self.template_name,result)
        else:
            return redirect('user-login')


        


