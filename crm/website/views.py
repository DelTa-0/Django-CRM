from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def home(request):
    #check to see if logging in 
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"there was a error please log in again!")
            return redirect('home')
    else:

        return render(request,'home.html',{})

def logout_user(request):
    

    logout(request)
    messages.success(request,"you have been logged out!")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})