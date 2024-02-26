from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.models import User
from .forms import *

# 회원가입
def signup_view(request):
    # 회원가입 폼 요청 
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})
    
    # 회원가입 데이터 유효성 검사
    form = SignUpForm(request.POST, request.FILES)
    if form.is_valid():
        user = form.save()
        return redirect('login')
    else:
        return render(request, 'accounts/signup.html', {'form': form})

# 로그인
def login_view(request):
    # 로그인 폼 요청 
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form':AuthenticationForm})
    
    # 로그인 데이터 유효성 검사
    form=AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('index')
    return render(request, 'accounts/login.html', {'form':form})

# 로그아웃
def logout_view(request):
    # 로그아웃 로직 진행 
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
