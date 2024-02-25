### 📌가상환경 생성
```bash
 python -m venv venv
 ```

 ### 📌가상환경 실행
 ```bash
 source venv/Scripts/activate
 ```

 ### 📌 Django 설치
 ```bash
 pip install django
 ```

### 📌 프로젝트 생성 
```bash
django-admin startproject djangoPrj .
```
* 뒤에 .을 붙일 경우 : 현재 디렉토리 내에 새 Django 프로젝트를 생성
* 뒤에 .을 붙이지 않을 경우 : 프로젝트 디렉토리를 만들고, 해당 프로젝트 디렉토리 안에 새로운 Django 프로젝트를 생성


### 📌 서버 돌리기
```bash
python manage.py runserver
```

### 📌 앱 생성
```bash
python manage.py startapp posts
```
* `settings.py`의 `INSTALLED_APPS`에 등록한 앱 추가

#### 💫 앱 생성 시 진행해야 하는 절차
* url 연결
    ```python
    path('', include('posts.urls')), # '' 경로에 posts/urls.py와 연결 
    ```
* 앱 내 메서드 생성, 구체적인 로직 작성 
* templates 폴더를 만든 후 view에서 지정한 템플릿 생성 (index.html)
* 앱 내 urls.py 생성 및 view 연결
    ```python
    from django.urls import path
    from .views import *; # 현재 경로 views.py의 모든 메서드를 불러옴 

    urlpatterns = [
        path('', index, name = "index"),
    ]
    ```
### 📌 SuperUser 생성
```bash
 python manage.py createsuperuser
```

### 📌 Model 작성
* 앱 내 models.py에 작성
  ```python
  class <모델명>(models.Model):
    # 필드 작성
  ```
* 모델을 정의한 후 데이터베이스에 모델 반영
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### 📌 admin 등록
```python
admin.site.register(<모델명>)
```

* admin 페이지에 보일 내용 수정
```python
def __str__(self):
    return f'[{self.id}] {self.title}' # self.필드명
```

### 📌 CBV vs FBV
```python
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
```

#### 💫 cbv 방식 주의점
* 기능에 맞는 view 임포트 필요 
    ```python
    from django.views.generic import ListView, DetailView
    ```
* url 연결 시 as_view() 작성 
    ```python
    path('posts-cbv/', cbv_list.as_view(), name = "posts-cbv"),
    ```
* list
    * `앱명/모델명_list.html`
    * `모델명_list` 로 쿼리 사용 (ex {% for post in post_list %})
* detail
    * `앱명/모델명_detail.html`
    * `모델명` 로 쿼리 사용 (ex {% post.id %})