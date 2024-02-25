from django.shortcuts import render
from posts.models import Post
from .models import User

# mypage
def mypage(request):
    return render(request, 'mypage.html')

# my likes at posts
def my_likes(request):
    posts = request.user.post_like.all() # 역참조
    return render(request, 'my_likes.html', {'posts':posts})

# my posts
def my_posts(request):
    posts = Post.objects.filter(writer = request.user)
    return render(request, 'my_posts.html', {'posts':posts})