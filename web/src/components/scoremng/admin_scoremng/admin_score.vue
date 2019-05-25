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
        <button class="btn btn-default" type="submit" @click="admin_find_score">查询成绩</button>
      </div>
      <div class="year_semester">
        <button class="btn btn-link" type="submit" @click="admin_download_score">下载成绩</button>
      </div>
    </div>

    <br><br><br>

    <div>
      <table class="table table-bordered">
        <thead>
        <tr>
          <th>课程名称</th>
          <th>课程种类</th>
          <th>课程学年</th>
          <th>课程学期</th>
          <th>课程学分</th>
          <th>课程平均成绩</th>
        </tr>
        </thead>
        <tbody v-for="(value,index) in list">
        <tr>
          <td>{{value.course_name}}</td>
          <td>{{value.course_type}}</td>
          <td>{{value.course_year}}</td>
          <td>{{value.course_semester}}</td>
          <td>{{value.course_credit}}</td>
          <td>{{value.course_avg_score}}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: "admin_score",
    data() {
      return {
        admin_number:null,
        list: null,
        year:'',
        semester:'',
      }
    },
    methods:{
      admin_find_score:function () {
        if(this.year=="" || this.semester==""){
          alert("请选择学年和学期")
        }
        else{
          let data = {
            'year': this.year,
            'semester': this.semester,
          };
          /*接口请求*/
          this.$http.post(this.Global_Api + '/scoremng/admin_check_scores/',data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            }
            else {
              this.list = res.body.avg_score_list;
              if(this.list.length === 0){
                alert("暂无本学期课程成绩信息！");
              }
            }
          });
        }
      },
      admin_download_score:function () {
        if(this.year=="" || this.semester==""){
          alert("请选择学年和学期");
        }
        else{
          let data = {
            'year': this.year,
            'semester': this.semester,
          };
          /*接口请求*/
          this.$http.post(this.Global_Api + '/scoremng/admin_download_scores/',data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("下载失败!" + res.body.error_message);
            } else {
              alert("下载成功!");
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

