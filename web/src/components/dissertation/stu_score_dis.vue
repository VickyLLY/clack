<template>
  <div>
    <PC_bar></PC_bar>
    <div>
      <h3>毕业设计最终成绩</h3>
      <table class="table table-bordered">
                <tbody v-for="value in list">
<!--        <tr>-->
        <tr>
          <th>指导教师评语</th>
<!--          <td>333</td>-->
                    <td>{{value.comment}}</td>
        </tr>

        <tr>
          <th>最终成绩</th>
<!--          <td>555</td>-->
                    <td>{{value.grade}}</td>
        </tr>
                </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  export default {
    name: "stu_score_dis",
    components: {
      PC_bar
    },
    data(){
      return{
        list:null,
        comment:'',
        grade:'',

        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        // student_number: this.$cookie.get('student_number')
      }
    },
    mounted: function(){
      let data = {
        "user_name": this.user_name,
        "user_token": this.user_token,
        // "student_number":this.student_number,
        // "comment":this.comment,
        // "grade":this.grade,
      };
      this.$http.post(this.Global_Api + '/dst/stu_view_grade', data).then((res) => {

        if (res.body.error_code !== 0) {
          alert(res.body.error_message)
        } else {
          this.list = res.body.stu_view_grade;
          alert("查询结果")
        }
      })
      // if(this.$cookie.get('username')==null)
      //   this.$router.push('/')
    }
  }
</script>

<style scoped>
  h3 {
    text-align: center;
  }
  .table{
    margin-left: 200px;
    width: 800px;
  }
</style>
