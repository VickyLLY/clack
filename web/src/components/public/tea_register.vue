<template>
  <div>
    <h3>教师注册</h3>
    <input type="text" class="form-control"  placeholder="请输入用户名" v-model="username" required="required">
    <br>
    <input type="password" class="form-control" placeholder="请输入密码" v-model="password" required="required">
    <br>
    <input type="password" class="form-control" placeholder="请确认密码" v-model="confirm_password" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入姓名" v-model="stu_name" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入教师号" v-model="stu_number" required="required">
    <br>
    <input type="text" class="form-control"  placeholder="请输入邮箱" v-model="stu_email" required="required">
    <br>
    <input type="text" class="form-control"  placeholder="请输入学院" v-model="stu_banji_id" required="required">
    <br>
    <button type="submit" class="btn btn-default" v-on:click="register">注册</button>
    <br>
  </div>
</template>

<script>
    export default {
        name: "tea_register"
    }
</script>

<style scoped>

</style>
