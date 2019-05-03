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
          <button class="btn btn-default" type="submit" @click="stu_find_score">查询成绩</button>
        </div>
        <div class="year_semester">
          <button class="btn btn-link" type="submit" @click="stu_download_score">下载成绩</button>
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
              </tr>
            </thead>
            <tbody v-for="(value,index) in list">
              <tr>
                <td>{{value.course_name}}</td>
                <td>{{value.course_credit}}</td>
                <td>{{value.course_type}}</td>
                <td>{{value.score}}</td>
              </tr>
            </tbody>
          </table>

      </div>



    </div>
</template>

<script>

    export default {
      name: "stu_score",
      data() {
        return {
          student_number:null,
          list: null,
          year:'',
          semester:'',
        }
      },
      methods:{

          stu_find_score:function () {
            if(this.year=="" || this.semester==""){
              alert("请选择学年和学期")
            }
            else{
              let data = {'year': this.year, 'semester': this.semester,'student_number':this.$cookie.get('user_student_number')};
              /*接口请求*/
              this.$http.post(this.Global_Api + '/scoremng/student_check_scores/',data).then((res) => {
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

        stu_download_score:function () {
          if(this.year=="" || this.semester==""){
            alert("请选择学年和学期");
          }
          else{
            let data = {'year': this.year, 'semester': this.semester,'student_number':this.$cookie.get('user_student_number')};
            /*接口请求*/
            this.$http.post(this.Global_Api + '/scoremng/student_download_scores/',data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("下载失败!  " + res.body.error_message);
              } else {
                alert("下载成功！");
              }
            });
          }
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
