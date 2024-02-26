from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta(): # Django에서 모델에 대한 추가적인 메타데이터를 제공
        model = get_user_model() # 폼이 연결된 모델 지정 
        fields = ['username', 'email', 'nickname', 'profile'] # 폼에 표시될 필드를 지정
