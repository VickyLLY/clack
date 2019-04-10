<template>
  <div>
  <nav class="navbar navbar-default navbar-fixed-top">
    <a class="navbar-brand"><strong>教务管理系统</strong></a>
    <ul class="nav navbar-nav">
      <li><a href="">排课子系统</a></li>
      <li><a href="">选课子系统</a></li>
      <li><a href="">后台管理子系统</a></li>
      <li><a href="">毕业设计管理子系统</a></li>
      <li><a href="">成绩管理子系统</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li class="col-md-7">
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
          {{username}}
          <b class="caret"></b>
        </a>
        <ul class="dropdown-menu">
          <li><a href="#">修改个人信息</a></li>
          <li><a href="#/" @click="quit">注销</a></li>
        </ul>
      </li>
    </ul>
  </nav>
  </div>
</template>

<script>
    export default {
        name: "main",
      data(){
          return{
            username:this.$cookie.get('username')
          }
      },
      methods:{
          quit:function () {
            this.$cookie.delete('username');
          }
      }

    }

</script>

<style>

</style>
