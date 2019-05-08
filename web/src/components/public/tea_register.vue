<template>
  <div>
    <h3>教师注册</h3>
    <input type="text" class="form-control" placeholder="请输入用户名" v-model="username" required="required">
    <br>
    <input type="password" class="form-control" placeholder="请输入密码" v-model="password" required="required">
    <br>
    <input type="password" class="form-control" placeholder="请确认密码" v-model="confirm_password" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入姓名" v-model="teacher_name" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入教师号" v-model="teacher_number" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入邮箱" v-model="teacher_email" required="required">
    <br>
    <div class="v_select">
      <department @listenToChild="get"></department>
    </div>
    <br>
    <button type="submit" class="btn btn-default" v-on:click="register">注册</button>
    <br>
  </div>
</template>

<script>
  import department from './department_list'

  export default {
    name: "tea_register",
    components: {
      department
    },
    data() {
      return {
        username: '',
        password: '',
        confirm_password: '',
        teacher_name: '',
        teacher_number: '',
        teacher_email: '',
        department_id: '',
      }
    },
    methods: {
      get(val) {
        this.department_id = val
      },
      register: function () {
        if (
          this.username === "" || this.password === "" || this.confirm_password === "" || this.teacher_name === "" ||
          this.teacher_number === "" || this.teacher_email === "" || this.department_name === ""
        )
          alert("信息未填写完全")
        else {
          if (this.password !== this.confirm_password)
            alert("两次输入的密码不一致")
          else {
            let data = {
              "user": {
                "user_name": this.username,
                "user_password": this.password
              },
              "teacher": {
                "teacher_name": this.teacher_name,
                "teacher_number": this.teacher_number,
                "teacher_email": this.teacher_email,
                "teacher_department_id": parseInt(this.department_id)
              }
            }
            this.$http.post(this.Global_Api + '/user/signup_teacher', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert(res.body.error_message)
              } else {
                alert("注册成功")
                this.$router.push('/')
              }
            })
          }
        }
      },
    }
  }
</script>

<style>

</style>
