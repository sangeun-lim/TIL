# Vuex를 활용한 Todo 앱 만들기

1. vue create todo

2. cd todo

3. npm run serve

4. components 폴더에 `TodoForm.vue` , `TodoList.vue` , `TodoListItem.vue` 컴포넌트 생성

5. App.vue 틀 잡기

   ```vue
   <template>
     <div id="app">
       <h1>Todo List</h1>
       <h2>전체 Todo 개수</h2>
       <h2>완료한 Todo 개수</h2>
       <h2>완료 X 개수</h2>
       <hr>
       <todo-form></todo-form>
       <hr>
       <todo-list></todo-list>
     </div>
   </template>
   
   <script>
   import TodoForm from '@/components/TodoForm.vue'
   import TodoList from '@/components/TodoList.vue'
   
   
   export default {
     name: 'App',
     components: {
       TodoForm, TodoList
     },
   }
   </script>
   
   <style>
   #app {
     font-family: Avenir, Helvetica, Arial, sans-serif;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-align: center;
     color: #2c3e50;
     margin-top: 60px;
   }
   </style>
   
   ```

6. TodoForm.vue 작성하기( 객체 생성, actions로 넘기고,  넘긴내용 초기화시키기)

   ```vue
   <template>
     <div>
       <h3>Todo 입력 영역</h3>
       <input type="text" v-model.trim='todoTitle'>
       <button @click='createTodo'>ADD TODO</button>
     </div>
   </template>
   
   <script>
   export default {
     name: 'TodoForm',
     data() {
       return { 
         todoTitle: '',
       }
     },
     methods : {
       // todo 객체의 생성
       createTodo() {
         const todoItem = {
           title: this.todoTitle,
           isCompleted : false,
           data: new Date().getTime()
         }
       
       // if 오른쪽의 유효성 검사를 위해서 v-model.trim 연관지어 생각
       if (todoItem.title) {
         this.$store.dispatch('createTodo', todoItem)
       }
       // 사이클 끝난 후 초기화
       this.todoTitle = ''
       }
     }
   }
   </script>
   
   <style>
   
   </style>
   ```

7. TodoForm.vue에서 넘겨준 것을 받을 index.js 작성하기

   ```javascript
   import Vue from 'vue'
   import Vuex from 'vuex'
   
   Vue.use(Vuex)
   
   export default new Vuex.Store({
     state: {
       todos : []
     },
     getters: {
     },
     mutations: {
       CREATE_TODO(state, todoItem) {
         state.todos.push(todoItem)
         // console.log(state)
         // console.log(state.todos)
       },
     },
     actions: {
       // 제일 먼저 받아주는 곳 
       // createTodo({commit}, todoItem) ???
       createTodo(context, todoItem) {
         context.commit('CREATE_TODO', todoItem)
       }
     },
     // modules: {
     // }
   })
   
   ```

8. TodoList.vue 틀일 잡기

   ```vue
   <template>
     <div>
       <todo-list-item 
       v-for='todo in todos'
       :key='todo.date'
       :todo='todo'> <!-- props 부분 -->  <!-- :내려갈 이름='실제값' -->
       </todo-list-item>
       <!-- {{ $store.state.todos }} 직접 X -->
     </div>
   </template>
   
   <script>
   import TodoListItem from '@/components/TodoListItem.vue'
   
   export default {
     name: 'TodoList',
     components: {
       TodoListItem
     },
     computed: {
       todos() {
         return this.$store.state.todos
       }
     }
   
   }
   </script>
   
   <style>
   
   </style>
   ```

9. TodoListItem.vue 에 props 가져오기 및 컴포넌트 내용 작성

   ```vue
   <template>
     <div>
       <span>{{ todo.title }}</span>
       <button>삭제</button>
     </div>
   </template>
   
   <script>
   export default {
     name: 'TodoListItem',
     props: {
       // [ {}, {}, {} ]가 v-for 돌려져서 나온 값이 obj!
       todo:Object,
     },
     methods: {
       // delete -> 버튼 눌렀을 때
   
       // update -> span 태그를 눌렀을 때 취소선 
     }
   }
   </script>
   
   <style>
   
   </style>
   ```

10. index.js에 [delete , update]  actions추가 

    ```js
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        todos : []
      },
      getters: {
      },
      mutations: {
        CREATE_TODO(state, todoItem) {
          state.todos.push(todoItem)
          // console.log(state)
          // console.log(state.todos)
        },
        DELETE_TODO(state, todoItem) {
    
        },
        UPDATE_TODO_STATUS(state, todoItem){
    
        }
      },
      actions: {
        // 제일 먼저 받아주는 곳 
        // createTodo({commit}, todoItem) ???
        createTodo(context, todoItem) {
          context.commit('CREATE_TODO', todoItem)
        },
        deleteTodo({commit}, todoItem) {
          commit('DELETE_TODO', todoItem)
        },
        updateTodo(context, todoItem) {
          context.commit('UPDATE_TODO_STATUS', todoItem)
        },
      },
      // modules: {
      // }
    })
    
    ```

