import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Admin_Register from '@/components/public/admin_register'  //管理员注册
import Stu_Register from '@/components/public/stu_register'  //学生注册
import Tea_Register from '@/components/public/tea_register'  //老师注册
import Main from '@/components/public/main' //主页
import VueCookie from 'vue-cookie'

Vue.use(VueCookie)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name:'Login',
      component:Login,

    },
    {
      path: '/admin_register',
      name: 'Admin_Register',
      component: Admin_Register,
    },
    {
      path: '/stu_register',
      name: 'Stu_Register',
      component: Stu_Register,
    },
    {
      path: '/tea_register',
      name: 'Tea_Register',
      component: Tea_Register,
    },
    {
      path:'/main',
      name:'Main',
      component:Main
    }
  ]
})
