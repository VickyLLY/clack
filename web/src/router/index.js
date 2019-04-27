import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register' //注册
import Main from '@/components/public/main' //PC端主页
import Add_course from '@/components/schedule/add_course'
import Arrange_course from '@/components/schedule/arrange_course'
import VueCookie from 'vue-cookie'
<<<<<<< HEAD
import main_mob from '@/components/schedule/main_mob' //手机端主页
import schedule_mob from  '@/components/schedule/schedule_mob'
import news_mob from  '@/components/schedule/news_mob'
import stu_sel_course from "@/components/select_course/stu_sel_course"
import tea_sel_course from "@/components/select_course/tea_sel_course"
import man_sel_course from "@/components/select_course/man_sel_course"
=======
import test from '@/components/mob/test'
import bar_mob from '@/components/mob/bar_mob'
>>>>>>> 5772c1f48958d257633d26d12805fcbda726e1d8
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
<<<<<<< HEAD
      component: Main
    },

=======
    {
      path:'/main/add_course',
      name:'Add_course',
      component:Add_course,
    },
    {
      path:'/main/arrange_semester',
      name:'Arrange_course',
      component:Arrange_course
>>>>>>> 5772c1f48958d257633d26d12805fcbda726e1d8
    },
  {
    path: '/stu_sel_course',
    name: 'stu_sel_course',
    component: stu_sel_course
  },
  {
    path: '/tea_sel_course',
    name: 'tea_sel_course',
    component: tea_sel_course
  },
  {
    path: '/man_sel_course',
    name: 'man_sel_course',
    component: man_sel_course
  }
  ],

})
