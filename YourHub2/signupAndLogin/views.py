from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .forms import CustomUCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Items
from django.core.signals import request_finished
from django.http import HttpRequest
from scrapy.crawler import CrawlerProcess
from scrapyd_api import ScrapydAPI
from scrapy.utils.project import get_project_settings
from .Yourhub2spider import ProductSpider
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from scrapy.cmdline import execute


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUCreationForm()
    return render(request, 'signuptemplate.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            #not_active means maybe banned or something
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'username or password not correct')
                return redirect('login')
    return render(request,'design.html')
def home(request):
    return render(request,'home.html')
def logout_method(request):
    return logout(request,'design.html')
def newitem(request):
    if request.method == 'POST':
        current_u = request.user
        temp_Item = Items(Item = request.POST['new-item-input'],Itemuser = current_u)
        temp_Item.save()
        return redirect('home')
    return render(request,'newitem.html')
def currentprices(request):
    #python manage.py runserver --nothreading --noreload
    items = Items.objects.all()
    execute(['Yourhub2spider.py', 'crawl', 'Product_spider'])
    return render(request,'currentprices.html',{'items':items})



    

   

    

        
        


