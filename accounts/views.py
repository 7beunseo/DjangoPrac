from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.models import User
from .forms import *

# 회원가입
def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})
    
    form = SignUpForm(request.POST)
    if form.is_valid():
        print("in")
        user = form.save()
        return redirect('login')
    else:
        print("out")
        return render(request, 'accounts/signup.html', {'form': form})

# 로그인
def login_view(request):
    if request.method=="GET":
        return render(request, 'accounts/login.html', {'form':AuthenticationForm})
    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('index')
    return render(request, 'accounts/login.html',{'form':form})

# 로그아웃
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
