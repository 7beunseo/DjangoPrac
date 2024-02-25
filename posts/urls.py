from django.urls import path
from .views import *;

urlpatterns = [
    path('', index, name = "index"),
    path('posts-fbv/', fbv_list, name = "posts-fbv"),
    path('posts-cbv/', cbv_list.as_view(), name = "posts-cbv"),
]