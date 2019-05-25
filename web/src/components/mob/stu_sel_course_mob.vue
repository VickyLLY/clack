<template>
  <div>
    <bar_mob>
    <table id="kblist_table" class="table table-hover table-bordered text-center timetable">
      <tbody>
      <tr>
        <td colspan="4">
          <div class="timetable_title">
            <h6 class="pull-left">2019-2020学年第1学期</h6>{{realname}}的课表<h6 class="pull-right">
            　学号：{{user_student_number}}</h6>
          </div>
        </td>
      </tr>
      <tr class="tbody_head">
        <td width="20%">星期</td>
        <td>节次</td>
        <td>课表信息</td>
      </tr>
      </tbody>

      <tbody id="xq_1" style="">
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

      <tbody id="xq_2" style="">
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

      <tbody id="xq_3" style="">
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

      <tbody id="xq_4" style="">
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

      <tbody id="xq_5" style="">
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

      <tbody id="xq_6" style="">
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

      <tbody id="xq_7" style="">
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
    </bar_mob>
  </div>
</template>

<script>
  import bar_mob from '../mob/bar_mob'

  export default {
    name: "stu_sel_course",
    components: {
      bar_mob
    },
    data(){
      return{
        username:this.$cookie.get('username'),
        realname:this.$cookie.get('realname'),
        user_type: this.$cookie.get('user_type'),
        course1: [],
        course2: [],
        course3: [],
        course4: [],
        course5: [],
        course6: [],
        course7: [],
      }
    },
    created(){
      this.$nextTick(function () {
        $('#sidebarCollapse').on('click',
          function () {
            $('#sidebar').toggleClass('active');
          }
        )
      })
    },
    methods:{
      enter_timetable: function () {
        this.$router.push('stu_timetable');
      },
      enter_attention: function () {
        this.$router.push('attention');
      },
      quit: function () {
        this.$cookie.delete('username');
      },
      course_sort:function(){
        this.course1.sort(function (a,b) {
          return a.start-b.start;
        });
        this.course2.sort(function (a,b) {
          return a.start-b.start;
        });
        this.course3.sort(function (a,b) {
          return a.start-b.start;
        });
        this.course4.sort(function (a,b) {
          return a.start-b.start;
        });
        this.course5.sort(function (a,b) {
          return a.start-b.start;
        });
        this.course6.sort(function (a,b) {
          return a.start-b.start;
        });
        this.course7.sort(function (a,b) {
          return a.start-b.start;
        });
      }
    },
    mounted() {
      if (this.$cookie.get('username') == null || this.$cookie.get('user_type')!=='2') {
        this.$router.push('/')
      }
      else {
        let data = {
          "year":2019,
          "semester":1,
          "student_number": this.username//记得改变post的学生id
        };
        this.$http.post(this.Global_Api + '/selecourse/course_inquiry', data).then((res) => {
          for (let i=0;i<res.body.course_list.length;i++) {
            if (res.body.course_list[i].length === 0) {

            } else {
              for(let j=0;j<res.body.course_list[i].classroom_info.length;j++){
                let a = res.body.course_list[i].classroom_info[j].day_of_week;
                let b = res.body.course_list[i].classroom_info[j];
                let c=res.body.course_list[i];
                if (a === 1) {
                  this.course1.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                } else if (a === 2) {
                  this.course2.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                } else if (a === 3) {
                  this.course3.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                } else if (a === 4) {
                  this.course4.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                } else if (a === 5) {
                  this.course5.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                } else if (a === 6) {
                  this.course6.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                } else if (a === 7) {
                  this.course7.push({
                    course_name: c.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:c.course_teacher,
                  });
                }
              }
            }
          }
          this.course_sort();
          if (this.course1.length === 0) {
            document.getElementById('xq_1').style.display = 'none';
          }
          if (this.course2.length === 0) {
            document.getElementById('xq_2').style.display = 'none';
          }
          if (this.course3.length === 0) {
            document.getElementById('xq_3').style.display = 'none';
          }
          if (this.course4.length === 0) {
            document.getElementById('xq_4').style.display = 'none';
          }
          if (this.course5.length === 0) {
            document.getElementById('xq_5').style.display = 'none';
          }
          if (this.course6.length === 0) {
            document.getElementById('xq_6').style.display = 'none';
          }
          if (this.course7.length === 0) {
            document.getElementById('xq_7').style.display = 'none';
          }
        });
      }

    },
  }
</script>

<style scoped>
  *{
    color: black;
  }
</style>
