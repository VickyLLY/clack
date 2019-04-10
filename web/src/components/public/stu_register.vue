<template>
  <div>
      <h3>学生注册</h3>
      <input type="text" class="form-control"  placeholder="请输入用户名" v-model="username" required="required">
      <br>
      <input type="password" class="form-control" placeholder="请输入密码" v-model="password" required="required">
      <br>
      <input type="password" class="form-control" placeholder="请确认密码" v-model="confirm_password" required="required">
      <br>
      <input type="text" class="form-control" placeholder="请输入姓名" v-model="stu_name" required="required">
      <br>
      <input type="text" class="form-control" placeholder="请输入学号" v-model="stu_number" required="required">
      <br>
      <input type="text" class="form-control"  placeholder="请输入邮箱" v-model="stu_email" required="required">
      <br>
      <div style="height: 100px">
      <v-select max-height="80px" style="width:300px;" placeholder="请选择入学年份" :options="start_year"  v-model="stu_start_year"></v-select>
        <v-select max-height="80px" style=";width:300px;" placeholder="请选择毕业年份" :options="end_year"  v-model="stu_end_year"></v-select>
      </div>
        <input type="text" class="form-control"  placeholder="请输入班级" v-model="stu_banji_id" required="required">
      <br>
      <button type="submit" class="btn btn-default" v-on:click="register">注册</button>
      <br>
      <router-link to="/"><button class="btn btn-link">已有账号？马上登录</button></router-link>
  </div>
</template>

<script>
    var start = [];
    var end = [];
    for(var i=2005;i<=2020;i++)
      start.push(i);
    for(var i=2009;i<=2024;i++)
      end.push(i);
    export default {
        name: "stu_register",
      data(){
          return{
            start_year:start,
            end_year:end,
            username:'',
            password:'',
            confirm_password:'',
            stu_name:'',
            stu_number:'',
            stu_email:'',
            stu_start_year:'',
            stu_end_year:'',
            stu_banji_id:''
          }
      },
      methods:{
          register:function () {
            if (
              this.username == "" || this.password == "" || this.confirm_password == "" || this.stu_name == "" ||
              this.stu_number == "" || this.stu_email == "" || this.stu_start_year == "" || this.stu_end_year == "" || this.stu_banji_id==""
            )
              alert("下列信息不能为空")
            else {
              if (this.password != this.confirm_password)
                alert("两次输入的密码不一致")
            }
          },
      }
    }
</script>
<style >

  h3{
    text-align: center;
  }
  input.form-control{
    display:block;
    margin:0 auto;
    width:300px;
  }
  v-select{

  }
  button.btn{
    display:block;
    margin:0 auto;
    width:300px;
  }
</style>
