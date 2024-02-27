from django.shortcuts import render, redirect
from posts.models import Post
from .models import User, Follow

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

# my following
def my_following(request):
    followings_follow_queryset = Follow.objects.filter(follower = request.user)
    followings = [ follow.following for follow in followings_follow_queryset]
    print(followings)
    return render(request, 'my_following.html', {'followings':followings})

# my follower
def my_followers(request):
    followers_follow_queryset = Follow.objects.filter(following = request.user) # 이 상태로는 Follow 객체이므로 follower.username 으로 접근할 수 없음
    print(followers_follow_queryset)
    followers = [ follow.follower for follow in followers_follow_queryset ]
    return render(request, 'my_followers.html', {'followers':followers})


# update profile
def update_userinfo(request):
    user = request.user
    if request.method == "POST":
        user.nickname = request.POST.get("nickname")
        new_img = request.FILES.get("profile")

        if new_img:
            previous_img = user.profile
            previous_img.delete() # 기존 프로필 삭제
            user.profile = new_img
            user.save()
        return redirect('mypage')
    return render(request, 'update_userinfo.html', {'user':user})
        
# follow, unfollow
def follow(request, follower, following, url, post_id):
    follower_user = User.objects.get(username = follower)
    following_user = User.objects.get(username = following)
    follow_status = Follow.objects.check_follow_status(follower_user, following_user)
    print(follow_status)
    if not follow_status.exists():
        Follow.objects.create(follower = follower_user, following = following_user)
    else:
        follow_status.delete()

    return redirect(url, post_id)
