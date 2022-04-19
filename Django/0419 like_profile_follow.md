# 0419 오후 실습(오전내용 리마인드) 

### 05_django_model_relation_I



1. 가상환경 세팅 및 실행

   ```
   python -m venv venv
   source venv/Scripts/activate
   ```

2. pip install

   ```
   pip install -r requirements.txt
   ```

3. articles > models.py 수정 

   ```
   Article 클래스에 'like_users' 추가
   
   like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
   
   이때, related_name을 설정해주지 않으면, Article클래스에서 Comment 클래스를 역참조할때 오류가 발생하므로(역참조 할 때 매니저 이름이 같으므로) 꼭 설정해주어야 한다.
   
   
   # 사용할 수 있는 User - Article 간의 DB API
   # article.user : 게시글을 작성한 유저
   # article.like_users : 게시글에 좋아요를 누른 유저
   # user.article_set : 유저가 작성한 게시글들(역참조)
   # user.like_articles : 유저가 좋아요 누른 게시글들(역참조)
   ```

4.  models.py를 수정했으므로 다시 마이그레이션

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. 중간중간 서버를 켜서 확인

   ```
   python manage.py runserver
   ```

6. articles > urls.py 에 url 추가

   ```
   path('<int:article_pk>/likes', views.likes, name='likes'),
   ```

7. articles > views.py에 def likes 정의해주기

   ```
   @require_POST
   def likes(request,article_pk):
   	# 로그인을 했다면
       if request.user.is_authenticated:
       	# 좋아요를 누를 게시글 받아오기
           article = get_object_or_404(Article,pk=article_pk) # 데이터가 없을때 404 에러를 표시하기 위해
           # 좋아요 기능은 좋아요를 누르지 않은 상태에서 누르면 '좋아요'로 표시
           # 이미 좋아요를 누른 상태라면, '좋아요 취소'로 표시
           # 2가지로 구분하기 위해 if문 사용
           
           # get 대신 filter를 쓴 이유 : get은 데이터가 없으면 에러 발생
           # if request.user in article.like_users.all() : 가능하지만 밑에 코드가 더 빠름
           if article.like_users.filter(pk=request.user.pk).exists(): 
           	# 이미 좋아요를 눌렀을때 또 누르면 좋아요 취소되게끔
               article.like_users.remove(request.user)
           else:
           	# 좋아요를 누르지 않을 상태라서 누르면 좋아요가 되게끔
               article.like_users.add(request.user)
           
           return redirect('articles:index')
       # 로그인을 안한 상태라면 로그인 페이지로 redirect
       return redirect('accounts:login')
   ```

8. '좋아요' 표시할 icon 사용하기 위해 font-awesome에서 cdn 받아와서 base.html에 추가

   ```
   base.html
   
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
   
   ```

9. articles > templates > articles > index.html 수정

   ```
   <div>
   <form action="{% url 'articles:likes' article.pk %}" method="POST">
   {% csrf_token %}
   {% if user in article.like_users.all %}
   <button class="btn btn-link shadow-none">
   <i class="fa-solid fa-heart" style="color:red"></i>
   </button>
   {% else %}
   <button class="btn btn-link shadow-none">
   <i class="fa-regular fa-heart" style="color:black"></i>
   </button>
   {% endif %}
   </form>
   </div>
   
   좋아요 버튼 추가
   ```

10. articles > froms.py 에서 ArticleForm 클래스의 Meta 클래스의 exclude에 like_users추가

    ```
    exclude = ('user','like_users',)
    ```

11. accounts > urls.py 추가 (프로필)

    ```
    variable routing으로 str을 입력받으므로 95%이상확률로 맨 밑에 path링크를 작성해야함. 그렇지않으면 오류가 발생함. 다른 링크를 들어갈때 str로 먼저 입력받아서 기능을 제대로 수행못하게됨.
    
    
    path('<username>/', views.profile, name='profile'),
    
    ```

12. accounts > views.py 추가

    ```
    def profile(request,username):
        person = get_object_or_404(get_user_model(),username=username)
        context = {
            'person':person,
        }
        return render(request,'accounts/profile.html',context)
    ```

