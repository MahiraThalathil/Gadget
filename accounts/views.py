from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,lastname=lastname,firstname=firstname,phone=phone)
                def __init__(self):
                     User.save()
                

            print("user created")
                  
        else:
            print("password not matched")

         
        return redirect("/")
    else:
         return render(request,'register.html')



def login(request):
    if request.method=="POST":
        username=request.POST["Username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid')
            return redirect('register')
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('login')



