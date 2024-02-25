from django.shortcuts import render
from posts.models import Post
from .models import User

def mypage(request):
    return render(request, 'mypage.html')

def my_likes(request):
    posts = request.user.post_like.all() # 역참조
    print(posts)
    return render(request, 'my_likes.html', {'posts':posts})