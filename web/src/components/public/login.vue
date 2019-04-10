<template>
  <div>
    <div class="login-wrap">
      <h3>登录</h3>
      <input type="text" placeholder="请输入用户名" v-model="username">
      <input type="password" placeholder="请输入密码" v-model="password">
      <button v-on:click="login">登录</button>
      <span v-on:click="register">没有账号？马上注册</span>
    </div>
  </div>
</template>

<style>
  .login-wrap{text-align:center;}
  input{display:block; width:250px; height:40px; line-height:40px; margin:0 auto; margin-bottom: 10px; outline:none; border:1px solid #888; padding:10px; box-sizing:border-box;}
  p{color:red;}
  button{display:block; width:250px; height:40px; line-height: 40px; margin:0 auto; border:none; background-color:#41b883; color:#fff; font-size:16px; margin-bottom:5px;}
  span{cursor:pointer;}
  span:hover{color:#41b883;}
</style>

<script>
  export default{
    data(){
      return{
        username: '',
        password: '',
      }
    },
    mounted() {
      if(this.$cookie.get('username'))
        this.$router.push({
          path: '/logout',
        })
    },
    methods: {
      login:function () {
        if (this.username == "" || this.password == "") {

          alert("请输入用户名或密码")
        } else {
          let data = {'user_name': this.username, 'user_password': this.password}
          /*接口请求*/
          this.$http.post(this.Global_Api+'/user/login', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("登录失败"+res.body.error_message)
            } else {
              //alert("登录成功")
              this.$cookie.set('username', this.username, 600);
              this.$cookie.set('user_token', res.body.user_token, 600);
              this.$cookie.set('user_type', res.body.user_type, 600);
              if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
                this.$router.push({
                  path: '/main_mob',
                })
                location.reload()
              }else{
                this.$router.push({
                  path: '/main',
                })
              }

              //location.reload()
            }
          })
        }
      },
      register:function () {
        this.$router.push('/register')
        location.reload()
      }
    }
  }
</script>
