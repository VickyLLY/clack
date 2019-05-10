<template>
  <div>
    <div class="login-wrap">
      <h3 style="margin: 20px">登录</h3>
        <div class="input-group" >
          <span class="input-group-addon glyphicon glyphicon-user demo"></span>
          <input type="text" placeholder="请输入用户名" class="form-control" v-model="username">
        </div>
        <div class="input-group">
          <span class="input-group-addon glyphicon glyphicon-lock demo"></span>
          <input type="password" placeholder="请输入密码"class="form-control" v-model="password">
        </div>

      <button class="login" v-on:click="login">登录</button>
      <button class="btn btn-link" @click="register">没有账号？马上注册</button>
    </div>
  </div>
</template>

<style scoped>
  *{
    outline: 0;
    margin: 0 auto;
  }
  .glyphicon{
    position: static;
  }
  .login-wrap {
    text-align: center;
  }
  .form-control{
    width: 250px;
  }
  .input-group {
    margin-bottom:5px;
    left: 50%;
    margin-left: -145px;
  }
  input {
    display: block;
    width: 250px;
    height: 40px;
    line-height: 40px;
    margin: 0 auto;
    margin-bottom: 10px;
    outline: none;
    border: 1px solid #888;
    padding: 10px;
    box-sizing: border-box;
  }

  p {
    color: red;
  }

  button.login {
    display: block;
    width: 288px;
    height: 40px;
    line-height: 40px;
    margin: 0 auto;
    border: none;
    background-color: #41b883;
    color: #fff;
    font-size: 16px;
    margin-bottom: 5px;
    border-radius: 5px;
  }

</style>

<script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      }
    },
    mounted() {
      if (this.$cookie.get('username'))
        if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
          this.$router.push({
            path: '/main_mob',
          })
          location.reload()
        } else {
          this.$router.push({
            path: '/main',
          })
        }
    },
    methods: {
      login: function () {
        if (this.username == "" || this.password == "") {
          alert("请输入用户名或密码")
        } else {
          let data = {'user_name': this.username, 'user_password': this.password}
          /*接口请求*/
          this.$http.post(this.Global_Api + '/user/login', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("登录失败" + res.body.error_message)
            } else {
              //alert("登录成功")

              this.$cookie.set('username', this.username, 600);
              this.$cookie.set('user_token', res.body.user_token, 600);
              this.$cookie.set('user_type', res.body.user_type, 600);

              if (res.body.user_type === 1) {
                this.$cookie.set('realname', res.body.teacher.teacher_name, 600);
                this.$cookie.set('user_teacher_number', res.body.teacher.teacher_number, 600);
              } else if (res.body.user_type === 2) {
                this.$cookie.set('realname', res.body.student.student_name, 600);
                this.$cookie.set('user_student_number', res.body.student.student_number, 600);
              } else {
                this.$cookie.set('realname', this.username, 600);
              }
              if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
                this.$router.push({
                  path: '/main_mob',
                })
                location.reload()
              } else {
                this.$router.push({
                  path: '/main',
                })
              }
            }
          })
        }
      },
      register: function () {
        this.$router.push('/register')
      }
    }
  }
</script>
