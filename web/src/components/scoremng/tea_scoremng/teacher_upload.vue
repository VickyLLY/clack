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
        <button class="btn btn-default" type="submit" @click="tea_find_stu">确认</button>
      </div>
    </div>

    <br><br><br>

    <div>
      <table class="table table-bordered">
        <thead>
        <tr>
          <th>课程名称</th>
          <th>课程学分</th>
          <th>课程类别</th>
          <th>课程学年</th>
          <th>课程学期</th>
          <th>学生学号</th>
          <th>学生姓名</th>
          <th>学生班级</th>
          <th>分数</th>
          <th>提交成绩</th>
        </tr>
        </thead>
        <tbody v-for="(each,index) in list">
        <tr>
          <td>{{each.course_name}}</td>
          <td>{{each.course_credit}}</td>
          <td>{{each.course_type}}</td>
          <td>{{each.course_year}}</td>
          <td>{{each.course_semester}}</td>
          <td>{{each.student_number}}</td>
          <td>{{each.student_name}}</td>
          <td>{{each.student_banji_name}}</td>
          <td><textarea class="form-control" placeholder="分数" v-model="score[index]"></textarea></td>
          <td><button class="btn btn-sm" type="submit" @click="submit_score(each,index)">确认提交</button></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: "teacher_upload",
    data() {
      return {
        teacher_number: null,
        list: null,
        year: '',
        semester: '',
        score: [],
      }
    },
    methods: {
      tea_find_stu: function () {
        if (this.year == "" || this.semester == "") {
          alert("请选择学年和学期")
        } else {
          let data = {
            'year': this.year,
            'semester': this.semester,
            'teacher_number': this.$cookie.get('user_teacher_number')
          };
          /*接口请求*/
          this.$http.post(this.Global_Api + '/scoremng/teacher_check_uncommitted_score/', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            } else {
              this.list = res.body.uncommitted_student_score_list;
              if (this.list.length === 0) {
                alert("本学期您没有教授课程！");
              }
            }
          });
        }
      },
      methods: {
        tea_find_stu: function () {
          if (this.year == "" || this.semester == "") {
            alert("请选择学年和学期")
          } else {
            let data = {
              'year': this.year,
              'semester': this.semester,
              'teacher_number': this.$cookie.get('user_teacher_number')
            };
            /*接口请求*/
            this.$http.post(this.Global_Api + '/scoremng/teacher_check_scores/', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              } else {
                this.list = res.body.student_score_list;
                if (this.list.length === 0) {
                  alert("本学期您没有教授课程！");
                }
              }
            });
          }
        },
        submit_score: function (each, index) {
          if (this.score[index] != "") {
            let data = {
              'course_name': each.course_name,
              'course_credit': each.course_credit,
              'course_type': each.course_type,
              'course_year': this.year,
              'course_semester': this.semester,
              'student_number': each.student_number,
              'student_name': each.student_name,
              'student_banji_name': each.student_banji_name,
              'course_score': this.score[index],
              'teacher_number': this.$cookie.get('user_teacher_number'),
            };
            /*接口请求*/
            this.$http.post(this.Global_Api + '/scoremng/teacher_upload/', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              } else {
                this.list = res.body.student_score_list;
                alert("提交成功！");
              }
            });
          } else {
            alert("请填写学生成绩！");
          }
        },
      },
    }
  }
</script>

<style scoped>
  .year_semester{
    float:left;
    margin-left:30px;
  }
</style>

