import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register'  //注册
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
      path: '/register',
      name: 'Register',
      component: Register,
    },
    {
      path:'/main',
      name:'Main',
      component:Main
    }
  ]
})
