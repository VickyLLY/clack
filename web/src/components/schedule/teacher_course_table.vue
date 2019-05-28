<template>
  <div>
    <PC_bar></PC_bar>
    <div class="select-teacher">
      <v-select max-height="80px" :options="teacher_list" placeholder="请选择你要查看的老师课表" style="width: 250px; display: inline-block" v-model="change_teacher" @change="teacher_change"></v-select>
    </div>
      <br>    <br>
    <table id="kblist_table" class="table table-hover table-bordered text-center timetable">
      <tbody>
      <tr>
        <td colspan="4">
          <div class="timetable_title">
            <h6 class="pull-left">2019学年第1学期</h6>{{realname}}的课表<h6 class="pull-right">　教师工号：{{user_teacher_number}}</h6>
          </div>
        </td>
      </tr>
      <tr class="tbody_head">
        <td width="20%">星期</td>
        <td>节次</td>
        <td>课表信息</td>
      </tr>
      </tbody>
      <tbody v-if="xq_1">
      <tr>
        <td id="xq_rowspan_1" rowspan="4"><br><span class="week">星期一</span></td>
      </tr>

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

      <tbody v-if="xq_2">
      <tr>
        <td id="xq_rowspan_1" rowspan="4" style=""><br><span class="week">星期二</span></td>
      </tr>
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

      <tbody v-if="xq_3">
      <tr>
        <td id="xq_rowspan_1" rowspan="4" width=""><br><span class="week">星期三</span></td>
      </tr>
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

      <tbody v-if="xq_4">
      <tr>
        <td id="xq_rowspan_1" rowspan="4" width=""><br><span class="week">星期四</span></td>
      </tr>
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

      <tbody v-if="xq_5">
      <tr>
        <td id="xq_rowspan_1" rowspan="4" width=""><br><span class="week">星期五</span></td>
      </tr>
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

      <tbody v-if="xq_6">
      <tr>
        <td id="xq_rowspan_1" rowspan="4" width=""><br><span class="week">星期六</span></td>
      </tr>
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

      <tbody v-if="xq_7">
      <tr>
        <td id="xq_rowspan_1" rowspan="4" width=""><br><span class="week">星期日</span></td>
      </tr>
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

  </div>
</template>

<script>
  import PC_bar from '../public/PC_bar'

  export default {
      components: {
        PC_bar
      },
      mounted(){
        let data={
          "user_name": this.user_name,
          "user_token": this.user_token
        };
        this.$http.post(this.Global_Api + '/schedule/teacher_list', data).then((res) => {
          for(let i=0;i<res.body.teacher_list.length;i++){
            let each={
              label:res.body.teacher_list[i].teacher_name,
              value:res.body.teacher_list[i].teacher_number
            };
            this.teacher_list.push(each);
          }
        });
        data={
          "user_name": this.user_name,
          "user_token": this.user_token,
          "teacher_number": this.user_teacher_number,
          "year": 2019,
          "semester": 1,
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
                  this.xq_1=true;
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
                  this.xq_2=true;

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
                  this.xq_3=true;

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
                  this.xq_4=true;

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
                  this.xq_5=true;

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
                  this.xq_6=true;

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
                  this.xq_7=true;

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
        });
      },
      methods:{
        teacher_change:function () {
          this.realname = this.change_teacher.label;
          this.teacher_number = this.change_teacher.value;
          let data={
            "user_name": this.user_name,
            "user_token": this.user_token,
            "teacher_number": this.change_teacher.value,
            "year": 2018,
            "semester": 2
          };
          this.$http.post(this.Global_Api + '/schedule/teacher_course_list',data).then((res) => {
            this.course1=[];
            this.course2=[];
            this.course3=[];
            this.course4=[];
            this.course5=[];
            this.course6=[];
            this.course7=[];
            this.xq_1=false;
            this.xq_2=false;
            this.xq_3=false;
            this.xq_4=false;
            this.xq_5=false;
            this.xq_6=false;
            this.xq_7=false;

            for(let i in res.body.course_list){
              if(res.body.course_list[i].date_and_classroom.length==0){

                continue;
              }
              else{
                for(let j=0;j<res.body.course_list[i].date_and_classroom.length;j++){
                  let a=res.body.course_list[i].date_and_classroom[j].day_of_week;
                  let c=res.body.course_list[i].date_and_classroom[j];
                  let b=res.body.course_list[i];
                  if(a===1){
                    this.xq_1=true;
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
                    this.xq_2=true;

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
                    this.xq_3=true;

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
                    this.xq_4=true;

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
                    this.xq_5=true;

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
                    this.xq_6=true;

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
                    this.xq_7=true;

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
          });
        }
      },
      data(){
        return{
          xq_1:false,
          xq_2:false,
          xq_3:false,
          xq_4:false,
          xq_5:false,
          xq_6:false,
          xq_7:false,
          user_teacher_number:this.$cookie.get('user_teacher_number'),
          realname:this.$cookie.get('realname'),
          user_name:this.$cookie.get('username'),
          user_token:this.$cookie.get('user_token'),
          course1:[],
          course2:[],
          course3:[],
          course4:[],
          course5:[],
          course6:[],
          course7:[],
          teacher_list:[],
          change_teacher:null,
        }
      },
    }

</script>

<style scoped>
  *{
    color: black;
  }
  div.select-teacher{
    text-align: center;
  }
</style>
