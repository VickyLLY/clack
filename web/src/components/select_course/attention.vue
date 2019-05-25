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
            <li><a href="#/" @click="quit">注销</a></li>
          </ul>
        </li>
      </ul>
    </nav>
    <br><br><br>

    <div class="container sl_all_bg newsdisp"  style="min-height: 600px !important;">

      <h2 class="text-center"><strong >选课注意事项</strong></h2>

      <hr>

      <div class="news_con" style="border:1px dotted whitesmoke;border-radius: 3px;">
        <p>
    <span style="font-size: 16.0px;"><span style="">全体本科生和研究生：<br />
  </span></span>
        </p>
        <p>
          <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 现将选课安排和注意事项通知如下，请同学们务必在规定时间内完成网上选课。</span></span>
        </p>
        <p>
          <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 网上选课路径：<a href="http://localhost:8080/main/stu_sel_course">http://localhost:8080/main/stu_sel_course</a></span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="line-height: 16px;">一、选课时间安排：<br />

      &nbsp;&nbsp;&nbsp; 系统规定时间，具体请阅读首页通知 <br/>

  二、选课内容安排：<br />
  &nbsp;&nbsp;&nbsp; 1、全校性选修<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 2、专业选修课<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 3、特殊类课程（国际化课程）<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 4、重修选课：因为小学期开设都是实践类课程，必须上课。所以，跟班重修的学生必须经过学生所在学院同意后，到学生所在学院申请手工选课。<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 5、因为学籍变动，不能网上退选课的学生请到所在学院申请手工选课。<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 6、必修课需要同学们手动添加课程，且必须首要添加。<br />
  三、选课注意事项<br />
  &nbsp;&nbsp;&nbsp;&nbsp;1、请学生网上选修课程时，注意课表的下方部分实践必修课程，虽然实践必修课程没有安排时间，但同学务必到学院核实清楚实践必修课程上课时间、地点，以免和选修课程上课时间冲突。<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 2、请同学们要严格遵守选课时间，截止日期后，不再做选课的后补工作。<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 3、选课结束后，会因为选课人数不足的原因而做停课处理，请关注系统中的公告。<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 4、小学期选课无退补选课安排，以本次选课结束后的课表为准，请确认查看个人课表。成绩记载以课表为准，未退掉的课程如果不上课或不参加考试，将以零分记载。<br />
  </span></span>
        </p>
        <p>
    <span style="font-size: 16.0px;"><span style="">&nbsp;&nbsp;&nbsp; 5、在选课期间内，选课系统全天24小时对学生开放。学生可根据自己的实际情况选择在非高峰时期上网选课，以获得较快的网络连接速度。<br />
  </span></span>
        </p>
        <p style="text-align: right;">
    <span style="font-size: 16.0px;"><span style=""><br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>教务处</strong><br />
  </span></span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "attention",
      data() {

        return {
          username: this.$cookie.get('username'),
          realname: this.$cookie.get('realname'),
        }
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
      }
    }
</script>

<style scoped>

</style>
