# 0420 Django_json_DRF

- django-seed 라이브러리를 사용해서 모델 구조에 맞는 데이터를 생성할수 있다!

  ```
  python manage.py migrate
  python manage.py seed articles --number=20
  ```

  - fake-data가 필요할때 활용

- Serialization

  - 직렬화
  - 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  - Django에서 쓰임 ==> Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환 할 수 있는 Python 데이터 타입으로 만들어 줌

- Django REST framework(DRF) 라이브러리를 사용한 JSON 응답

  ```
  pip install djangorestframework 로 설치 후
  settings.py에 'rest_framework' 앱 등록
  ```

- 