import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import Receive from '@/views/Receive.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: {
        name: 'home'
      }
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/receive',
      name: 'receive',
      component: Receive
    }
  ]
})
