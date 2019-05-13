<template>
  <div>

    <div>
      <div class="year_semester">
        <input type="text" class="form-control"  placeholder="学年" v-model="year" required="required">
      </div>
      <div class="year_semester">
        <input  type="text" class="form-control"  placeholder="学期" v-model="semester" required="required">
      </div>
      <div class="year_semester">
        <button class="btn btn-default" type="submit" @click="stu_find_score">确认</button>
      </div>
    </div>


    <br><br><br>

    <div>

      <table class="table table-bordered">
        <thead>
        <tr>
          <th>课程名</th>
          <th>课程学分</th>
          <th>课程类型</th>
          <th>分数</th>
          <th>课程评价</th>
          <th>提交评价</th>
        </tr>
        </thead>
        <tbody v-for="(each,index) in list">
          <tr>
            <td>{{each.course_name}}</td>
            <td>{{each.course_credit}}</td>
            <td>{{each.course_type}}</td>
            <td>{{each.score}}</td>
            <td><textarea class="form-control" placeholder="课程评价" v-model="evaluation[index]"></textarea></td>
            <td><button class="btn btn-sm" type="submit" @click="submit_evaluation(each,index)">确认提交</button></td>
          </tr>
        </tbody>
      </table>

    </div>



  </div>
</template>

<script>
    export default {
      name: "stu_evaluation",
      data() {
        return {
          student_number: null,
          list: null,
          year: '',
          semester: '',
          evaluation:[],
        }
      },
      methods: {
        stu_find_score: function () {
          if (this.year == "" || this.semester == "") {
            alert("请选择学年和学期")
          } else {
            let data = {
              'year': this.year,
              'semester': this.semester,
              'student_number': this.$cookie.get('user_student_number')
            };
            /*接口请求*/
            this.$http.post(this.Global_Api + '/scoremng/student_check_scores/', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              } else {
                this.list = res.body.score_list;
                if(this.list.length === 0){
                  alert("这个学期没有课程！");
                }
              }
            });
          }
        },
        submit_evaluation:function (each,index) {
          if(this.evaluation[index] != ""){
            let data = {
              'course_name':each.course_name,
              'course_credit':each.course_credit,
              'course_year':this.year,
              'course_semester':this.semester,
              'score':each.score,
              'course_comment':this.evaluation[index],
              'student_number': this.$cookie.get('user_student_number'),
            };
            //alert(this.evaluation[index]);
            /*接口请求*/
            this.$http.post(this.Global_Api + '/scoremng/courses_comment/', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              } else {
                alert("评价成功！");
              }
            });
          }
          else{
            alert("请填写评价！");
          }
        },
      },

    }
</script>

<style scoped>
  .year_semester{
    float:left;
    margin-left:30px;
  }
</style>

