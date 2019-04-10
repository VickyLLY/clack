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
Vue.use(Resource)
Vue.prototype.PC_Api=Api.PC_Api //登录接口
Vue.prototype.Mobile_Api=Api.Mobile_Api //登录接口
Vue.config.productionTip = false

/* eslint-disable no-new */
var app = new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})





