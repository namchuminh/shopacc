from unittest import result
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.utils import checkPay, convertPrice, convertVND, sendAcc
from .models import AccCategory, AccFifa, AccCategory
from user.models import Profile, ShopCart
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
            cartNumber = ShopCart.objects.all().filter(user = user).count()
            money = Profile.objects.all().get(user = user).money
            money = convertVND(money)
            result = {'allacc':allacc, 'newacc':newacc, 'username': request.user.username, 'money': money, 'category':category, 'cartNumber':cartNumber}
            return render(request,self.template_name, result)

class detail(View):
    template_name =  'home/detail.html'
    def get(self, request, slug):
        if request.user.is_authenticated:
            user = User.objects.all().get(pk=request.user.id)
            cartNumber = ShopCart.objects.all().filter(user = user).count()
            money = Profile.objects.all().get(user = user).money
            money = convertVND(money)
            acc = AccFifa.objects.all().get(slug=slug)
            price = convertVND(acc.price)
            sale = convertVND(acc.sale)
            cate = AccCategory.objects.all().get(accfifa = acc)
            result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price, 'sale':sale, 'cate':cate, 'cartNumber':cartNumber}
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
            cartNumber = ShopCart.objects.all().filter(user = user).count()
            money = Profile.objects.all().get(user = user).money
            acc = AccFifa.objects.all().get(slug=slug)
            price = convertVND(acc.price)
            money = convertVND(money)
            result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price, 'cartNumber':cartNumber}
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
                    error = "S??? d?? kh??ng ?????, vui l??ng n???p th??m ti???n!"
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
                        error = "Mua t??i kho???n th??nh c??ng, vui l??ng ki???m tra email ????? nh???n t??i kho???n!"
                        result = {'login' : True, 'username': request.user.username, 'money': newMoney, 'acc':acc, 'price': price, 'error':error}
                        return render(request,self.template_name,result)
                    else:
                        user = User.objects.all().get(pk=request.user.id)
                        money = Profile.objects.all().get(user = user).money
                        acc = AccFifa.objects.all().get(slug=slug)
                        price = convertVND(acc.price)
                        money = convertVND(money)
                        error = "Vui l??ng nh???p v??o email h???p l???! V?? d???: nguyenvana@gmail.com!"
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

class category(View):
    template_name =  'home/category.html'
    def get(self, request, slug):
        if request.user.is_authenticated:
            user = User.objects.all().get(pk=request.user.id)
            cartNumber = ShopCart.objects.all().filter(user = user).count()
            money = Profile.objects.all().get(user = user).money
            allCate = AccCategory.objects.all()
            cate = AccCategory.objects.all().get(slug=slug)
            acc = AccFifa.objects.all().filter(category=cate)
            acc = convertPrice(acc)
            money = convertVND(money)
            result = {'login' : True, 'username': request.user.username, 'money': money,'acc':acc, 'cate':cate, 'allCate':allCate, 'cartNumber':cartNumber}
            return render(request,self.template_name,result)
        else:
            category = AccCategory.objects.all().get(slug=slug)
            result = {'login' : False, 'username': request.user.username}
            return render(request,self.template_name,result)

        


