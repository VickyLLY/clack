<template>
  <div>
    <div class="text-center">
      <h3>管理员注册</h3>
      <input type="text" class="form-control"  style="margin-left: auto;margin-right: auto;width:300px;" placeholder="请输入用户名" v-model="username" required="required">
      <br>
      <input type="password" class="form-control" style="margin-left: auto;margin-right: auto;width:300px;" placeholder="请输入密码" v-model="password" required="required">
      <br>
      <input type="password" class="form-control" style="margin-left: auto;margin-right: auto;width:300px;" placeholder="请确认密码" v-model="confirm_password" required="required">
      <br>
      <button type="submit" class="btn btn-default" v-on:click="register">注册</button>
      <br>
      <router-link to="/"><button class="btn btn-link">已有账号？马上登录</button></router-link>
    </div>
  </div>
</template>

<style>

</style>

<script>
  export default{
    data(){
      return{
        username: '',
        password: '',
        confirm_password:'',
      }
    },
    methods: {
      register:function () {
        if (this.username == "" || this.password == "" || this.confirm_password == "" || this.user_type == "")
          alert("下列信息不能为空")
        else {
          if (this.password != this.confirm_password)
            alert("两次输入的密码不一致")
          else {
              let data = {
                "user": {
                  'user_name': this.username,
                  'user_password': this.password,
                }
              }
            this.$http.post(this.Global_Api+'/user/signup_admin', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert(res.body.error_message)
              } else {
                alert("注册成功")
                this.$router.push('/')
              }
            })
          }
        }
      }
    }
  }
</script>
