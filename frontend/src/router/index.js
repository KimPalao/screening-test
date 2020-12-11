import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Values from '../views/Values.vue';
import Principles from '../views/Principles.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/values',
    name: 'Values',
    component: Values,
  },
  {
    path: '/principles',
    name: 'Principles',
    component: Principles,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
