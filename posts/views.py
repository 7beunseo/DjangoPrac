from django.shortcuts import render
from .models import *

# cbv 사용하기위해 임포트 필요
from django.views.generic import ListView

# 대문 페이지
def index(request):
    return render(request, 'index.html')

# fbv posts 목록 페이지
def fbv_list(request):
    # Post의 모든 데이터를 id가 큰 순으로 가져옴
    posts = Post.objects.all().order_by('-id')

    # posts 라는 이름으로 list.html에서 사용 
    return render(request, 'posts.html', {'posts':posts})

# cbv posts 목록 페이지
class cbv_list(ListView):
    model = Post 
    ordering = '-id'
