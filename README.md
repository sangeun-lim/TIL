----

### **Today I Learned**

---

- 2022-01-05 ~
- 공부한 내용을 기록할 예정입니다.

---

### 참고 자료

----

- pull test

---

- startcamp

  - Day1

    - CLI
    - markdown 작성법
    - git / github에 관해

  - Day2

    - github 계정 생성

    - git 과 github 연동

    - git 명령어

      ```
      $ git add "파일명"
      $ git commit -m "커밋 메시지"
      $ git push -u origin master
      ```

    - git clone & pull 

      ```
      $ git clone 주소 
      ```

      - clone을 통해 생성된 로컬 저장소는 `git init`과 `git remote add`가 이미 수행되어 있습니다. 

    - git pull 

      - 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어

      - 로컬 저장소와 원격 저장소의 내용이 완전 일치하면 git pull해도 변화가 일어나지 않습니다.

      - `git pull <저장소 이름> <브랜치 이름>`의 형태로 작성합니다.

        ```
        $ git pull origin master
        
        [풀이]
        git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다(pull).
        ```

        

