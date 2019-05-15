<template>
  <div>
    <!-- 页面顶部导航栏 -->
    <PC_bar></PC_bar>

    <!-- 下拉菜单选择学年及学期 -->
    <form class="form-inline" role="form" style="text-align: center">
      <div class="form-group" style="margin: 20px">
<!--        {{default_year}}-->
        <label for="year" style="margin: 10px">选择学年</label>
        <select class="form-control" v-model="default_year">
          <option v-for="item in years" :value="item.value">{{item.name}}</option>
        </select>
        &nbsp;&nbsp;
<!--        {{default_semester}}-->
        <label for="semester" style="margin: 10px">选择学期</label>
        <select class="form-control" v-model="default_semester">
          <option v-for="item in semesters" :value="item.value">{{item.name}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;
      </div>
      <button class="btn btn-primary" type="button" @click="get_course">
        <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>  确认
      </button>
    </form>

    <!-- 学期课程信息 -->
    <table class="table table-hover">
      <caption class="table-bar" style="font-size: larger; font-weight: bolder">课程信息</caption>
      <thead>
      <tr>
        <th class="table-bar">课程代码</th>
        <th class="table-bar">课程名称</th>
        <th class="table-bar">课程性质</th>
        <th class="table-bar">课程学分</th>
        <th class="table-bar">任课老师</th>
        <th class="table-bar">课程余量</th>
        <th class="table-bar">课程容量</th>
        <th class="table-bar">上课地点</th>
        <th class="table-bar">开课学院</th>
        <th class="table-bar"><span class="glyphicon glyphicon-user"></span> 学生名单 </th>
      </tr>
      </thead>
      <tbody class="table-bar">
        <tr v-for="course in teacher_course">
          <td>{{course.course_id}}</td>
          <td>{{course.course_name}}</td>
          <td>{{course.course_type}}</td>
          <td>{{course.course_credit}}</td>
          <td>{{course.teacher_name}}</td>
          <td>{{course.course_allowance}}</td>
          <td>{{course.course_capacity}}</td>
          <td>{{course.course_classroom}}</td>
          <td>{{course.course_department}}</td>
          <td>
            <!--使用课程代码进行绑定-->
            <a data-toggle="modal" v-bind:data-target="'#'+course.course_id" @click="get_student(course.course_id)">
              <span class="glyphicon glyphicon glyphicon-list-alt"></span>
            </a>
          </td>

            <!-- 学生名单弹窗 -->
            <div class="modal fade" v-bind:id="course.course_id" tabindex="-1"
                 role="dialog" aria-labelledby="studentListModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">

                  <!--显示课程名称-->
                  <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title" id="myModalLabel">{{course.course_name}}</h4>
                  </div>

                  <!--显示学生名单-->
                  <div class="modal-body">

                    <!--学生上课名单检索栏-->
<!--                    <form class="form-inline" role="form" style="text-align: center">-->
<!--                      <div class="form-group" style="margin: 20px">-->
<!--                        <label for="searchStudent" style="margin: 10px">学生名单检索项</label>-->
<!--                        <select class="form-control">-->
<!--                          <option>学号</option>-->
<!--                          <option>姓名</option>-->
<!--                          <option>学院</option>-->
<!--                          <option>专业</option>-->
<!--                          <option>班级</option>-->
<!--                        </select>-->
<!--                      </div>-->
<!--                      <button type="submit" class="btn btn-primary">-->
<!--                        <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>  确认-->
<!--                      </button>-->
<!--                    </form>-->

                    <!--学生名单表-->
                    <table class="table table-hover">
                      <thead>
                      <tr>
                        <th class="table-bar">课程名称</th>
                        <th class="table-bar">学号</th>
                        <th class="table-bar">姓名</th>
                        <th class="table-bar">班级</th>
                      </tr>
                      </thead>
                      <tbody class="table-bar">
                        <tr v-for="stu in course_student">
                          <td>{{stu.course_name}}</td>
                          <td>{{stu.student_number}}</td>
                          <td>{{stu.student_name}}</td>
                          <td>{{stu.student_banji}}</td>
                        </tr>
                      </tbody>

                    </table>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                    <button type="button" class="btn btn-primary" @click="export2Excel">
                      <span class="glyphicon glyphicon glyphicon-download-alt"></span> 下载名单
                    </button>
                  </div>
                </div><!-- /.modal-content -->
              </div><!-- /.modal -->
            </div>
        </tr>
      </tbody>
    </table>

    <!--课表表头-->
    <table id="kblist_table" class="table table-hover table-bordered text-center timetable">
      <tbody>
      <tr>
        <td colspan="4">
          <div class="timetable_title">
            <h4 style="text-align: center"> 2019 学年 1 学期 教师 {{realname}} 课表</h4>
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
          </div>
        </td>
      </tr>
      </tbody>

    </table>

  </div>
</template>

<script>
    import PC_bar from "../public/PC_bar";
    export default {
      name: "tea_sel_course",
      components: {PC_bar},
      data() {
        return{
          //默认年份2019
          default_year: 2019,
          //默认学期
          default_semester: 1,
          years: [
            {
              name: '2016-2017学期',
              value: 2016,
            },
            {
              name: '2017-2018学期',
              value: 2017,
            },
            {
              name: '2018-2019学期',
              value: 2018,
            },
            {
              name: '2019-2020学期',
              value: 2019,
            },
            {
              name: '2020-2021学期',
              value: 2020,
            },
          ],
          semesters: [
            {
              name: "第1学期",
              value: 1,
            },
            {
              name: "第2学期",
              value: 2,
            },
            {
              name: "第3学期",
              value: 3,
            },
          ],
          //获得教师用户名
          realname: this.$cookie.get('realname'),
          username: this.$cookie.get('username'),

          // 周一至周日数据
          course1: [],
          course2: [],
          course3: [],
          course4: [],
          course5: [],
          course6: [],
          course7: [],

          // 课程测试数据
          teacher_course: [],

          //上课学生信息
          course_student: [],

          table_data: [],
        }
      },

      created() {
        this.get_course();
      },

      methods: {
        get_course:function () {
          this.teacher_course = [];
          let select_course = {
            'year': this.default_year,
            'semester': this.default_semester,
            'teacher_number': this.username,
          };
          this.$http.post(this.Global_Api + '/selecourse/teacher_inquiry', select_course).then((res) => {
            //无课程信息输出提示窗口
            if (res.body.course_student_list.length == 0) {
              alert("所查询学年学期无课程信息")
            }
            //存在课程信息则输出课程信息列表
            else {
              for (let course of res.body.course_student_list) {
                this.teacher_course.push(course);
              }
            }
          });
        },

        get_student: function(course_id_par) {

          this.course_student = [];
          let student_list = {
            'year': this.default_year,
            'semester': this.default_semester,
            'course_id': course_id_par,
          };
          this.$http.post(this.Global_Api + '/selecourse/teacher_download', student_list).then((res) => {
            if (res.body.student_list.length == 0) {
              alert("该课程目前未有学生选择")
            }
            else {
              for (var student of res.body.student_list) {
                this.course_student.push(student);
                this.table_data.push(student);
              }
            }
          });
        },

        export2Excel() {
          require.ensure([], () => {
            const { export_json_to_excel } = require('../../excel/Export2Excel.js');
            const tHeader = ['课程名称', '学生姓名', '学生学号', '学生班级'];
            // 上面设置Excel的表格第一行的标题
            const filterVal = ['course_name', 'student_name', 'student_number', 'student_banji'];
            // 上面的index、phone_Num、school_Name是tableData里对象的属性
            const list = this.table_data;  //把data里的tableData存到list
            const data = this.formatJson(filterVal, list);
            export_json_to_excel(tHeader, data, 'course');
          })
        },

        formatJson(filterVal, jsonData) {
          return jsonData.map(v => filterVal.map(j => v[j]))
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
        if (this.$cookie.get('username') == null || this.$cookie.get('user_type') !== '1') {
          this.$router.push('/')
        }
        else {
          let data = {
            "year": 2019,
            "semester": 1,
            "teacher_number": this.username//记得改变post的学生id
          };
          this.$http.post(this.Global_Api + '/selecourse/teacher_timetable', data).then((res) => {
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
    }

</script>

<style scoped>

  .table-bar {
    text-align: center;
  }

</style>
