from django.urls import path
from .views import *;

urlpatterns = [
    path('', index, name = "index"),
    path('posts-fbv/', fbv_list, name = "posts-fbv"),
    path('posts-cbv/', cbv_list.as_view(), name = "posts-cbv"),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>/', delete, name = "delete"),
    
    path('comment-create/<int:post_id>/', comment_create, name = "comment-create"),

    path('post-likes/<int:post_id>/<str:url>/', post_likes, name = "post-likes"),
    path('comment-likes/<int:post_id>/<int:comment_id>/', comment_likes, name = "comment-likes"),
]