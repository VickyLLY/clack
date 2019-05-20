<!--<template>-->
<!--    <div>-->
<!--      <PC_bar></PC_bar>-->
<!--      <div>-->
<!--        <h3>答辩信息</h3>-->
<!--        <table class="table table-bordered">-->
<!--                  <tbody>-->
<!--          <tr>-->
<!--            <th>学生</th>-->
<!--                      <td>{{user_name}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>学号</th>-->
<!--                      <td>{{student_number}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>答辩时间</th>-->
<!--                      <td>{{data}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>答辩地点</th>-->
<!--                      <td>{{classroom}}</td>-->
<!--          </tr>-->
<!--                  </tbody>-->
<!--        </table>-->
<!--      </div>-->
<!--    </div>-->
<!--</template>-->

<!--<script>-->
<!--    import PC_bar from "../public/PC_bar";-->
<!--    export default {-->
<!--      name: "stu_def_view",-->
<!--      components: {-->
<!--        PC_bar-->
<!--      },-->
<!--    data()-->
<!--    {-->
<!--      return {-->
<!--        list: null,-->
<!--        user_name: this.$cookie.get('username'),-->
<!--        user_token: this.$cookie.get('user_token'),-->
<!--        student_number: this.$cookie.get('user_student_number')-->
<!--      }-->
<!--    },-->
<!--      methods:{-->
<!--        mounted(value){-->
<!--          let data = {-->
<!--            "user_name": this.user_name,-->
<!--            "user_token": this.user_token,-->
<!--            "student_number": this.student_number,-->
<!--            // "teacher_number":this.teacher_number,-->
<!--            "data": this.data,-->
<!--            "classroom": this.classroom-->
<!--          }-->
<!--          this.$http.post(this.Global_Api + '/background/design', data).then((res) => {-->
<!--            if (res.body.error_code !== 0) {-->
<!--              alert(res.body.error_message)-->
<!--            } else {-->
<!--              alert("查询结果")-->
<!--            }-->
<!--          })-->
<!--          // if(this.$cookie.get('username')==null)-->
<!--          //   this.$router.push('/')-->
<!--        }-->
<!--      }-->

<!--    }-->
<!--</script>-->

<!--<style scoped>-->
<!--  h3 {-->
<!--    text-align: center;-->
<!--  }-->
<!--  .table{-->
<!--    margin-left: 400px;-->
<!--    width: 800px;-->
<!--  }-->
<!--</style>-->

<template>
  <div>
    <PC_bar></PC_bar>
    <div>
      <h3>答辩信息</h3>
      <table class="table table-bordered">
        <tbody>
        <tr>
          <th>学生</th>
          <td>{{user_name}}</td>
        </tr>
        <tr>
          <th>学号</th>
          <td>{{student_number}}</td>
        </tr>
        </tbody>
        <tbody v-for="value in schedule">
        <tr>
          <th>答辩时间</th>
          <td>{{value.assign_date}}</td>
        </tr>
        <tr>
          <th>答辩地点</th>
          <td>{{value.assign_classroom_id}}</td>
        </tr>
        </tbody>
        <tbody v-for="v in tea_list">
        <tr>
          <th>教师工号</th>
          <td>{{v.teacher_number}}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  export default {
    name: "stu_def_view",
    components: {
      PC_bar
    },
    data()
    {
      return {
        list: null,
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        student_number: this.$cookie.get('user_student_number'),
        schedule:null,
        tea_list:null
      }
    },

      mounted(){
        let data = {
          "user_name": this.user_name,
          "user_token": this.user_token,
          "student_number": this.student_number,
        }
        this.$http.post(this.Global_Api + '/background/design', data).then((res) => {
          if (res.body.error_code !== 0) {
            alert(res.body.error_message)
          } else {
            this.schedule=res.body.result_list
            // alert("查询结果")
          }
        })
        this.$http.post(this.Global_Api + '/background/design_tea', data).then((res) => {
          if (res.body.error_code !== 0) {
            alert(res.body.error_message)
          } else {
            this.tea_list=res.body.result_list2
            // alert("查询结果")
          }
        })
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
