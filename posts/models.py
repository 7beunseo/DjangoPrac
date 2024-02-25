from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length = 50) # 글의 제목
    content = models.TextField(null = True) # 본문
    created_at = models.DateTimeField(auto_now_add = True) # 레코드 생성 시각으로 자동 저장
    modified_at = models.DateTimeField(auto_now=True) # 레코드가 저장될 때마다 현재 시간 갱신 
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # User 다대일 관계 

    def __str__(self):
        return f'[{self.id}] {self.title}'
    