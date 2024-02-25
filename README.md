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
* posts 앱 내 메서드 생성, 구체적인 로직 작성 
* templates 폴더를 만든 후 view에서 지정한 템플릿 생성 (index.html)
* posts 앱 내 urls.py 생성 및 view 연결
    ```python
    from django.urls import path
    from .views import *; # 현재 경로 views.py의 모든 메서드를 불러옴 

    urlpatterns = [
        path('', index, name = "index"),
    ]
    ```

