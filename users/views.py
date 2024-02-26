from django.shortcuts import render, redirect
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

# update profile
def update_userinfo(request):
    user = request.user
    if request.method == "POST":
        user.nickname = request.POST.get("nickname")
        new_img = request.FILES.get("profile")

        if new_img:
            previous_img = user.profile
            previous_img.delete()
            user.profile = new_img
            user.save()
        return redirect('mypage')
    return render(request, 'update_userinfo.html', {'user':user})
        
