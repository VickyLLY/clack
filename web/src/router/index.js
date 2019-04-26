import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register' //注册
import Main from '@/components/public/main' //PC端主页
import VueCookie from 'vue-cookie'
import main_mob from '@/components/schedule/main_mob' //手机端主页
import schedule_mob from  '@/components/schedule/schedule_mob'
import news_mob from  '@/components/schedule/news_mob'
import stu_sel_course from "@/components/select_course/stu_sel_course"
import tea_sel_course from "@/components/select_course/tea_sel_course"
import man_sel_course from "@/components/select_course/man_sel_course"
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
  ]
})
