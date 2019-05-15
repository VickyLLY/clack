<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <a href="/main" class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="/main/stu_sel_course">自主选课</a></li>
        <li><a href="javascript:void(0)" @click="enter_timetable">查看课表</a></li>
        <li><a href="javascript:void(0)" @click="enter_attention">其他注意事项</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li class="col-md-7">
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            {{realname}}
            <b class="caret"></b>
          </a>
          <ul class="dropdown-menu">
            <li><a href="#">修改个人信息</a></li>
            <li><a href="/" @click="quit">注销</a></li>
          </ul>
        </li>
      </ul>
    </nav>
    <br><br><br>
    <table id="kblist_table" class="table table-hover table-bordered text-center timetable text-center">
      <tbody>
      <tr>
        <td colspan="4">
          <div class="timetable_title">
            <h6 class="pull-left">2018-2019学年第1学期</h6>{{realname}}的课表<h6 class="pull-right">
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

  </div>
</template>

<script>
  import PC_bar from '../public/PC_bar'

  export default {
    name: "stu_timetable",
    components: {
      PC_bar
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
              break;
            } else {
                let a = res.body.course_list[i].day_of_week;
                let b = res.body.course_list[i];
                if (a === 1) {
                  this.course1.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
                } else if (a === 2) {
                  this.course2.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
                } else if (a === 3) {
                  this.course3.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
                } else if (a === 4) {
                  this.course4.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
                } else if (a === 5) {
                  this.course5.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
                } else if (a === 6) {
                  this.course6.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
                } else if (a === 7) {
                  this.course7.push({
                    course_name: b.course_name,
                    start: b.start,
                    end: b.end,
                    start_week: b.start_week,
                    end_week: b.end_week,
                    location: b.classroom_name,
                    teacher:b.course_teacher,
                  });
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
    data() {
      return {
        realname: this.$cookie.get('realname'),
        username: this.$cookie.get('username'),
        course1: [],
        course2: [],
        course3: [],
        course4: [],
        course5: [],
        course6: [],
        course7: [],
      }
    },
  }
</script>

<style scoped>

</style>
