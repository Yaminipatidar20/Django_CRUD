from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout


def home(request):
    stu=Student.objects.all()   # show data
    context={
            'stu':stu    
            }
    return render(request, 'home.html', context)


def signin(request):                      # login
    if request.method=="POST":
        user=User()
        u_name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=u_name,password=pwd)
        if user :
            login(request,user)
            return redirect(home)
        return render(request,'signin.html')
    else:
        return render(request, 'signin.html')


def register(request):                           # signup
    msg=""
    if request.method=="POST":
        user=User()
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        pwd=request.POST.get('password')
        pwd2=request.POST.get('psw-repeat')
        if pwd==pwd2:
            user.set_password(pwd)
        else:
            msg=" please enter same password"
        user.save()
        return redirect(signin)
    return render(request, 'register.html',{'msg':msg})


def index(request):
    return render(request, 'index.html')   # home page


def logout_view(request):
    logout(request)
    return redirect('index')


def add(request):
    if request.method=='POST':
        stu=Student()                 # add data
        stu.name=request.POST.get('name')
        stu.cls=request.POST.get('cls')
        stu.mob=request.POST.get('mob')
        stu.subject=request.POST.get('subject')
        stu.save()
        return redirect(home)
    return render(request, 'add.html')


def update(request):
    if request.method=='GET':
        stu_id=request.GET.get('stu_id')
        stu=Student.objects.get(id=stu_id)
        return render(request, 'update.html',{'stu':stu})
    else:
        stu_id=request.POST.get('stu_id')
        stu=Student.objects.get(id=stu_id)        # update data
        stu.name=request.POST.get('name')
        stu.cls=request.POST.get('cls')
        stu.mob=request.POST.get('mob')
        stu.subject=request.POST.get('subject')
        stu.save()
        return redirect(home)


def delete(request):                      # delete data
    stu_id=request.GET.get('stu_id')
    stu=Student.objects.get(id=stu_id)
    stu.delete()
    return redirect(home)
