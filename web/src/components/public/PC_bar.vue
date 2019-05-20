<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <a href="/main" class="navbar-brand"><strong>教务管理系统</strong></a>
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                排课子系统
                <b class="caret"></b>
              </a>
              <ul class="dropdown-menu">
                <!--0 admin ,1 teacher, 2 student-->
                <li><a href="javascript:void(0)" v-if="user_type===0" @click="add_course">添加课程</a></li>
                <li><a href="javascript:void(0)" v-if="user_type===0" @click="arrange_course">安排课程</a></li>
                <li><a href="javascript:void(0)" v-if="user_type===0" @click="add_semester">添加学期</a></li>
                <li><a href="javascript:void(0)" v-if="user_type===2" @click="stu_check_course_table">查看课表(学生)</a></li>
                <li><a href="javascript:void(0)" v-if="user_type===1" @click="tea_check_course_table">查看课表(教师)</a></li>
              </ul>
            </li>
            <li><a href="#" class="dropdown-toggle" data-toggle="dropdown">
              选课子系统
              <b class="caret"></b>
            </a>
              <ul class="dropdown-menu">
                <li><a href="javascript:void(0)" @click="select_course">自主选课</a></li>
                <li><a href="javascript:void(0)" @click="view_course">查看课表及课程情况</a></li>
              </ul>
            </li>
                      <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
              后台管理子系统
              <b class="caret"></b>
            </a>
            <ul class="dropdown-menu">
              <li><a href="javascript:void(0)" @click="edit_student">编辑学生信息</a></li>
              <li><a href="javascript:void(0)" @click="edit_teacher">编辑教师信息</a></li>
              <li><a href="javascript:void(0)" @click="edit_classroom">编辑教室信息</a></li>
              <li><a href="javascript:void(0)" @click="edit_major">编辑专业信息</a></li>
              <li><a href="javascript:void(0)" @click="edit_department">编辑学院信息</a></li>
              <li><a href="javascript:void(0)" @click="edit_class">编辑班级信息</a></li>
              <li><a href="javascript:void(0)" @click="add_notice">发布公告通知</a></li>
             <li><a href="javascript:void(0)" @click="help">帮助</a></li>

            </ul>
          </li>
            <li><a href="">毕业设计管理子系统</a></li>
            <li><a href="javascript:void(0)" @click="scoremng">成绩管理子系统</a></li>
          </ul>
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
      </div>
    </nav>

    <br><br><br>
  </div>
</template>

<script>
  export default {
    name: "PC_bar",
    data() {
      return {
        username: this.$cookie.get('username'),
        realname: this.$cookie.get('realname'),
        user_type: parseInt(this.$cookie.get('user_type')),
      }
    },
    mounted(){
      //alert(typeof this.user_type)
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
      help:function(){
        this.$router.push('/main/help');
      },
      add_course: function () {
        if (this.user_type == 0) {
          this.$router.push('/main/add_course');
        }
        else {
          alert("你没有管理员权限");
        }
      },
      add_semester:function(){
          this.$router.push({name:"add_semester"})
      },
      arrange_course: function () {
        this.$router.push('/main/arrange_semester');
      },
      background: function (module_name) {
        if (this.user_type == 0) {
          this.$router.push('/main/' + module_name);
        }
        else {
          alert("你没有管理员权限");
        }
      },
      edit_classroom:function () {
            // if (this.user_type === '0') {
            //   this.$router.push('/main/edit_classroom');
            // }
            // else {
            //   alert('你没有管理员权限');
            // }
            this.$router.push('/main/edit_classroom');
          },
      edit_major:function () {
        // if (this.user_type === '0') {
        //   this.$router.push('/main/edit_classroom');
        // }
        // else {
        //   alert('你没有管理员权限');
        // }
        this.$router.push('/main/edit_major');
      },
      edit_student:function () {
        // if (this.user_type === '0') {
        //   this.$router.push('/main/edit_classroom');
        // }
        // else {
        //   alert('你没有管理员权限');
        // }
        this.$router.push('/main/edit_student');
      },
      edit_teacher:function () {
        // if (this.user_type === '0') {
        //   this.$router.push('/main/edit_classroom');
        // }
        // else {
        //   alert('你没有管理员权限');
        // }
        this.$router.push('/main/edit_teacher');
      },
      edit_department:function () {
        // if (this.user_type === '0') {
        //   this.$router.push('/main/edit_classroom');
        // }
        // else {
        //   alert('你没有管理员权限');
        // }
        this.$router.push('/main/edit_department');
      },
      edit_class:function () {
        // if (this.user_type === '0') {
        //   this.$router.push('/main/edit_classroom');
        // }
        // else {
        //   alert('你没有管理员权限');
        // }
        this.$router.push('/main/edit_class');
      },
      help:function () {
        // if (this.user_type === '0') {
        //   this.$router.push('/main/edit_classroom');
        // }
        // else {
        //   alert('你没有管理员权限');
        // }
        this.$router.push('/main/help');
      },
      arrange_course: function () {
        this.$router.push('/main/arrange_semester')
      },
      select_course: function () {
        if (this.user_type == 2) {
          this.$router.push('/main/stu_sel_course');
        } else if (this.user_type == 1) {
          alert("老师无法选课")
        } else if(this.user_type == 0) {
          alert('管理员无法选课');
        }else{
          alert("系统出现未知错误");
        }
      },
      view_course:function () {
        if (this.user_type == 2) {
          this.$router.push('/main/stu_sel_course/stu_timetable');
        } else if (this.user_type == 1) {
          this.$router.push('/main/tea_sel_course');
        } else if(this.user_type == 0) {
          this.$router.push('/main/man_sel_course')
        }else{
          alert("系统出现未知错误");
        }
      },
      stu_check_course_table:function () {
        this.$router.push({name:'course_table'});
      },
      tea_check_course_table:function(){
        this.$router.push({name:'tea_course_table'})
      },
      scoremng:function () {
        this.$router.push('/main/navigation')
      },
      add_notice:function () {
        this.$router.push('/main/background/add_notice')
      }
    }
  }
</script>

<style scoped>

</style>
