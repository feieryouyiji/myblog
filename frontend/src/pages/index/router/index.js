/* eslint-disable */
// eslint-disable-next-line
import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/HelloWorld'
import Tag from '@/components/Tag'
import Category from '@/components/Category'
import Article from '@/components/Article'
import Book from '@/components/Book'

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
      path: '/tag',
      name: 'Tag',
      component: Tag
    }
    ,{
      path: '/category',
      name: 'Category',
      component: Category
    }
    ,{
      path: '/article',
      name: 'Article',
      component: Article
    }
    ,{
      path: '/book',
      name: 'Book',
      component: Book
    }
    ,{
      path: '*',
      name: 'Hello',
      component: Hello
    }
  ]
})
