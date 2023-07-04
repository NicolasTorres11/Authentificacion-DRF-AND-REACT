<template>
  <div class="home">
    <div class="col-6 mx-auto">
      <div class="form-group d-flex">
        <input class="form-control" v-model="ToDo" placeholder="Enter Model" type="text">
        <button class="btn btn-success" @click="createToDo()">Create</button>
      </div>
      <ul class="list-group">
        <li class="list-group-item" v-for="todos in ToDo" :key="todos.uid">{{ todos.todo_models }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HomeView',
  
  data() {
    return {
      ToDo: [],
    };
  },
  methods: {
    createdToDo() {
      this.getToDo()
    },

    getToDo() {
      const token = localStorage.getItem('token');

      axios.get('http://127.0.0.1:8000/todo/api/', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        }
      })
        .then(response => {
          console.log('Response:', response); // Verificar la respuesta completa del servidor
          console.log('Response Data:', response.data); // Verificar los datos recibidos

          this.todos = response.data;
          console.log('Todos:', this.todos); // Verificar que los datos se asignen correctamente
        })
        .catch(error => {
          console.error('Error:', error); // Verificar cualquier error de la solicitud
        });
    },

    createToDo() {
      const token = localStorage.getItem('token');

      const requestData = {
        todo_models: this.todo
      };

      axios.post('http://127.0.0.1:8000/todo/api/', requestData, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        }
      })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
