from django.shortcuts import render
from datetime import datetime
# Create your views here.
date=datetime.now()
def index(request):
    return render(request,'main/index.html',{'date':date})
def about(request):
    return render(request,'main/about.html',{'date':date})
def contact(request):
    return render(request,'main/contact.html',{'date':date})
def menu(request):
    return render(request,'main/menu.html',{'date':date})
def services(request):
    return render(request,'main/services.html',{'date':date})
def register(request):
    return render(request,'auth/register.html')
def login(request):
    return render(request,'auth/login.html')