/* eslint-disable */
// eslint-disable-next-line
import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/HelloWorld'
import First from '@/components/first'
import Two from '@/components/two'
import Three from '@/components/three'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    }
    ,{
      path: '/first',
      name: 'First',
      component: First
    }
    ,{
      path: '/two',
      name: 'Two',
      component: Two
    }
    ,{
      path: '/three',
      name: 'Three',
      component: Three
    }
    ,{
      path: '*',
      name: 'Hello',
      component: Hello
    }
  ]
})
