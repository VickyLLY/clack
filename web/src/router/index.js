import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register' //注册
import Main from '@/components/public/main' //PC端主页
import VueCookie from 'vue-cookie'
import main_mob from '@/components/schedule/main_mob' //手机端主页
import schedule_mob from  '@/components/schedule/schedule_mob'
import news_mob from  '@/components/schedule/news_mob'
import edit_classroom from '@/components/background/edit_classroom'
import edit_major from '@/components/background/edit_major'
import edit_student from '@/components/background/edit_student'
import edit_department from '@/components/background/edit_department'
import edit_class from '@/components/background/edit_class'
import edit_teacher from '@/components/background/edit_teacher'


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
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/main_mob',
      name: 'main_mob',
      component: main_mob,
      meta: {
        keepAlive: true// 需要被缓存
      },
      children:[
        {
          path:'schedule_mob',
          component: schedule_mob,
          meta: {
            keepAlive: false // 需要被缓存
          },
        },
        {
          path:'news_mob',
          component: news_mob,
          meta: {
            keepAlive: false // 需要被缓存
          },
        }
      ]
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/main/edit_classroom',
      name: 'edit_classroom',
      component: edit_classroom,
    },
    {
      path: '/main/edit_major',
      name: 'edit_major',
      component: edit_major,
    },
    {
      path: '/main/edit_teacher',
      name: 'edit_teacher',
      component: edit_teacher,
    },
    {
      path: '/main/edit_student',
      name: 'edit_student',
      component: edit_student,
    },
    {
      path: '/main/edit_class',
      name: 'edit_class',
      component: edit_class,
    },
    {
      path: '/main/edit_department',
      name: 'edit_department',
      component: edit_department,
    },
  ]
})
