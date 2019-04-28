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
          <button class="btn btn-default" type="submit" @click="stu_find_score">查询</button>
<!--          <router-link :to="{name:'stu_score'}">成绩管理子系统</router-link>-->
        </div>
<!--        <get_year_semester @listenToChild="year_semester" ></get_year_semester>-->
      </div>



<!--      <div>-->
<!--        <div class="v_select" style="float:left;margin-left: 30px;">-->
<!--          <v-select max-height="80px" placeholder="学年" :options="course_year" v-model="course_year"></v-select>-->
<!--        </div>-->
<!--        <div class="v_select" style="float:left;margin-left: 30px;">-->
<!--          <v-select max-height="80px" placeholder="学期" :options="course_semester" v-model="course_semester"></v-select>-->
<!--        </div>-->
<!--        <div style="float:left;margin-left: 30px;">-->
<!--          <button class="btn btn-default" type="submit" @click="stu_score">查询</button>-->
<!--        </div>-->
<!--      </div>-->

      <br><br><br>

      <div>

<!--        <div v-for="(value,key) in message">-->
<!--          {{value}}-->
<!--        </div>-->
<!--        {{score_list}}-->
        {{message}}

      </div>



    </div>
</template>

<script>
  // import get_year_semester from '../../schedule/get_year_semester'

    export default {
      name: "stu_score",
      data() {
        return {
          student_number:this.$cookie.get('user_student_number'),
          // score_list: '',
          message:null,
          year:'',
          semester:''
        }
      },
      // components:{
      //   get_year_semester,
      // },
      methods:{

          stu_find_score:function () {

            let data = {'year': this.year, 'semester': this.semester};
            //this.message=data;
            /*接口请求*/
            this.$http.get(this.Global_Api + '/scoremng/student_scores/2015014069/',data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              } else {

                this.message = res.body;
                // this.score_list = res.body.score_list;
              }
            });

            // this.$http.get(this.Global_Api + '/schedule/course_list').then((res) =>{
            //   if (res.body.error_code !== 0) {
            //     alert("error!" + res.body.error_message)
            //   } else {
            //     this.message = res.body;
            //   }
            // });

          }
      }
    }
</script>

<style scoped>
  .year_semester{
    float:left;
    margin-left:30px;
  }
</style>
