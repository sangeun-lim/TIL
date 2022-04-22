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

- ModelSerializer

  - 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut
  - 핵심 기능은 다음과 같다
    - 모델 정보에 맞춰 자동으로 필드 생성
    - serializer에 대한 유효성 검사기를 자동으로 생성
    - .create() & .update()의 간단한 기본 구현이 포함됨
  - `many` argument
    - many=True
      - Serializing multiple objects
      - 단일 인스턴스 대신 QuerySet 등을 직렬화하기 위해서는 serializer를 인스턴스화 할 때 many=True를 키워드 인자로 전달해야함

- 