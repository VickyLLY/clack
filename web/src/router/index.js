import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register' //注册
import Main from '@/components/public/main' //PC端主页

//成绩管理
import Stu_navigation from '@/components/scoremng/stu_scoremng/Stu_navigation'
import Stu_score from '@/components/scoremng/stu_scoremng/stu_score'
import Stu_complain from '@/components/scoremng/stu_scoremng/stu_complain'

import Add_course from '@/components/schedule/add_course'
import Arrange_course from '@/components/schedule/arrange_course'
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
    },
    {
      path:'/main/arrange_semester',
      name:'Arrange_course',
      component:Arrange_course
    },
    //成绩管理
    {
      path:'/main/stu_navigation',
      name:'Stu_navigation',
      component:Stu_navigation,
      children: [
            {
              path:'stu_score',
              name:'stu_score',
              component:Stu_score
            },
            {
              path:'stu_complain',
              name:'stu_complain',
              component:Stu_complain
            }
          ]
    }
  ]
})
