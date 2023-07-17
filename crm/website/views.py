from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm,AddRecordForm
from .models import Record
def home(request):
    records=Record.objects.all()
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

        return render(request,'home.html',{'records':records})

def logout_user(request):
    

    logout(request)
    messages.success(request,"you have been logged out!")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})

def register_user(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"you have succesfully registered.")
            return redirect('home')
    else:
        form=SignupForm()
        return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        #look recor
        customer_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"you must be logged in to view.")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record deleted sucessfully!")
        return redirect('home')
    else:
        messages.success(request,"must be logged in to perform this action.")
        return redirect('home')
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record added sucessfully!")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"you must be logged in!")
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record updated sucessfully!")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"you must be logged in!")
        return redirect('home')