<template>
<div class="wrapper">
    <v-form
      ref="form"
      class="add-todo-form"
    >
      <v-text-field
        :counter="40"
        label="Title"
        required
        outlined
        v-model="title"
      ></v-text-field>

      <v-text-field
        label="Content"
        required
        outlined
        v-model="content"
      ></v-text-field>

    <v-text-field
      type="date" 
      label="end date (required)"
      v-model="end_date"
      >
     </v-text-field>
     <v-text-field 
      type="color" 
      label="Color (click to open)"
      mode="hexa"
      v-model="color"
      >
        Pick a color
     </v-text-field>

      <v-btn @click.prevent="addTodo()" type="submit" color="primary">
        Add Todo
      </v-btn>

  </v-form>
  <div class="container">



    <swiper class="swiper" :options="swiperOption" >
      <swiper-slide
        :key="todo.id"
        v-for="todo in todos"
        :style="{background: todo.color}"
      >
      <div class="todo-wrapper">
        <h1 class="todo-title">
          {{ todo.title }}
        </h1>
        <p class="todo-content">
          {{ todo.description }}
        </p>

        <div class="dates-wrapper">
          <h4>
           Start date: {{ todo.start_date.substring(0, 10) }}
          </h4>
          <h4>
            End date: {{ todo.end_date }}
          </h4>
        </div>

        <div class="buttons-wrapper">
          <form>

            <div class="my-2" v-if="todo.completed">
            <v-btn 
              :id="todo.id" 
              type="submit" 
              color="success"
              @click.prevent="toggleCompleted(todo.id)"
              >
              Completed
            </v-btn>
            </div>

            <div class="my-2" v-else>
            <v-btn 
              @click.prevent="toggleCompleted(todo.id)"
              type="submit">
              Mark Complete
             </v-btn>
            </div>
          </form>

          <div class="my-2">
            <v-btn color="error" @click.prevent="deleteTodo(todo.id)">Delete</v-btn>
          </div>
        </div>
      </div>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </div>
</div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import "../assets/css/ListView.css"
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

Vue.use(axios);

console.clear();

export default {
name: "ListView",

title: '3D Coverflow effect',
components: {
  Swiper,
  SwiperSlide
},

data(){
  return{
    todos: [],
    dialog: false,
    swiperOption: {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows : true 
      },
      pagination: {
      el: '.swiper-pagination'
      },
    },
    title: null,
    content: null,
    color: "#20aaee",
    end_date: null,
  }
},

created(){
  this.getTodos();
},

methods:{
  async getTodos(){
    let res = await axios.get(
      "http://localhost:8000/api/todos/"
    );
    let data = res.data;
    this.todos = data;
    console.log(data);
    },

    async toggleCompleted(id){
      let isComplete
      this.todos.forEach(todo =>{
        if(todo.id === id){
          isComplete = !todo.completed
        }
      })
      let req = {
        url: `http://localhost:8000/api/todos/${id}/`,
        method: "PATCH",
        data: {
          completed: isComplete,
        },
      };  
      await axios(req);
      this.getTodos();
    },

    async deleteTodo(id){
      let req = {
        url: `http://localhost:8000/api/todos/${id}/`,
        method: "DELETE",
      };
      await axios(req);
      this.getTodos();
    },

    async addTodo(){
      let req = {
        url: `http://localhost:8000/api/todos/`,
        method: "POST",
        data:{
          title: this.title,
          description:this.content,
          end_date: this.end_date,
          color: this.color,
          completed: false
        }
      };
      await axios(req);
      this.getTodos();

      this.title = ""
      this.content = ""
      this.end_date = ""
      this.color = ""
      }
  },
}
</script>

<style lang="scss" scoped>
.wrapper{
  background: #eee;
  text-align: center;
}

.add-todo-form{
  margin-top: 3em;
  width: 50%;
  display: inline-block;
}

.buttons-wrapper{
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.container{
  border-radius: 5px;
  padding-top: 3em;
  margin-top: 2em;
  height: 40vh;
  background: rgb(255, 255, 255);
  filter: drop-shadow(0 0 10px rgba(71, 71, 71, 0.349));
}

.todo-container{
  margin-top: 1em !important;
}


.swiper {
    height: 100%;
    width: 100%;

   

    .swiper-pagination {
      .swiper-pagination-bullet.swiper-pagination-bullet-active {
        background-color: white;
      };
    };
  };
   .swiper-slide {
      text-align: left;
      width: 400px;
      height: 250px;
      font-weight: bold;
      font-size: 1rem;
      background-color: rgb(29, 148, 218);
      background-position: center;
      background-size: cover;
      color: white;
      padding: 1em;
      border-radius: 10px;
      transition-duration: 0.5s;
      transition: ease-in-out;
    }

</style>