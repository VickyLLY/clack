// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Resource from 'vue-resource'
import Api from './router/Api'  //导入全局接口
import $ from 'jquery'   //引入jQuery
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import '../node_modules/bootstrap/dist/js/bootstrap.min'
import vSelect from 'vue-select'

Vue.component('v-select', vSelect)
Vue.use(Resource)
Vue.prototype.Global_Api=Api.Global_Api
Vue.config.productionTip = false

// 以下后台管理系统用

// 引入axios
import axios from 'axios'
// 引入vuex
import Vuex from 'vuex'
// 引入element-ui
import ElementUi from'element-ui'
// 引入样式
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false

// 创建过滤器
Vue.filter('formatter',function(value){
  if(value === true){
    return '启用'
  }
  return '停用'
})
// 使用vuex
Vue.use(Vuex)
// 使用element-ui
Vue.use(ElementUi)
// 创建一个vuex的实例
const store = new Vuex.Store({
  // state存放数据的地方
  state:{

  },
  // getter也是存放数据的地方，但是这里跟state的区别主要在于getter中用于计算后的结果
  getter:{

  },
  // 用于改变状态的地方
  mutations:{

  },
  // 也是用于改变状态的地方，但是通常用于异步改变
  actions:{

  },
  // 模块
  modules:{

  }
})

// 以上后台管理系统用

/* eslint-disable no-new */
var app = new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})





