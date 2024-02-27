from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import Follow

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
    tags = Tag.objects.all()
    # post 요청인 경우
    if request.method == "POST":
        # 태그 리스트
        selected_tags = request.POST.getlist("tags")

        post = Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            # 현재 유저
            writer = request.user
        )

        # 태그 다대다 연결 
        for selected_tag in selected_tags:
            tag = Tag.objects.get(name = selected_tag)
            post.tags.add(tag)

        post.save()
        return redirect('posts-fbv')
    return render(request, 'crud/create.html', {'tags':tags})

# post detail
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    comments = Comment.objects.filter(post = post)
    follow_status = Follow.objects.check_follow_status(request.user, post.writer)
    return render(request, 'crud/detail.html', {'post': post, 'comments' : comments, 'follow_status' : follow_status})

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

# add or remove post like
def post_likes(request, post_id, url):
    post = get_object_or_404(Post, id = post_id)

    if request.user in post.likes.all(): # post.likes는 ManyToManyField의 관련 매니저 객체, 반복가능하지 않음 
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    if(url == "detail"):
        return redirect(url, post_id)
    return redirect(url)

# add or remove comment like
def comment_likes(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return redirect('detail', post_id)