13. accounts > templates > accounts > profile.html 작성

    ```
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>{{ person.username }} 님의 프로필</h1>
      <hr>
      <h2> {{ person.username }}님의 게시글</h2>
      {% for article in person.article_set.all %}
        <div>
          <a href="{% url 'articles:detail' article.pk%}">{{ article.title }}</a>
        </div>
      {% endfor %}
      <hr>
      <h2> {{ person.username }} 님이 좋아요한 글</h2>
      {% for article in person.like_articles.all %}
        <div>
          <a href="{% url 'articles:detail' article.pk %}"> {{ article.title }}</a>
        </div>
      {% endfor %}
      <hr>
      <h2>{{ person.username}}님이 남긴 댓글</h2>
      {% for comment in person.commnet_set.all %}
        <div>
          <a href="{% url 'articles:detail' comment.article.pk%}">{{ comment.content }}</a>
        </div>
      {% endfor %}
    
      <hr>
      <a href="{% url 'articles:index' %}">BACK</a>
    {% endblock content %}
    ```

14. base.html에 프로필 링크 추가

    ```
    로그인했을때를 확인하는 코드 밑에
    <a href="{% url 'accounts:profile' user.username%}">[내 프로필]</a> 
    추가 작성
    ```

15. articles > templates > articles > index.html에 프로필 링크 추가

    ```
    <p>
        <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
    </p>
    ```

16. accounts > models.py 에 팔로우, 팔로워 기능추가

    ```
    User 클래스에 followings 추가 
    
    # A 유저는 여러 명의 Follower들을 가질 수 있다. (User <- User)
    # A 유저는 여러 명의 유저를 Following 할 수 있다. (User -> User)
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    ```

17. models.py를 수정했으므로 다시 마이그레이션

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

18. accounts  > urls.py 추가 ( 팔로우 기능)

    ```
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    ```

19. accounts > views.py 추가

    ```
    def follow(request,user_pk):
    	# 로그인을 했을때
        if request.user.is_authenticated:
            person = get_object_or_404(get_user_model(), pk=user_pk)
            # 자기 자신이 아니라면
            if person != request.user:
            	# 이미 팔로우 했다면
                if person.followers.filter(pk=request.user.pk).exists():
                    person.followers.remove(request.user)
                # 아직 팔로우 하지 않았다면
                else:
                    person.followers.add(request.user)
            return redirect('accounts:profile', person.username)
        # 로그인 하지 않은 상태라면 로그인페이지로
        return redirect('accounts:login')
    ```

20. accounts > templates > accounts > profile.html에 팔로우/ 언팔로우 버튼 작성

    ```
    {% with followings=person.followings.all followers=person.followers.all%}
        <div>
          팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
        </div>
    
        <div>
          {% if request.user != person %}
            <div>
              <form action="{% url 'accounts:follow' person.pk %}"metho="POST">
                {% csrf_token %}
                {% if request.user in followers %}
                  <button>Unfollow</button>
                {% else %}
                  <button>Follow</button>
                {% endif %}
              </form>
            </div>
          {% endif %}
        </div>
    {% endwith %}
    ```

21. gravatar를 활용해서 프로필 그림 넣기(없어도 될듯?)

    ```
    import urllib, hashlib
    
    # Set your variables here
    email = "lse2625@gmail.com"
    
    default = "https://www.example.com/default.jpg"
    size = 40
    
    m = hashlib.md5(email.encode('utf-8'))
    
    hashed_email = m.hexdigest()
    print(hashed_email)
    ```

22. accounts 앱에 templatetags 폴더 생성하고 `__init__.py` 와 `gravatar.py ` 생성

23. garvatar.py

    ```
    import urllib, hashlib
    from django import template
    
    register = template.Library()
    
    # gravatar default
    default = 'monsterid'
    
    # 2w. custom default
    
    default = 'https://newsimg.sedaily.com/2019/07/29/1VLVR41LYQ_1.jpg'
    
    @register.filter
    def get_gravatar(email, size=40):
        hashed_email = hashlib.md5(email.encode('utf-8').strip().lower()).hexdigest()
        query = f'size={size}&d={default}'
        return f'https://www.gravatar.com/avatar/{hashed_email}?{query}'
    ```

24. profile.html 에 img 태그 추가

    ```
    {% load gravatar %} <<< 꼭 추가,,,, 안하면 페이지 에러뜸
    
    <img src="{{ person.email | get_gravatar:50 }}" alt="gravatar-img">
    ```

    



