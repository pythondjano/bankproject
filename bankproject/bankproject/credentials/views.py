from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import render, redirect, get_object_or_404

from credentials.models import Category


# Create your views here.

def userhome(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "userhome.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Taken")
            return redirect('login')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('login')
    else:
        messages.info(request, "password not matching")
        return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('index.html')


def user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('/')
        # else:
        #     messages.info(request,"invalid credentials")
        #     return redirect('login')
    return render(request, "userhome.html")


def reregister(request):
    if request.method == 'POST':
        Fullname = request.POST['Name']
        Date_of_birth = request.POST['Date_of_birth']
        Age = request.POST['Age']
        male = request.POST['male']
        female = request.POST['female']
        other = request.POST['other']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        return redirect('/')

    return render(request, "reregister.html")


def index(request):
    return render(request, "index.html")
