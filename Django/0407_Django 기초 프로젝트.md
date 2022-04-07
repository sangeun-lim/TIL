# Django 기초 프로젝트

1. 가상 환경 만들기

   ```
   python -m venv venv
   ```

2. 가상 환경 실행

   ```
   source venv/Scripts/activate
   ```

3. 장고 or 필요한 프로그램 설치

   ```
   pip install django==3.2.12
   
   or
   
   pip install -r requirement.txt (협업할때 txt 파일이 있다면, 환경을 맞춰주기 위해)
   ```

4. 프로젝트 생성

   ```
   django-admin startproject <프로젝트명> .
   ```

5. 앱생성 후 앱 등록

   ```
   python manage.py startapp 앱이름(복수형태로)
   
   그리고 만들어준 프로젝트의 setting.py로 가서 INSTALLED_APPS에 가서 앱 등록
   ```

6. 서버 실행해보기

   ```
   python manage.py runserver
   ```

7. setting.py 수정

   ```
   프로젝트와 앱과 같은 위치에 templates 폴더 생성하고, 모든 템플릿에서 상속받아 사용할 base.html 작성
   
   setting.py의 TEMPLATES의 DIR에 BASE_DIR / 'templates' 추가
   ```

8. 프로젝트의 urls.py 수정

   ```
   여러 앱을 사용할 경우 그 앱에서 urls.py를 연결해서 실행되게끔 
   프로젝트의 urls.py는 include를 사용
   
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
   ]
   ```

9. 앱의 urls.py (메인페이지 경로 설정)

   ```
   from django.urls import path
   from . import views
   
   app_name = 'articles'
   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

10. views.py (index 구성 (뼈대만)

    ```
    from django.shortcuts import render
    from .models import Article
    
    def index(request):
    
        return render(request, 'articles/index.html')
    ```

11. 앱의 models.py

    ```
    from django.db import models
    
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return f'{self.pk} - {self.title}'
    ```

12. 마이그레이션 해주기

    ```
    터미널에서
    
    python manage.py makemigrations
    python manage.py migrate
    ```

13. admin.py (관리자 페이지)

    ```
    from django.contrib import admin
    from .models import Article
    
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ['pk', 'title', 'created_at', 'updated_at', 'content']
    
    admin.site.register(Article, ArticleAdmin)
    
    파일 만들어 준후
    
    터미널에서 python manage.py createsuperuser
    ```

14. 새로운 페이지를 만들때마다 

    ```
    urls.py , views.py, 새로운페이지.html 수정 및 생성 
    ```

15. forms.py

    ```
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
    
        class Meta:
            model = Article
            fields = '__all__'
            # exclude = ['content',]
    ```

16. views.py 에 import 추가

    ```
    from .forms import ArticleForm
    ```

17. urls.py 내용 추가

    ```
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
        path('create/', views.create, name='create'),
        path('<int:pk>/', views.detail, name='detail'),
        path('<int:pk>/update', views.update, name='update'),
        path('<int:pk>/delete', views.delete, name='delete'),
    ]
    
    ```

18. index.html

    ```
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Articles</h1>
      <a href="{% url 'articles:create' %}">CREATE</a>
      <hr>
      {% for article in articles %}
        <p>글 번호: {{ article.pk }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
        <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
        <hr>
      {% endfor %}
    {% endblock content %}
    ```

19. create.html

    ```
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>CREATE</h1>
      <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit", value="CREATE">
      </form>
      <hr>
      <a href="{% url 'articles:index' %}">BACK</a>
    {% endblock content %}
    ```

20. update.html

    ```
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>UPDATE</h1>
      <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit", value="UPDATE">
      </form>
      <hr>
      <a href="{% url 'articles:detail' article.pk %}">BACK</a>
    {% endblock content %}
    ```

21. detail.html

    ```
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Detail</h1>
      <h3>{{ article.title }}</h3>
      <p>{{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
      <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <button class="btn btn-light">DELETE</button>
      </form>
      <a href="{% url 'articles:index' %}">BACK</a>
    {% endblock content %}
    ```

22. forms.py 수정

    ```
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        title = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Enter the title'
                }
            )
        )
    
        class Meta:
            model = Article
            fields = '__all__'
            # exclude = ['content',]
    ```

23. views.py 수정

    ```
    from django.shortcuts import redirect, render
    from .models import Article
    from .forms import ArticleForm
    
    def index(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index.html', context)
    
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else :
            form = ArticleForm()
        context = {
            'form' : form,
        }
        return render(request, 'articles/create.html', context)
    
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    
    def update(request,pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else :
            form = ArticleForm(instance=article)
        context = {
            'form' : form,
            'article' : article,
        }
        return render(request, 'articles/update.html', context)
    
    def delete(request,pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
        return redirect('articles:detail', article.pk)
    ```

    