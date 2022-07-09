from unittest import result
from django.shortcuts import redirect, render
from django.http import HttpResponse
from matplotlib.pyplot import get

from home.utils import convertVND
from .models import AccFifa
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
            result = {'allacc':allacc, 'newacc':newacc}
            return render(request,self.template_name, result)

class home(View):
    template_name =  'home/home.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        else:
            allacc = AccFifa.objects.all().filter(product=True)
            newacc = AccFifa.objects.all().filter(product=True).order_by('-id')[:11]
            user = User.objects.all().get(pk=request.user.id)
            money = Profile.objects.all().get(user = user).money
            result = {'allacc':allacc, 'newacc':newacc, 'username': request.user.username, 'money': money}
            return render(request,self.template_name, result)

class detail(View):
    template_name =  'home/detail.html'
    def get(self, request, slug):
        if request.user.is_authenticated:
            user = User.objects.all().get(pk=request.user.id)
            money = Profile.objects.all().get(user = user).money
            acc = AccFifa.objects.all().get(slug=slug)
            result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc}
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
            result = {'login' : True, 'username': request.user.username, 'money': money, 'acc':acc, 'price': price}
            return render(request,self.template_name,result)
        else:
            acc = AccFifa.objects.all().get(slug=slug)
            result = {'login' : False, 'acc':acc}
            return render(request,self.template_name,result)

        


