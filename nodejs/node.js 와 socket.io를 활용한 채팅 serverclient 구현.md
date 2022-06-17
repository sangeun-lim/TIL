### node.js 와 socket.io를 활용한 채팅 server/client 구현 

1.  node.js 다운

2. cmd 명령어로

   ```
   mkdir chat && cd chat
   npm init --yes
   npm install --save --save-exact socket.io express
   ```

3. 같은 폴더내에 server.js 파일 작성

   ```js
   const { join } = require('path');
   
   var app = require('express')();
   var http = require('http').Server(app);
   var io = require('socket.io')(http);
   
   // client가 최초 접속 시 보여지는 화면
   app.get('/', function(req, res){
     res.sendFile(__dirname + '/index.html');
   });
   
   // 서버 실행
   http.listen(3000, function(){
     console.log('server listening on port : 3000');
   });
   
   var userList = [];
   
   io.on('connection', function(socket){
     // console.log('a user connected');
     var joinedUser = false;
     var nickname;
   
   //유저 입장
   socket.on('join', function(data){
     console.log(data);
     if (joinedUser) { // 이미 입장 했다면 중단
       return false;
     }
   
     nickname = data;
     userList.push(nickname);
     socket.broadcast.emit('join', {
       nickname : nickname,
       userList : userList
     });
   
     socket.emit('welcome', {
       nickname : nickname,
       userList : userList
     });
   
     joinedUser = true;
   });
   
   // 메시지 전달
   socket.on('msg', function(data){
     console.log('msg: ' + data);
     io.emit('msg', {
       nickname : nickname,
       msg : data
     });
   });
   
   // 접속 종료
   socket.on('disconnect', function() {
     // 입장하지 않았다면 중단
     if ( !joinedUser){
       console.log(' --- not joinedUser left');
       return false;
     }
     // 접속자 목록에서 제거
     var i = userList.indexOf(nickname);
     userList.splice(i,1);
     
     socket.broadcast.emit('left', {
       nickname : nickname,
       userList : userList
       });
     });
   });
   ```
   
4.  index.html 파일도 작성
   
   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Socket.IO chat</title>
       <style>
         * { margin: 0; padding: 0; box-sizing: border-box;}
         body { font: 13px Helvetica, Arial;}
         form { background: #000; padding: 3px; position: fixed; bottom: 0; width: 100%; }
         form input { border: 0; padding: 10px; width: 90%; margin-right: .5%;}
         form button { width: 9%; background: rgb(130,224,255); border:none; padding: 10px;}
         #messages { list-style-type: none; margin: 0; padding: 0;}
         #messages li {padding:5px 10px;}
         #messages li:nth-child(odd) { background: #eee;}
         #messages span.nickname { font-weight: bold; font-size: 120%; display: inline-block; width: 100px;}
   
         div.userList {text-align: center; width: 200px; min-height: 200px; border: 1px solid #999;}
         #userList{ list-style-type: none; margin: 0; padding: 0;}
         
         #before {text-align: center; margin-top: 50%;}
         #after{display: none;}
         .noti{text-align: center; color: blue;}
       </style>
     </head>
     <body>
   
       <section id="before">
         <p>닉네임을 입력하세요</p>
         <input id="nickname"><button id="joinBtn">들어가기</button>
       </section>
       
       <section id="after">
         <div class="userList">
           <h2>현재 접속자</h2>
           <ul id="userList"></ul>
         </div>
   
         <hr>
         <ul id="messages"></ul>
         <form>
           <input id="m" autocomplete="off" /><button>Send</button>
         </form>
       </section>
       
       <script src="socket.io/socket.io.js"></script>
       <script src="http://code.jquery.com/jquery-1.11.1.js"></script>
       <script>
         var nickname;
         var socket = io();
   
         // 이벤트: join 클릭
         $('#joinBtn').click(function(e){
           fnNickname(e);
         });
   
         // 이벤트: nickname 엔터키
         $('#nickname').keypress(function(e) {
           if (e.which == 13) {
             fnNickname(e);
           }
         });
   
         // 송신: 닉네임
         function fnNickname(e){
           if ($('#nickname').val().trim() == '') {
             alert('Input your nickname!');
             return false;
           }
           nickname = $('#nickname').val().trim();
           socket.emit('join', nickname); // 접속이벤트
         }
   
         // 수신: 인사
         socket.on('welcome', function(data){
           //유저리스트 업데이트
           fnUpdateUserList(data.userList);
   
           $('#before').hide();
           $('#after').show();
           $('#messages').append($('<li class="noti">').text(nickname + '님 환영합니다.'));
         });
   
         // 유저리스트 업데이트
         function fnUpdateUserList(userList){
           $('#userList').text('');
           for (i = 0; i < userList.length; i++){
             $('#userList').append($('<li>').text(userList[i]));
           };
         }
   
         // 수신: 신규 유저 접속
         socket.on('join', function(data){
           //입장 알림
           $('#messages').append($('<li class="noti">').text(data.nickname + '님이 입장하셨습니다.'));
   
           // 유저리스트 업데이트
           fnUpdateUserList(data.userList);
         });
   
         // 수신: 퇴장
         socket.on('left', function(data){
           //입장 알림
           $('#messages').append($('<li class="noti">').text(data.nickname + '님이 퇴장하셨습니다.'));
   
           // 유저리스트 업데이트
           fnUpdateUserList(data.userList);
         });
   
         // 송신 : 메시지
         $('form').submit(function(){
           socket.emit('msg', $('#m').val());
           $('#m').val('');
           return false;
         });
   
         // 수신 : 메시지
         socket.on('msg', function(data){
           var span = $('<span class="nickname">').text(data.nickname);
           var li = $('<li>').append(span).append(data.msg);
           $('#messages').append(li);
         });
       </script>
     </body>
   </html>
   ```
   
   
   
4. node 명령어로 서버를 실행한 뒤 http://localhost:3000으로 여러 창을 띄워서 채팅 확인
   
   ```
   node server.js
   ```
   
   
   
   
   
   
   
   
   
   