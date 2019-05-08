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
Vue.prototype.Global_Api = Api.Global_Api
Vue.config.productionTip = false

/* eslint-disable no-new */
var app = new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})





