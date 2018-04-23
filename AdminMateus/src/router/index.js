import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Galeria from '@/components/Galeria'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path:'/galeria',
      name: 'Galeria',
      component: Galeria
    },
    { 
      path: '*', 
      component: Home 
    }    
  ]
})
