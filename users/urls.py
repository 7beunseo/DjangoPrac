from django.urls import path
from .views import *

urlpatterns = [
    path('', mypage, name = "mypage"),
    path('my-likes/', my_likes, name = "my-likes"),
    path('my-posts/', my_posts, name = "my-posts"),
    path('update-userinfo/', update_userinfo, name = 'update-userinfo'),
    path('follow/<str:follower>/<str:following>/<str:url>/<int:post_id>/', follow, name = "follow"),
    path('my-followers/', my_followers, name = "my-followers"),
    path('my-followings/', my_following, name = "my-followings"),
    
]