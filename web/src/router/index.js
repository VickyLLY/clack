import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/schedule/login'  //登录
import Register from '@/components/schedule/register'  //注册
import Main from '@/components/schedule/main' //主页
import VueCookie from 'vue-cookie'
import main_mob from '@/components/schedule/main_mob'
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
      path: '/main_mob',
      name: 'main_mob',
      component: main_mob,
    },
    {
      path:'/main',
      name:'Main',
      component:Main
    }
  ]
})
