from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_id = request.POST.get('email_id')
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        conf_passwd = request.POST.get('conf_passwd')
        # print(first_name,last_name,email_id,username,passwd,conf_passwd)

        if (passwd == conf_passwd):
            if User.objects.filter(username=username).exists():
                print("Username Taken")
                messages.info(request, "Username Taken")
            elif User.objects.filter(email=email_id).exists():
                print("Email Taken")
                messages.info(request, "Email Taken")
            else:
                user = User.objects.create_user(username=username, password=passwd,
                                                email=email_id, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            print("Password Doesn't Match!!")
            messages.info(request, "Password Doesn't Match!!")

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')

        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
            print("Hello")
            return redirect('create_book_page')
    return render(request, "login.html")
