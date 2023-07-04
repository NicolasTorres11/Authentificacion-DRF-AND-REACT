import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import LoginView from '../views/LoginView.vue'

/*
const save = function (to, from, next){
  if(localStorage.getItem('token')){
    next
  }else{
    next('/login')
  }
}
*/

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
/*
    beforeEnter: (to, from, next) => {
      save(to, from, next)
    }
  */
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
