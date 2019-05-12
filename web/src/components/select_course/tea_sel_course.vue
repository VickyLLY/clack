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
        &nbsp;&nbsp;&nbsp;&nbsp;
        <label for="semester" style="margin: 10px">选择学期</label>
        <select class="form-control">
          <option>上学期（9月-2月）</option>
          <option>下学期（3月-6月）</option>
          <option>小学期（7月-8月）</option>
        </select>
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
        <th class="table-bar">学分</th>
        <th class="table-bar">任课老师</th>
        <th class="table-bar">课程容量</th>
        <th class="table-bar">已选人数</th>
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
          <td>{{course.course_capacity}}</td>
          <td>{{course.course_stu_num}}</td>
          <td>{{course.course_department}}</td>
          <td><button><span class="glyphicon glyphicon glyphicon-th-list"></span></button></td>
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
        return {
          // 课程测试数据
          teacher_course: [
            {course_id: "001", course_name: "计算机组成原理", course_credit: 4.5, course_type: 0, course_year: 2016,
              course_semester: 1, course_capacity: 180, course_stu_num: 140, course_teacher: "吴越", course_department: "信息学院"},
            {course_id: "002", course_name: "计算机系统结构", course_credit: 3.5, course_type: 0, course_year: 2016,
              course_semester: 1, course_capacity: 180, course_stu_num: 150, course_teacher: "吴越", course_department: "信息学院"},
            {course_id: "003", course_name: "计算机导论", course_credit: 2.0, course_type: 0, course_year: 2016,
              course_semester: 1, course_capacity: 180, course_stu_num: 160, course_teacher: "吴越", course_department: "信息学院"},
          ],
        }
      }
    }

</script>

<style scoped>
  .table-bar {
    text-align: center;
  }
</style>
