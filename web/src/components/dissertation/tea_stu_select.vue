<template>
  <div>
    <PC_bar></PC_bar>
  <div>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>学号</th>
        <th>姓名</th>
        <th>专业</th>
        <th  v-if="flag===3">操作</th>
      </tr>
      </thead>
      <tbody v-for="d_a in list">
      <tr>
        <td>{{d_a.student_number}}</td>
        <td>{{d_a.student_name}}</td>
        <td>{{d_a.major_name}}</td>
        <td v-if="flag===3"><button type="submit"  @click="select_this(d_a.student_number)">选择</button></td>
      </tr>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script>
    import PC_bar from "../public/PC_bar";
    export default {
        name: "tea_stu_select",
      components: {PC_bar},
      data(){
        return{
          user_name: this.$cookie.get('username'),
          user_token: this.$cookie.get('user_token'),
          dissertation_id:this.$route.query.dissertation_id,
          flag:this.$route.query.flag,
          list:null,
          ss:''
        }
      },
      mounted(){
          let data = {
            "dissertation_id":this.dissertation_id,
            "user_name": this.user_name,
            "user_token": this.user_token,
          }
      this.$http.post(this.Global_Api + '/dst/view_student', data).then((res) =>{
        if (res.body.error_code !== 0) {
          alert("error!" + res.body.error_message)
        }else{
          this.list =  res.body.stu_list
          if(this.list.length===0)
            alert("无学生")
        }
      })
      },
      methods:{
          select_this:function(student_number){
            let data = {
                'dissertation_number': parseInt(this.dissertation_id),
                'student_number': parseInt(student_number),
                'user_name':this.user_name,
                'user_token':this.user_token,
              }
            this.$http.post(this.Global_Api + '/dst/define_stu', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("选择失败" + res.body.error_message)
              } else {
                alert("选择成功")
                location.reload()
              }
            })
        }
      }
    }
</script>

<style scoped>

</style>
