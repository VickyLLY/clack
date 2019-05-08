<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <a href="#/" class="navbar-brand"><strong>教务管理系统</strong></a>
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                排课子系统
                <b class="caret"></b>
              </a>
              <ul class="dropdown-menu">
                <li><a href="javascript:void(0)" @click="add_course">添加课程</a></li>
                <li><a href="javascript:void(0)" @click="arrange_course">安排课程</a></li>
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
            <li><a href="">后台管理子系统</a></li>
            <li><a href="">毕业设计管理子系统</a></li>
            <li><a href="">成绩管理子系统</a></li>
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
              <li><a href="#/" @click="quit">注销</a></li>
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
        user_type: this.$cookie.get('user_type')
      }
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
      add_course: function () {
        if (this.user_type == 0) {
          this.$router.push('/main/add_course')
        } else {
          alert("你没有管理员权限")
        }
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
          this.$router.push('/main/stu_sel_course/timetable');
        } else if (this.user_type == 1) {
          this.$router.push('/main/tea_sel_course');
        } else if(this.user_type == 0) {
          this.$router.push('/main/man_sel_course')
        }else{
          alert("系统出现未知错误");
        }
      }
    }
  }
</script>

<style scoped>

</style>
