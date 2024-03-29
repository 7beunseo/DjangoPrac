from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from uuid import uuid4
from django.utils import timezone

# uuid라는 고유 식별자 생성기를 통해서 파일 경로의 중복을 막음 
def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=20, unique=True)
    profile = models.ImageField(upload_to=upload_filepath, blank=True)

    def __str__(self):
        return f'{self.username}'
    
class FollowManager(models.Manager):
    def check_follow_status(self, follower, following):
        return self.get_queryset().filter(follower=follower, following=following)

    
class Follow(models.Model):
    follower = models.ForeignKey(to="User", related_name = "follower", on_delete = models.CASCADE) # 팔로우 ㅏ는 사람
    following = models.ForeignKey(to="User", related_name = "following", on_delete = models.CASCADE) # 팔로우 받는 사람 

    objects = FollowManager()

    