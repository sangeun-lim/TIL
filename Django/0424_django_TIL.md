# 0425 시험대비 (REST API)

1. 가상환경 세팅

   ```
   python -m venv venv
   source venv/Scripts/activate
   
   pip install django djangorestframework django-extensions ipython django-seed psycopg2
   pip freeze > requirements.txt
   ```

2. 프로젝트 생성 및 앱 생성

   ```
   django-admin startproject my_api .
   python manage.py startapp myapps
   ```

3. 프로젝트의 settings.py에서 앱 등록

   ```
   INSTALLED_APPS = [
       'myapps',
       'rest_framework',
       'django_seed',
       'django_extensions',
       ...
   ]
   ```

4. 프로젝트의 urls.py 수정

   ```
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
   	path('admin/', admin.site.urls),
   	path('api/first/', include('myapps.urls')),
   ]
   ```

5. myapps/urls.py

   ```
   from django.urls import path
   from . import views
   
   urlpatterns =[
   
   ]
   ```

6. myapps/models.py

   ```
   from django.db import models
   
   class Myapp(models.Model):
   	title = models.CharField(max_length=100)
   	content = models.TextField()
   	created_at = models.DateTimeField(auto_now_add=True)
   	updated_at = models.DateTimeField(auto_now=True)
   ```

7. models.py에 변경사항이 생겼으므로 터미널에서 명령어 입력

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

8. 페이크 데이터 만들기

   ```
   python manage.py seed myapps --number=20
   ```

9. Serializers

   ```
   # myapps/serializers.py
   
   from rest_framework import serializers
   from .models import Myapp
   
   class MyappListSerializer(serializers.ModelSerializer):
   
   	class Meta:
   		model = Myapp
   		fields = '__all__'
   ```

10. urls.py

    ```
    urlpatterns = [
    	path('myapps/', views.myapps_list),
    ]
    ```

11. views.py

    ```
    from django.shortcuts import get_list_or_404
    from .serializers import MyappListSerializer
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    from .models import Myapp
    
    @api_view(['GET'])
    def myapps_list(request):
    	myapps = get_list_or_404(Myapp)
    	serializer = MyappListSerializer(myapps, many=True)
    	return Response(serializer.data)
    ```

12. serializer.py

    ```
    class MyappSerializer(serializers.ModelSerializer):
    
    	class Meta:
    		model = Myapp
    		fields = '__all__'
    ```

13. urls.py

    ```
    urlpatterns = [
    	path('myapps/', views.myapps_list),
    	path('myapps/'<int:myapp_pk>/',views.myapp_detail),
    ]
    ```

14. views.py

    ```
    @api_view(['GET'])
    def myapp_detail(request, myapp_pk):
    	myapp = get_object_or_404(Myapp, pk=myapp_pk)
    	serializer = MyappSerializer(myapp)
    	return Response(serializer.data)
    ```

15. myapp_list에 POST로 들어올때 경우

    ```
    from rest_framework import status
    
    @api_view(['GET','POST'])
    def myapps_list(request):
    	if request.method == 'GET':
            myapps = get_list_or_404(Myapp)
            serializer = MyappListSerializer(myapps, many=True)
            return Response(serializer.data)
            
        elif request.method == 'POST':
        	serializer = MyappSerializer(data=request.data)
        	if serializer.is_valid(raise_exception=True):
        		serializer.save()
        		return Response(serializer.data, status=status.HTTP_201_CREATED)
        		
    ```

16. myapp_detail 에서 PUT(수정) 및 DELETE(삭제) 추가

    ```
    @api_view(['GET','PUT','DELETE'])
    def myapp_detail(request, myapp_pk):
    	myapp = get_object_or_404(Myapp, pk=myapp_pk)
    	if request.method == 'GET':
            serializer = MyappSerializer(myapp)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
        	serializer = MyappSerializer(instance=myapp, data=request.data)
        	if serializer.is_valid(raise_exception=True):
        		serializer.save()
        		return Response(serializer.data)
        
        elif request.method == 'DELETE':
        	myapp.delete()
        	data = {
        		'delete': f'{myapp_pk}번이 삭제.'
        	}
        	return Response(data, status=status.HTTP_204_NO_CONTENT)
    ```

    