from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        user=auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials!!')    


    return render (request,'loginform.html')

def logout(request):
    auth.logout(request)
    return redirect('login')        