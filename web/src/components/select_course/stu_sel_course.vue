<template>
  <div style="overflow: hidden;position:relative;">
    <nav class="navbar navbar-default navbar-fixed-top">
      <a class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="">本科生选课</a></li>
        <li><a href="">研究生选课</a></li>
        <li><a href="">查看课表</a></li>
        <li><a href="">其他注意事项</a></li>
      </ul>
      <div id="clock">
        <p class="date">{{ date }}</p>
        <p class="time">{{ time }}</p>
      </div>
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

    <div id="aside" class="container pull-right "
         style="width:700px;height:900px;border:1px solid red;position:absolute;top:100px;right:-630px;background: white;">
      <div class="row">
        <div class="col-lg-1" style="background: red;height:700px;position: relative;">
          <p class="glyphicon glyphicon-arrow-left" style="width: 30px;height:30px;position: absolute;top:50px;"></p>
          <p style="width: 20px;height: 100px;position:absolute;top:140px;line-height: 30px;">选课信息</p>
          <p style="width: 20px;height: 100px;position: absolute;top:350px;line-height: 30px">已选</p>
          <p style="width:15px;height: 20px;position: absolute;top:420px;border-radius: 50%;background: white;text-align: center">{{count}}</p>
        </div>
        <div class="col-lg-11">
          <table class="table table-bordered text-center">
            <thead>
            <tr>
              <td>节次</td>
              <td>星期一</td>
              <td>星期二</td>
              <td>星期三</td>
              <td>星期四</td>
              <td>星期五</td>
              <td>星期六</td>
              <td>星期日</td>
            </tr>
            </thead>
            <tr v-for="n in 13">
              <td :class=td[n]>{{n}}</td>
              <td v-for="m in 7" :class=reColor>
              </td>
            </tr>
            <tr>
              <td colspan="3"><span class="little_course" style="width: 25px;height: 15px;display: inline-block;vertical-align: center"></span><span>空余周数=总周数</span></td>
              <td colspan="3"><span class="middle_course" style="width: 25px;height: 15px;display: inline-block;"></span><span>空余周数>=(总周数/2)</span></td>
              <td colspan="3"><span class="large_course" style="width: 25px;height: 15px;display: inline-block"></span><span>空余周数<(总周数/2)</span></td>
            </tr>
          </table>
        </div>
      </div>
      <div class="row" style="overflow:scroll;">

      </div>
    </div>
    <div class="panel panel-default" style="width: 95%;margin: 0 auto">

      <div class="panel-body">
        <div class="panel-heading">
          <h2  style="text-align:center;"><strong>选课标题</strong></h2>
          <h3>
            <font size="3" ><strong>剩余<font color="red">{{day}}</font>天</strong></font>
            <font size="2">选课要求总学分最低<font color="red">{{min_lp}}</font></font>
            <font size="2">最高学分<font color="red">{{max_lp}}</font></font>
            <font size="2">已获得学分<font color="red">{{get_lp}}</font></font>
            <font size="2">本学期已选<font color="red">{{sel_lp}}</font></font>
          </h3>
        </div><!--选课标题-->
        <hr/>
        <div>
          <h1>
            <font size="3" color="red" ><span class="glyphicon glyphicon-list-alt"></span> <strong>专业必修</strong></font>
            <font size="2">要求修读<font color="red">{{z_b_must_lp}}2</font>学分,</font>
            <font size="2">以获得<font color="red">{{z_b_get_lp}}2</font>学分,</font>
            <font size="2">本学期已选<font color="red">{{z_b_sel_lp}}2</font>学分</font>
          </h1>
          <div v-for="c in z_b_course">
            <div v-if="-1==stu_sel.indexOf(c.co_num)" class="panel panel-default">
              <div class="panel-heading" style="color: #204d74;background: #66afe9">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.co_num">
                    ({{c.co_num}}){{c.co_name}}--{{c.co_point}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.co_num" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>上课教师</th>
                    <th>上课时间</th>
                    <th>地点</th>
                    <th>学期</th>
                    <th>总容量</th>
                    <th>余量</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="co in z_b_course" >
                    <td>{{co.co_num}}</td>
                    <td>{{co.co_teacher}}</td>
                    <td>{{co.co_time}}</td>
                    <td>{{co.co_place}}</td>
                    <td>{{co.co_term}}</td>
                    <td>{{co.co_capacity}}</td>
                    <td>{{co.co_margin}}</td>
                    <td v-if="co.co_margin > 0" ><button type="button" class="btn btn-primary" v-on:click="add_course(co.co_num,username)" >选课</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div v-else>
              <div class="panel-heading" style="color: #204d74;background:lightgreen">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.co_num">
                    ({{c.co_num}}){{c.co_name}}--{{c.co_point}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.co_num" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>上课教师</th>
                    <th>上课时间</th>
                    <th>地点</th>
                    <th>学期</th>
                    <th>总容量</th>
                    <th>余量</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="co in z_b_course" >
                    <td>{{co.co_num}}</td>
                    <td>{{co.co_teacher}}</td>
                    <td>{{co.co_time}}</td>
                    <td>{{co.co_place}}</td>
                    <td>{{co.co_term}}</td>
                    <td>{{co.co_capacity}}</td>
                    <td>{{co.co_margin}}</td>
                    <td><button type="button" class="btn btn-primary" v-on:click="del_course(co.co_num,username)">退选</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div>
          <h1>
            <font size="3" color="red" ><span class="glyphicon glyphicon-list-alt"></span> <strong>专业选修</strong></font>
            <font size="2">要求修读<font color="red">{{z_b_must_lp}}2</font>学分,</font>
            <font size="2">以获得<font color="red">{{z_b_get_lp}}2</font>学分,</font>
            <font size="2">本学期已选<font color="red">{{z_b_sel_lp}}2</font>学分</font>
          </h1>
          <!--<ul>-->

          <div v-for="c in z_x_course">
            <div v-if="-1==stu_sel.indexOf(c.co_num)" class="panel panel-default">
              <div class="panel-heading" style="color: #204d74;background: #66afe9">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.co_num">
                    ({{c.co_num}}){{c.co_name}}--{{c.co_point}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.co_num" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>上课教师</th>
                    <th>上课时间</th>
                    <th>地点</th>
                    <th>学期</th>
                    <th>总容量</th>
                    <th>余量</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="co in z_x_course" >
                    <td>{{co.co_num}}</td>
                    <td>{{co.co_teacher}}</td>
                    <td>{{co.co_time}}</td>
                    <td>{{co.co_place}}</td>
                    <td>{{co.co_term}}</td>
                    <td>{{co.co_capacity}}</td>
                    <td>{{co.co_margin}}</td>
                    <td v-if="co.co_margin > 0" ><button type="button" class="btn btn-primary" v-on:click="add_course(co.co_num,username)" >选课</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div v-else>
              <div class="panel-heading" style="color: #204d74;background:lightgreen">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.co_num">
                    ({{c.co_num}}){{c.co_name}}--{{c.co_point}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.co_num" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>上课教师</th>
                    <th>上课时间</th>
                    <th>地点</th>
                    <th>学期</th>
                    <th>总容量</th>
                    <th>余量</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="co in z_x_course" >
                    <td>{{co.co_num}}</td>
                    <td>{{co.co_teacher}}</td>
                    <td>{{co.co_time}}</td>
                    <td>{{co.co_place}}</td>
                    <td>{{co.co_term}}</td>
                    <td>{{co.co_capacity}}</td>
                    <td>{{co.co_margin}}</td>
                    <td><button type="button" class="btn btn-primary" v-on:click="del_course(co.co_num,username)">退选</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <!--</ul>-->

        </div>
      </div>

    </div>
    <div class="panel panel-default" style="width: 80%;margin: 0 auto">

      <div class="panel-body">
        <h2>vue</h2>
      </div>

    </div>
  </div>
</template>


<script>
  import $ from 'jquery'
  export default {
    name: "stu_sel_course",
    data() {
      return {
        username: this.$cookie.get('username'),
        realname: this.$cookie.get('realname'),
        time: '',
        date: '',
        week: ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
        td:['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen'],
        count:0,
        day:0,
        max_lp:100,
        min_lp:100,
        get_lp:50,
        sel_lp:50,
        stu_sel:['201600123','201600124'],
        z_b_course:[{'co_point':3.0,'co_num':'201600123','co_name':'计算机组成原理','co_teacher':'薛博元','co_time':'3,4,5','co_place':'b103','co_term':'2','co_capacity':50,'co_sel':10,'co_margin':0},
          {'co_point':3.0,'co_num':'201600122','co_name':'计算机组成原理','co_teacher':'薛博元','co_time':'3,4,5','co_place':'b103','co_term':'2','co_capacity':50,'co_sel':10,'co_margin':20}],
        z_x_course:[{'co_point':3.0,'co_num':'201600124','co_name':'计算机组成原理','co_teacher':'薛博元','co_time':'3,4,5','co_place':'b103','co_term':'2','co_capacity':50,'co_sel':10,'co_margin':0},
          {'co_point':3.0,'co_num':'201600121','co_name':'计算机组成原理','co_teacher':'薛博元','co_time':'3,4,5','co_place':'b103','co_term':'2','co_capacity':50,'co_sel':10,'co_margin':20}],

      }
    },
    created: function () {
      /*将可选课程分为必修与选修*/
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
      add_course:function(course_num,stu_name){
        alert(stu_name+" select  "+course_num)/*学生选课*/
      },
      del_course:function(course_num,stu_name){
        alert(stu_name+" delete  "+course_num)/*删除所选课程*/
      },
      getStyle: function (obj, name) {
        if (obj.currentStyle) {
          return obj.currentStyle[name];
        } else {
          return getComputedStyle(obj, false)[name];
        }
      },
      startMove: function (obj, attr, iTarget, vueObject) {
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
          var cur = 0;

          if (attr === 'opacity') {
            cur = parseFloat(vueObject.getStyle(obj, attr)) * 100;
          } else {
            cur = parseInt(vueObject.getStyle(obj, attr));
          }

          var speed = (iTarget - cur) / 6;
          speed = speed > 0 ? Math.ceil(speed) : Math.floor(speed);
          console.log(speed);
          if (cur === iTarget) {
            clearInterval(obj.timer);
          } else {
            if (attr === 'opacity') {
              obj.style.filter = 'alpha(opcity:' + (cur + speed) + ')';
              obj.style.opacity = (cur + speed) / 100;
              document.getElementById('txt1').value = obj.style.opacity;
            } else {
              obj.style[attr] = cur + speed + 'px';
            }
          }
        }, 30);
      },
      updateTime: function (vueObject) {
        var cd = new Date();
        vueObject.time = vueObject.zeroPadding(cd.getHours(), 2) + ':' + vueObject.zeroPadding(cd.getMinutes(), 2) + ':' + vueObject.zeroPadding(cd.getSeconds(), 2);
        vueObject.date = vueObject.zeroPadding(cd.getFullYear(), 4) + '-' + vueObject.zeroPadding(cd.getMonth() + 1, 2) + '-' + vueObject.zeroPadding(cd.getDate(), 2) + ' ' + vueObject.week[cd.getDay()];
      },
      zeroPadding: function (num, digit) {
        var zero = '';
        for (let i = 0; i < digit; i++) {
          zero += '0';
        }
        return (zero + num).slice(-digit);
      },

    },
    mounted: function () {
      var that = this;
      var oDiv1 = document.getElementById('aside');
      this.$nextTick(() => {
        if(that.timer){
          clearInterval(that.timer);
        }
        that.timer=setInterval(()=>{
          that.updateTime(that);
        },1000);
        that.updateTime(that);
        oDiv1.onmouseover = function () {
          that.startMove(oDiv1, 'right', 0, that);
          $(".glyphicon-arrow-left").addClass("glyphicon-arrow-right").removeClass("glyphicon-arrow-left")
        };
        oDiv1.onmouseout = function () {
          that.startMove(oDiv1, 'right', -630, that);
          $(".glyphicon-arrow-right").addClass("glyphicon-arrow-left").removeClass("glyphicon-arrow-right")
        };

      })
    },
    computed:{
      reColor:function () {
        if(this.count===0)
          return 'init';
        else if(this.count>0&&this.count<3)
          return 'little_course';
        else
          return 'large_course';
      }
    },
    watch:{

    }
  }
</script>

<style scoped>
  #clock {
    font-family: 'Microsoft YaHei','Lantinghei SC','Open Sans',Arial,'Hiragino Sans GB','STHeiti','WenQuanYi Micro Hei','SimSun',sans-serif;
    color: black;
    text-align: center;
    position: absolute;
    left: 60%;
    top:10px;
  }
  #clock .time {
    letter-spacing: 0.05em;
    font-size: 20px;
    padding: 5px;
    display: inline-block;
  }
  #clock .date {

    display: inline-block;
    letter-spacing: 0.1em;
    font-size: 20px;
  }
  .init{
    background: green;
  }
  .little_course{
    background: blue;
  }
  .middle_course{
    background: yellow;
  }
  .large_course{
    background: red;
  }

</style>