11. TodoListItem의 methods에서 deleteTodo() 함수 작성 및 버튼에 연결

    ```
    <template>
      <div>
        <span>{{ todo.title }}</span>
        <button @click='deleteTodo'>삭제</button>
      </div>
    </template>
    
    <script>
    export default {
      name: 'TodoListItem',
      props: {
        // [ {}, {}, {} ]가 v-for 돌려져서 나온 값이 obj!
        todo:Object,
      },
      methods: {
        // delete -> 버튼 눌렀을 때
        deleteTodo(){
          this.$store.dispatch('deleteTodo', this.todo)
      }
        // update -> span 태그를 눌렀을 때 취소선
        
      }
    }
    </script>
    
    <style>
    
    </style>
    ```

12. index.js에 actions와 mutations 작성하기 

    ```js
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        todos : []
      },
      getters: {
      },
      mutations: {
        CREATE_TODO(state, todoItem) {
          state.todos.push(todoItem)
          // console.log(state)
          // console.log(state.todos)
        },
        DELETE_TODO(state, todoItem) {
          // 1. 현재 payload의 인덱스 찾아야함 
          const index = state.todos.indexOf(todoItem)
          // 2. 걔만 싹 도려냄 => 원본 변화
          state.todos.splice(index,1)
    
        },
        // UPDATE_TODO_STATUS(state, todoItem){
    
        // }
      },
      actions: {
        // 제일 먼저 받아주는 곳 
        // createTodo({commit}, todoItem)로 받아서 써도 됨
        createTodo(context, todoItem) {
          context.commit('CREATE_TODO', todoItem)
        },
        deleteTodo({commit}, todoItem) {
          commit('DELETE_TODO', todoItem)
        },
        // updateTodo(context, todoItem) {
        //   context.commit('UPDATE_TODO_STATUS', todoItem)
        // },
      },
      // modules: {
      // }
    })
    ```

13. TodoListItem.vue에서 update 함수 랑 style 작성 및 span 태그 연결

    ```vue
    <template>
      <div>
        <!-- 클래스 v-bind -> 참이되는 경우 class ON!  -->
        <span @click="updateTodoStatus"
          :class="{'is_completed' : todo.isCompleted}">{{ todo.title }}
        </span>
        <button @click='deleteTodo'>삭제</button>
      </div>
    </template>
    
    <script>
    export default {
      name: 'TodoListItem',
      props: {
        // [ {}, {}, {} ]가 v-for 돌려져서 나온 값이 obj!
        todo:Object,
      },
      methods: {
        // delete -> 버튼 눌렀을 때
        deleteTodo(){
          this.$store.dispatch('deleteTodo', this.todo)
        },
        // update -> span 태그를 눌렀을 때 취소선
        updateTodoStatus(){
          this.$store.dispatch('updateTodo', this.todo)
        }
      }
    }
    </script>
    
    <style scoped>
    /* 취소선의 css 구현 */
      .is_completed {
        text-decoration: line-through;
      }
    </style>
    ```

14. index.js에서 actions와 mutations 작성( update 부분 )

    ```js
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        todos : []
      },
      getters: {
      },
      mutations: {
        CREATE_TODO(state, todoItem) {
          state.todos.push(todoItem)
          // console.log(state)
          // console.log(state.todos)
        },
        DELETE_TODO(state, todoItem) {
          // 1. 현재 payload의 인덱스 찾아야함 
          const index = state.todos.indexOf(todoItem)
          // 2. 걔만 싹 도려냄 => 원본 변화
          state.todos.splice(index,1)
        },
    
        // 1개를 찾고 망냑 그게 타켓이라면,
        // isCompleted를 반전
        UPDATE_TODO_STATUS(state, todoItem){
          state.todos = state.todos.map(todo => {
            if (todo === todoItem) {
              return {
                ...todo,     // title : todoItem.title,
                isCompleted: !todo.isCompleted
              }
            } else {
              return todo
            }
          })
        }
      },
      actions: {
        // 제일 먼저 받아주는 곳 
        // createTodo({commit}, todoItem)로 받아서 써도 됨
        createTodo(context, todoItem) {
          context.commit('CREATE_TODO', todoItem)
        },
        deleteTodo({commit}, todoItem) {
          commit('DELETE_TODO', todoItem)
        },
        updateTodo(context, todoItem) {
          context.commit('UPDATE_TODO_STATUS', todoItem)
        },
      },
      // modules: {
      // }
    })
    ```

    여기까지 하면 추가 / 삭제 / 줄긋기까지 완성

