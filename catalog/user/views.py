from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(request):

    if request.method != "POST":
        return render(request, "user/login.html")
    
    username = request.POST["username"]
    password = request.POST["password"]

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user=user)
        messages.add_message(request, messages.SUCCESS, "Logged in successfully")
        return redirect("index")


    messages.add_message(request, messages.ERROR, "Wrong username or password")
    return redirect("login")

def logout(request):

    if request.method != "POST":
        return render(request, "pages/index.html")
    
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, "loguted successfully")
    return redirect("index")

def register(request):

    if request.method != "POST":
        return render(request, "user/register.html")
    
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]

    if password != repassword:
        messages.add_message(request, messages.WARNING, "password and repassword must be same")
        return redirect("register")
    if User.objects.filter(email = email).exists():
        messages.add_message(request, messages.WARNING, "user with this email already exists")
        return redirect("register")
    
    user = User.objects.create_user(username= username, password = password, email = email)
    user.save()
    messages.add_message(request, messages.SUCCESS, "registered successfully")
    return redirect("login")
