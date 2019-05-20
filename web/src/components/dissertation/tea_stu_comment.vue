<template>
  <div>
    <PC_bar></PC_bar>
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>学号</th>
        <th>名称</th>
        <th>专业</th>
        <th>附件</th>
        <th>操作</th>
      </tr>
      </thead>
      <tbody v-for="d_a in list">
      <tr>
        <td>{{d_a.student_number}}</td>
        <td>{{d_a.student_name}}</td>
        <td>{{d_a.major_name}}</td>
        <td><button type="button" @click="download">下载</button></td>
        <td><button type="button" @click="comment(d_a.student_number)">评价</button></td>
      </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
    import PC_bar from "../public/PC_bar";
    export default {
        name: "tea_stu_comment",
      components: {PC_bar},
      data()
      {
        return{
          user_name: this.$cookie.get('username'),
          user_token: this.$cookie.get('user_token'),
          dissertation_id:this.$route.query.dissertation_id,
          list:[],
        }
      },
      mounted(){
        let data = {
          "dissertation_id":this.dissertation_id,
          "user_name": this.user_name,
          "user_token": this.user_token,
        }
      this.$http.post(this.Global_Api + '/dst/view_determination', data).then((res) =>{
        // if (res.body.error_code !== 0) {
        //   alert("error!  " + res.body.error_message)
        // }else
        // {
          this.list =  res.body.stu_list
          if(this.list.length===0)
            alert("无学生")
        // }
      })
    },
    methods:
    {
      download: function(student_number){
        let data ={'student_number':student_number,'username':this.username,'user_token':this.user_token};
        this.$http.post(this.Global_Api + '/dst/download', data).then((res) =>{
            alert("下载成功")
            })
      },
      comment: function(student_number){
        this.$router.push({
          path: '/main/tea_comment',
          query: {
            'student_number': student_number,
            'dissertation_id': this.dissertation_id,
          }
        })
      }
    }
    }
</script>

<style scoped>

</style>
