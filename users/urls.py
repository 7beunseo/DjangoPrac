from django.urls import path
from .views import *

urlpatterns = [
    path('', mypage, name = "mypage"),
    path('my-likes/', my_likes, name = "my-likes"),
]