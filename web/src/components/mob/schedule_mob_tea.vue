<template>
  <bar_mob>
    <table id="kblist_table" class="table table-hover table-bordered text-center timetable">
      <tbody>
      <tr><td colspan="4">
        <div class="timetable_title">
          <h6 class="pull-left">2018-2019学年第2学期</h6>{{realname}}的课表<h6 class="pull-right">　教师工号：{{user_teacher_number}}</h6>
        </div>
      </td></tr>
      <tr class="tbody_head"><td>星期</td><td>节次</td><td>课表信息</td></tr>
      </tbody>

      <tbody id="xq_1" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期一</span></td></tr>

      <tr v-for="x in course1">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <tbody id="xq_2" style=""><tr><td id="xq_rowspan_1" rowspan="4" style="width: 15%;"><br><span class="week">星期二</span></td></tr>
      <tr v-for="x in course2">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <tbody id="xq_3" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期三</span></td></tr>
      <tr v-for="x in course3">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <tbody id="xq_4" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期四</span></td></tr>
      <tr v-for="x in course4">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <tbody id="xq_5" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期五</span></td></tr>
      <tr v-for="x in course5">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <tbody id="xq_6" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期六</span></td></tr>
      <tr v-for="x in course6">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <tbody id="xq_7" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期日</span></td></tr>
      <tr v-for="x in course7">
        <td style="width: 15%;"><br>{{x.start+"-"+x.end}}</td>
        <td>
          <div class="timetable_con text-left">
            <span class="title">{{x.course_name}}</span>
            <br>
            <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
            <br>
            <span class="glyphicon glyphicon-map-marker">{{"上课地点："+x.location}}</span><br>
            <span class="glyphicon glyphicon-tower">{{"教师："+x.teacher}}</span>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
  </bar_mob>
</template>

<script>
  import bar_mob from './bar_mob'
  export default {
    mounted(){
      let data={
        "user_name": this.user_name,
        "user_token": this.user_token,
        "teacher_number": this.user_teacher_number,
        "year": 2018,
        "semester": 2
      };
      this.$http.post(this.Global_Api + '/schedule/teacher_course_list',data).then((res) => {
        for(var i in res.body.course_list){
          if(res.body.course_list[i].date_and_classroom.length==0){
            continue;
          }
          else{
            for(let j=0;j<res.body.course_list[i].date_and_classroom.length;j++){
              let a=res.body.course_list[i].date_and_classroom[j].day_of_week;
              let c=res.body.course_list[i].date_and_classroom[j];
              let b=res.body.course_list[i];
              if(a===1){
                if(b.teachers.length===0){
                  this.course1.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course1.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
              else if(a===2){
                if(b.teachers.length===0){
                  this.course2.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course2.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
              else if(a===3){
                if(b.teachers.length===0){
                  this.course3.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course3.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
              else if(a===4){
                if(b.teachers.length===0){
                  this.course4.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course4.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
              else if(a===5){
                if(b.teachers.length===0){
                  this.course5.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course5.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
              else if(a===6){
                if(b.teachers.length===0){
                  this.course6.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course6.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
              else if(a===7) {
                if(b.teachers.length===0){
                  this.course7.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:'',
                  });
                }
                else{
                  this.course7.push({
                    course_name:b.course_name,
                    start:c.start,
                    end:c.end,
                    start_week:c.start_week,
                    end_week:c.end_week,
                    location:c.classroom.classroom_name,
                    teacher:b.teachers[0].teacher_name,
                  });
                }
              }
            }
          }
        }
        if(this.course1.length===0){
          document.getElementById('xq_1').style.display='none';
        }
        if(this.course2.length===0){
          document.getElementById('xq_2').style.display='none';
        }
        if(this.course3.length===0){
          document.getElementById('xq_3').style.display='none';
        }
        if(this.course4.length===0){
          document.getElementById('xq_4').style.display='none';
        }
        if(this.course5.length===0){
          document.getElementById('xq_5').style.display='none';
        }
        if(this.course6.length===0){
          document.getElementById('xq_6').style.display='none';
        }
        if(this.course7.length===0){
          document.getElementById('xq_7').style.display='none';
        }
      });
    },
    methods:{
    },
    data(){
      return{
        user_teacher_number:this.$cookie.get('user_teacher_number'),
        realname:this.$cookie.get('realname'),
        user_student_number:this.$cookie.get('user_student_number'),
        course1:[],
        course2:[],
        course3:[],
        course4:[],
        course5:[],
        course6:[],
        course7:[],
      }
    },
    components: {
      bar_mob
    }
  }
</script>

<style scoped>
  *{
    color: black;
  }
</style>
