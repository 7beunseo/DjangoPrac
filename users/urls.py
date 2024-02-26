from django.urls import path
from .views import *

urlpatterns = [
    path('', mypage, name = "mypage"),
    path('my-likes/', my_likes, name = "my-likes"),
    path('my-posts/', my_posts, name = "my-posts"),
    path('update-userinfo/', update_userinfo, name = 'update-userinfo')
]