from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
from .form import LoginForm
from .form import RegForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def reg(request):
    if request.method=='POST':
        regform=RegForm(request.POST)
        if regform.is_valid():
            regform.save(commit=True)
        return HttpResponse('reg success')
    else:
        regform=RegForm()
    return render(request,'reg.html',{'regform':regform})
def login(request):
    if request.method=='POST':
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            un=loginform.cleaned_data['user']
            pw=loginform.cleaned_data['pwd']
            dbuser=Reg.objects.filter(user=un,pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                return HttpResponse('login success')
    else:
        loginform=LoginForm()
        return render(request,'login.html',{'loginform':loginform})