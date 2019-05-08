<template>
  <div>
    <h3>学生注册</h3>
    <input type="text" class="form-control" placeholder="请输入用户名" v-model="username" required="required">
    <br>
    <input type="password" class="form-control" placeholder="请输入密码" v-model="password" required="required">
    <br>
    <input type="password" class="form-control" placeholder="请确认密码" v-model="confirm_password" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入姓名" v-model="stu_name" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入学号" v-model="stu_number" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入邮箱" v-model="stu_email" required="required">
    <br>
    <div class="v_select">
      <v-select max-height="80px" placeholder="请选择入学年份" :options="start_year" v-model="stu_start_year"></v-select>
      <br>
      <v-select max-height="80px" placeholder="请选择毕业年份" :options="end_year" v-model="stu_end_year"></v-select>
      <br>
      <v-select max-height="80px" placeholder="请选择班级" :options="banji_name" v-model="stu_banji_name"></v-select>
    </div>
    <br>
    <button type="submit" class="btn btn-default" v-on:click="register">注册</button>
    <br>
  </div>
</template>

<script>
  var start = [];
  var end = [];
  for (var i = 2005; i <= 2020; i++)
    start.push(i);
  for (var i = 2009; i <= 2024; i++)
    end.push(i);
  export default {
    name: "stu_register",
    data() {
      return {
        banji_list: [],
        start_year: start,
        end_year: end,
        username: '',
        password: '',
        confirm_password: '',
        stu_name: '',
        stu_number: '',
        stu_email: '',
        stu_start_year: '',
        stu_end_year: '',
        stu_banji_id: '',
        banji_name: [],
        banji_name_to_id: {},
        stu_banji_name: ''
      }
    },
    mounted() {
      let data = {}
      this.$http.post(this.Global_Api + '/entity/banji_list', data).then((res) => {
        this.banji_list = res.body.banji_list
        for (let i = 0; i < this.banji_list.length; i++) {
          this.banji_name.push(this.banji_list[i].banji_name)
          this.banji_name_to_id[this.banji_list[i].banji_name] = this.banji_list[i].banji_id
        }
      })
    },
    methods: {
      register: function () {
        if (
          this.username === "" || this.password === "" || this.confirm_password === "" || this.stu_name === "" ||
          this.stu_number === "" || this.stu_email === "" || this.stu_start_year === "" || this.stu_end_year === "" || this.stu_banji_name === ""
        )
          alert("部分信息未填写")
        else {
          if (this.password !== this.confirm_password)
            alert("两次输入的密码不一致")
          else {
            this.stu_banji_id = this.banji_name_to_id[this.stu_banji_name]
            let data = {
              "user": {
                "user_name": this.username,
                "user_password": this.password
              },
              "student": {
                "student_name": this.stu_name,
                "student_number": this.stu_number,
                "student_email": this.stu_email,
                "student_start_year": parseInt(this.stu_start_year),
                "student_end_year": parseInt(this.stu_end_year),
                "student_banji_id": parseInt(this.stu_banji_id)
              }
            }
            this.$http.post(this.Global_Api + '/user/signup_student', data).then((res) => {
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
