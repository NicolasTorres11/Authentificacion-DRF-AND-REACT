<template>
    <div class="login">
      <h1>This is an login page</h1>
    </div>
    <div class="col-6 mx-auto">
        <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Username</label>
              <input type="text" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
              {{ username }}
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
            </div>
            <button type="submit" @click="submit($event)" class="btn btn-primary">Submit</button>
          </form> 
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    submit(e) {
      console.log(this.username);
      console.log(this.password);
      e.preventDefault();

      if (!this.username) {
        alert('Fill Username');
      }
      if (!this.password) {
        alert('Fill password');
      }

      const requestData = {
        username: this.username,
        password: this.password
      };

      axios
        .post('http://127.0.0.1:8000/api/token/', requestData)
        .then(response => {
          console.log(response.data.access);
          localStorage.setItem('token', response.data.access);
          window.location.href = '/';
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};


</script>

<style>


</style>