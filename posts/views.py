from django.shortcuts import render, redirect, get_object_or_404
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

# post create
def create(request):
    # post 요청인 경우
    if request.method == "POST":
        post = Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            # 현재 유저
            writer = request.user
        )
        post.save()
        return redirect('posts-fbv')
    return render(request, 'crud/create.html')

# post detail
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    comments = Comment.objects.filter(post = post)

    return render(request, 'crud/detail.html', {'post': post, 'comments' : comments})

# post update
def update(request, id):
    post = get_object_or_404(Post, id = id)
    
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    
    return render(request, 'crud/update.html', {'post':post})

# post delete
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('posts-fbv')

# comment create - post 요청만 받음 
def comment_create(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    commnet = Comment.objects.create(
        content = request.POST.get('content'),
        post = post,
        writer = request.user
    )

    return redirect('detail', post_id)