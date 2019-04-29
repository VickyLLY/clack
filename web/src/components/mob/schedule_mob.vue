<template>
    <bar_mob>
      <table id="kblist_table" class="table table-hover table-bordered text-center timetable">
        <tbody>
              <tr><td colspan="4">
              <div class="timetable_title">
              <h6 class="pull-left">2018-2019学年第2学期</h6>周志伟的课表<h6 class="pull-right">　学号：2016014322</h6>
              </div>
              </td></tr>
              <tr class="tbody_head"><td>星期</td><td>课表信息</td></tr>
        </tbody>

        <tbody id="xq_1" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期一</span></td></tr>
        <tr v-for="x in course1">
            <td>
              <div class="timetable_con text-left">
                <span class="title">{{x.course_name}}</span>
                <br>
                <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
                <span class="glyphicon glyphicon-tower">{{"节数："+x.start+"-"+x.end}}</span>
                <br>
                <span class="glyphicon glyphicon-tower">{{"上课地点："+x.location}}</span>
                <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
              </div>
            </td>
        </tr>
        </tbody>

        <tbody id="xq_2" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期二</span></td></tr>
        <tr v-for="y in course2">
          <td>
            <div class="timetable_con text-left">
              <span class="title">{{y.course_name}}</span>
              <br>
              <span class="glyphicon glyphicon-calendar">{{"周数："+y.start_week+"-"+y.end_week}}</span>
              <span class="glyphicon glyphicon-tower">{{"节数："+y.start+"-"+y.end}}</span>
              <span class="glyphicon glyphicon-tower">{{"上课地点："+y.location}}</span>
              <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
            </div>
          </td>
        </tr>
        </tbody>

        <tbody id="xq_3" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期三</span></td></tr>
        <tr v-for="x in course3">
          <td>
            <div class="timetable_con text-left">
              <span class="title">{{x.course_name}}</span>
              <br>
              <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
              <span class="glyphicon glyphicon-tower">{{"节数："+x.start+"-"+x.end}}</span>
              <span class="glyphicon glyphicon-tower">{{"上课地点："+x.location}}</span>
              <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
            </div>
          </td>
        </tr>
        </tbody>

        <tbody id="xq_4" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期四</span></td></tr>
        <tr v-for="x in course4">
          <td>
            <div class="timetable_con text-left">
              <span class="title">{{x.course_name}}</span>
              <br>
              <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
              <span class="glyphicon glyphicon-tower">{{"节数："+x.start+"-"+x.end}}</span>
              <span class="glyphicon glyphicon-tower">{{"上课地点："+x.location}}</span>
              <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
            </div>
          </td>
        </tr>
        </tbody>

        <tbody id="xq_5" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期五</span></td></tr>
        <tr v-for="x in course5">
          <td>
            <div class="timetable_con text-left">
              <span class="title">{{x.course_name}}</span>
              <br>
              <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
              <span class="glyphicon glyphicon-tower">{{"节数："+x.start+"-"+x.end}}</span>
              <span class="glyphicon glyphicon-tower">{{"上课地点："+x.location}}</span>
              <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
            </div>
          </td>
        </tr>
        </tbody>

        <tbody id="xq_6" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期六</span></td></tr>
        <tr v-for="x in course6">
          <td>
            <div class="timetable_con text-left">
              <span class="title">{{x.course_name}}</span>
              <br>
              <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
              <span class="glyphicon glyphicon-tower">{{"节数："+x.start+"-"+x.end}}</span>
              <span class="glyphicon glyphicon-tower">{{"上课地点："+x.location}}</span>
              <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
            </div>
          </td>
        </tr>
        </tbody>

        <tbody id="xq_7" style=""><tr><td id="xq_rowspan_1" rowspan="4" width="50"><br><span class="week">星期日</span></td></tr>
        <tr v-for="x in course7">
          <td>
            <div class="timetable_con text-left">
              <span class="title">{{x.course_name}}</span>
              <br>
              <span class="glyphicon glyphicon-calendar">{{"周数："+x.start_week+"-"+x.end_week}}</span>
              <span class="glyphicon glyphicon-tower">{{"节数："+x.start+"-"+x.end}}</span>
              <br>
              <span class="glyphicon glyphicon-tower">{{"上课地点："+x.location}}</span>
              <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
            </div>
          </td>
        </tr>
        </tbody>
      </table>
      <button @click="fun"></button>
    </bar_mob>
</template>

<script>
  import bar_mob from './bar_mob'
  export default {
    mounted(){
      let data={
          "student_number" : 1
      };
      this.$http.post(this.Global_Api + '/schedule/student_course_list',data).then((res) => {
        console.log(res.body.course_list)
        for(let i in res.body.course_list){
          if(res.body.course_list[i].date_and_classroom.length==0){
            continue;
          }
          else{
            let a=res.body.course_list[i].date_and_classroom[0].day_of_week;
            let c=res.body.course_list[i].date_and_classroom[0];
            let b=res.body.course_list[i];
            if(a===1){
              this.course1.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
            }
            else if(a===2){
              this.course2.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
            }
            else if(a===3){
              this.course3.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
            }
            else if(a===4){
              this.course4.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
            }
            else if(a===5){
              this.course5.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
            }
            else if(a===6){
              this.course6.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
            }
            else if(a===7){
              this.course7.push({
                course_name:b.course_name,
                start:3,
                end:5,
                start_week:c.start_week,
                end_week:c.end_week,
                location:c.classroom.classroom_name,
              });
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
      fun:function () {
        alert(this.course1.length)
      }

    },
    data(){
      return{
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
