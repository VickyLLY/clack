<template>
  <div>
    <div class="choose">
      <input type="radio" name="type" @click="type='student'">
      <label>学生</label>
      <input type="radio" name="type" @click="type='teacher'">
      <label>教师</label>
      <input type="radio" name="type" @click="type='admin'">
      <label>管理员</label>
    </div>
    <transition name="component-fade" mode="out-in">
      <component v-bind:is="type"></component>
    </transition>
    <router-link to="/">
      <button class="btn btn-link">已有账号？马上登录</button>
    </router-link>
  </div>
</template>

<script>
  import student from './stu_register'
  import teacher from './tea_register'
  import admin from './admin_register'

  export default {
    name: "register",
    data() {
      return {
        type: '',
      }
    },
    components: {
      student: student,
      teacher: teacher,
      admin: admin
    }
  }
</script>

<style>
  .component-fade-enter-active, .component-fade-leave-active {
    transition: opacity .3s ease;
  }

  .component-fade-enter, .component-fade-leave-to
    /* .component-fade-leave-active for below version 2.1.8 */
  {
    opacity: 0;
  }

  h3 {
    text-align: center;
  }

  div.choose {
    text-align: center;
    margin-top: 50px;
  }

  div.v_select {
    display: block;
    margin: 0 auto;
    width: 300px;
  }

  input.form-control {
    display: block;
    margin: 0 auto;
    width: 300px;
  }

  button.btn {
    display: block;
    margin: 0 auto;
    width: 300px;
  }
</style>
