<template>
  <div>
    <!-- 页面顶部导航栏 -->
    <PC_bar></PC_bar>

    <!-- 下拉菜单选择学年及学期 -->
    <form class="form-inline" role="form" style="text-align: center">
      <div class="form-group" style="margin: 20px">
        <label for="year" style="margin: 10px">选择学年</label>
        <select class="form-control">
          <option>2016-2017 学年</option>
          <option>2017-2018 学年</option>
          <option>2018-2019 学年</option>
          <option>2019-2020 学年</option>
        </select>
        &nbsp;&nbsp;
        <label for="semester" style="margin: 10px">选择学期</label>
        <select class="form-control">
          <option>上学期（9月-2月）</option>
          <option>下学期（3月-6月）</option>
          <option>小学期（7月-8月）</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <div class="form-group">
          <input type="text" class="form-control" placeholder="输入课程名">
        </div>

      </div>
      <button type="submit" class="btn btn-primary">
        <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>  确认
      </button>
    </form>

    <!-- 学期课程信息 -->
    <table class="table table-hover">
      <caption class="table-bar" style="font-size: larger; font-weight: bolder">课程信息</caption>
      <thead>
      <tr>
        <th class="table-bar">学年</th>
        <th class="table-bar">学期</th>
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
          <td>{{course.course_year}}</td>
          <td>{{course.course_semester}}</td>
          <td>{{course.course_id}}</td>
          <td>{{course.course_name}}</td>
          <td>{{course.course_type}}</td>
          <td>{{course.course_credit}}</td>
          <td>{{course.course_teacher}}</td>
          <td>{{course.course_allowance}}</td>
          <td>{{course.course_capacity}}</td>
          <td>{{course.course_classroom}}</td>
          <td>{{course.course_department}}</td>
          <td>
            <!--使用课程代码进行绑定-->
            <a data-toggle="modal" v-bind:data-target="'#'+course.course_id">
              <span class="glyphicon glyphicon glyphicon-list-alt"></span>
            </a>
          </td>

            <!-- 学生名单弹窗 -->
            <div class="modal fade" v-bind:id="course.course_id" tabindex="-1" role="dialog" aria-labelledby="studentListModalLabel" aria-hidden="true">
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
                    <form class="form-inline" role="form" style="text-align: center">
                      <div class="form-group" style="margin: 20px">
                        <label for="searchStudent" style="margin: 10px">学生名单检索项</label>
                        <select class="form-control">
                          <option>学号</option>
                          <option>姓名</option>
                          <option>学院</option>
                          <option>专业</option>
                          <option>班级</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>  确认
                      </button>
                    </form>

                    <!--学生名单表-->
                    <table class="table table-hover">
                      <thead>
                      <tr>
                        <th class="table-bar">学号</th>
                        <th class="table-bar">姓名</th>
                        <th class="table-bar">学院</th>
                        <th class="table-bar">专业</th>
                        <th class="table-bar">班级</th>
                      </tr>
                      </thead>
                      <tbody class="table-bar">
                        <tr v-for="stu in course_student">
                          <td>{{stu.student_number}}</td>
                          <td>{{stu.student_name}}</td>
                          <td>{{stu.student_department}}</td>
                          <td>{{stu.student_major}}</td>
                          <td>{{stu.student_banji_id}}</td>
                        </tr>
                      </tbody>

                    </table>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                    <button type="button" class="btn btn-primary">
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
            <h4 style="text-align: center">2018-2019学年第2学期</h4>
          </div>
        </td>
      </tr>
      <tr class="tbody_head">
        <td width="20%">星期</td>
        <td>节次</td>
        <td>课表信息</td>
      </tr>
      </tbody>

      <!--星期一课表-->
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <!--星期二课表-->
      <tbody id="xq_2" style="">
      <tr>
        <td id="xq_rowspan_2" rowspan="4" style=""><br><span class="week">星期二</span></td>
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <!--星期三课表-->
      <tbody id="xq_3" style="">
      <tr>
        <td id="xq_rowspan_3" rowspan="4" width=""><br><span class="week">星期三</span></td>
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <!--星期四课表-->
      <tbody id="xq_4" style="">
      <tr>
        <td id="xq_rowspan_4" rowspan="4" width=""><br><span class="week">星期四</span></td>
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <!--星期五课表-->
      <tbody id="xq_5" style="">
      <tr>
        <td id="xq_rowspan_5" rowspan="4" width=""><br><span class="week">星期五</span></td>
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
            <span class="glyphicon glyphicon-tower">{{"教师："}}</span>
          </div>
        </td>
      </tr>
      </tbody>

      <!--星期六课表-->
      <tbody id="xq_6" style="">
      <tr>
        <td id="xq_rowspan_6" rowspan="4" width=""><br><span class="week">星期六</span></td>
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

      <!--星期日课表-->
      <tbody id="xq_7" style="">
      <tr>
        <td id="xq_rowspan_7" rowspan="4" width=""><br><span class="week">星期日</span></td>
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
          //获得教师用户名
          teacher_id: this.$cookie.get("user_name"),

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
        }
      },
      created() {
        let select_course = {
          year: 2019,
          semester: 1,
          teacher_name: '1',
        };
        this.$http.post(this.Global_Api + '/selecourse/teacher_inquiry', select_course).then((res) => {
          for (let i = 0; i < res.body.course_student_list.length; i++) {
            this.teacher_course.push(course_student_list[i]);
          }
        });
      },
      methods() {

      },
      course_table() {

        let data = {
          "user_name": this.user_name,
          "user_token": this.user_token,
        };
        data = {
          "user_name": this.user_name,
          "user_token": this.user_token,
          "teacher_number": this.user_teacher_number,
          "year": 2018,
          "semester": 2,
        };
        this.$http.post(this.Global_Api + '/schedule/teacher_course_list', data).then((res) => {

        });
      },
    }

</script>

<style scoped>

  .table-bar {
    text-align: center;
  }

</style>