15. index.js의 getters 작성 ( 할일관련 개수 세기 위해서 )

    ```js
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        todos : []
      },
      getters: {
        allTodosCount(state){
          return state.todos.length
        },
        completedTodosCount(state){
          return state.todos.filter(todo => {
            return todo.isCompleted === true
          }).length
        },
        uncompletedTodosCount(state){
          return state.todos.filter(todo => {
            return todo.isCompleted === false
          }).length
        }
      },
      mutations: {
        CREATE_TODO(state, todoItem) {
          state.todos.push(todoItem)
          // console.log(state)
          // console.log(state.todos)
        },
        DELETE_TODO(state, todoItem) {
          // 1. 현재 payload의 인덱스 찾아야함 
          const index = state.todos.indexOf(todoItem)
          // 2. 걔만 싹 도려냄 => 원본 변화
          state.todos.splice(index,1)
        },
    
        // 1개를 찾고 망냑 그게 타켓이라면,
        // isCompleted를 반전
        UPDATE_TODO_STATUS(state, todoItem){
          state.todos = state.todos.map(todo => {
            if (todo === todoItem) {
              return {
                ...todo,     // title : todoItem.title,
                isCompleted: !todo.isCompleted
              }
            } else {
              return todo
            }
          })
        }
      },
      actions: {
        // 제일 먼저 받아주는 곳 
        // createTodo({commit}, todoItem)로 받아서 써도 됨
        createTodo(context, todoItem) {
          context.commit('CREATE_TODO', todoItem)
        },
        deleteTodo({commit}, todoItem) {
          commit('DELETE_TODO', todoItem)
        },
        updateTodo(context, todoItem) {
          context.commit('UPDATE_TODO_STATUS', todoItem)
        },
      },
      // modules: {
      // }
    })
    
    ```

16. App.vue 의 template랑 computed 작성

    ```vue
    <template>
      <div id="app">
        <h1>Todo List</h1>
        <!-- <h2>전체 Todo 개수: {{ allTodos }}</h2> -->
        <h2>전체 Todo 개수: {{ allTodosCount }}</h2>
        <h2>완료한 Todo 개수: {{ completedTodosCount }}</h2>
        <h2>완료 X 개수: {{ uncompletedTodosCount }}</h2>
        <hr>
        <todo-form></todo-form>
        <hr>
        <todo-list></todo-list>
      </div>
    </template>
    
    <script>
    import TodoForm from '@/components/TodoForm.vue'
    import TodoList from '@/components/TodoList.vue'
    // 1. 일단 바인딩 헬퍼를 가져온다.
    import {mapGetters} from 'vuex'
    
    export default {
      name: 'App',
      components: {
        TodoForm, TodoList
      },
      computed : {
        // allTodos() {
        //   return this.$store.getters.allTodosCount
        // }
        ...mapGetters([
        'allTodosCount', 
        'completedTodosCount', 
        'uncompletedTodosCount' ])
      }
    }
    </script>
    
    <style>
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
    }
    </style>
    
    ```

17. Map 활용하기 ( TodoListItem.vue 수정 )

    ```vue
    <template>
      <div>
        <!-- 클래스 v-bind -> 참이되는 경우 class ON!  -->
        <!-- 기본적으로 mapActions 안쓸때 문법 -->
        <!-- <span @click="updateTodoStatus"
          :class="{'is_completed' : todo.isCompleted}">{{ todo.title }}
        </span> -->
        <span @click="updateTodo(todo)"
          :class="{'is_completed' : todo.isCompleted}">{{ todo.title }}
        </span>
        <!-- 기본적으로 mapActions 안쓸때 문법 -->
        <!-- <button @click='deleteTodo'>삭제</button> -->
        <button @click='deleteTodo(todo)'>삭제</button>
        <!-- 이게 실행이 절대 아님 -->
        <!-- 마치 문법은 deleteTodo -> paylod:todo 인것임 -->
      </div>
    </template>
    
    <script>
    import { mapActions } from 'vuex'
    
    export default {
      name: 'TodoListItem',
      props: {
        // [ {}, {}, {} ]가 v-for 돌려져서 나온 값이 obj!
        todo:Object,
      },
      methods: {
        // delete -> 버튼 눌렀을 때
        // deleteTodo(){
        //   this.$store.dispatch('deleteTodo', this.todo)
        // },
        // update -> span 태그를 눌렀을 때 취소선
        // updateTodoStatus(){
          // this.$store.dispatch('updateTodo', this.todo)
        // }
        ...mapActions(['deleteTodo', 'updateTodo'])
      }
    }
    </script>
    
    <style scoped>
    /* 취소선의 css 구현 */
      .is_completed {
        text-decoration: line-through;
      }
    </style>
    ```

18. Local Storage ==>  vuex-persistedstate

    - 터미널에  npm i vuex-persistedstate 설치

19. index.js 수정

    ```js
    import createPersistedState from 'vuex-persistedstate'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      plugins: [
        createPersistedState()
      ],
    ```

    새로고침을 새로 데이터가 삭제되지 않음.

    그런데 사이트가 제대로 뜨지 않는다면, Application의 Storage에서 value가 null일 때 에러뜨므로 delete하고 다시 새로고침하면 잘 됨



