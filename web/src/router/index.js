import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register' //注册
import Main from '@/components/public/main' //PC端主页
import Add_course from '@/components/schedule/add_course'
import VueCookie from 'vue-cookie'
import main_mob from '@/components/mob/main_mob' //手机端主页
import schedule_mob from  '@/components/mob/schedule_mob'
import test from '@/components/mob/test'
import bar_mob from '@/components/mob/bar_mob'
Vue.use(VueCookie)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path:'/test',
      component: test,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/main_mob',
      name: 'main_mob',
      component: main_mob,
    },
    {
      path: '/bar_mob',
      component: bar_mob,
    },
    {
      path:'/schedule_mob',
      component: schedule_mob,
    },
    {
      path: '/main',
      name: 'Main',
      component: Main,
    },
    {
      path:'/main/add_course',
      name:'Add_course',
      component:Add_course,
    }
  ]
})