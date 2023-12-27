from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from investments_app.views import view_home

# Create your views here.

def view_login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        login_user = authenticate(request, username=username, password=password)
        print(login_user)
        if login_user is not None:
            login(request, login_user)                        
            return redirect('home')
    return render(request,'auth/login.html')

def view_logout_user(request):
    logout(request)
    return redirect('login')


def view_register_user(request):
    emsg= None
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        #reg_user = User(username=uname, password=password, email=email, first_name=fname, last_name=lname)             
        if uname =="" or fname=="" or lname=="" or email=="" or password=="" :
            emsg="All fields are mandatory"            
            return render(request,'auth/userregistration.html',{'emsg':emsg})
        if password != cpassword:
            emsg="Passwords don't match"
            return render(request,'auth/userregistration.html',{'emsg':emsg})
        if User.objects.filter(username=uname).exists():
            emsg="Username already exists"            
            return render(request,'auth/userregistration.html',{'emsg':emsg})        
        User.objects.create_user(username=uname, password=password, email=email, first_name=fname, last_name=lname)
        emsg="User Created Successfully"               
        return render(request,'auth/userregistration.html',{'emsg':emsg})                        
    return render(request,'auth/userregistration.html')
