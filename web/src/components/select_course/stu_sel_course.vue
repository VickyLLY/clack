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
    <div class="panel panel-default" style="width: 95%;allowance: 0 auto">

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
            <font size="2">要求修读<font color="red">2</font>学分,</font>
            <font size="2">以获得<font color="red">2</font>学分,</font>
            <font size="2">本学期已选<font color="red">2</font>学分</font>
          </h1>
          <div v-for="c in z_b_course">
            <div v-if="-1==stu_sel.indexOf(c.id)" class="panel panel-default">
              <div class="panel-heading" style="color: #204d74;background: #66afe9">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.course_id">
                    ({{c.id}}){{c.course_name}}--{{c.course_credit}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.course_id" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>课程名</th>
                    <th>课程学分</th>
                    <th>课程类型</th>
                    <th>课程容量</th>
                    <th>课程余量</th>
                    <th>任课教师</th>
                    <th>开课学院</th>
                    <th>开课周数</th>
                    <th>上课时间</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr >
                    <td>{{c.id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_departmen}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td v-if="c.course_allowance > 0" ><button type="button" class="btn btn-primary" v-on:click="add_course(c.id,username)" >选课</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div v-else>
              <div class="panel-heading" style="color: #204d74;background:lightgreen">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.course_id">
                    ({{c.id}}){{c.course_name}}--{{c.course_credit}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.course_id" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>课程名</th>
                    <th>课程学分</th>
                    <th>课程类型</th>
                    <th>课程容量</th>
                    <th>课程余量</th>
                    <th>任课教师</th>
                    <th>开课学院</th>
                    <th>开课周数</th>
                    <th>上课时间</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td>{{c.id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_departmen}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td><button type="button" class="btn btn-primary" v-on:click="del_course(c.id,username)">退选</button></td>
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
            <font size="2">要求修读<font color="red">2</font>学分,</font>
            <font size="2">以获得<font color="red">{{get_lp}}2</font>学分,</font>
            <font size="2">本学期已选<font color="red">{{sel_lp}}2</font>学分</font>
          </h1>
          <!--<ul>-->

          <div v-for="c in z_x_course">
            <div v-if="-1==stu_sel.indexOf(c.id)" class="panel panel-default">
              <div class="panel-heading" style="color: #204d74;background: #66afe9">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.course_id">
                    ({{c.course_id}}){{c.course_name}}--{{c.course_credit}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.course_id" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>课程名</th>
                    <th>课程学分</th>
                    <th>课程类型</th>
                    <th>课程容量</th>
                    <th>课程余量</th>
                    <th>任课教师</th>
                    <th>开课学院</th>
                    <th>开课周数</th>
                    <th>上课时间</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td>{{c.id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_departmen}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td v-if="c.course_allowance > 0" ><button type="button" class="btn btn-primary" v-on:click="add_course(c.id,username)" >选课</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div v-else>
              <div class="panel-heading" style="color: #204d74;background:lightgreen">
                <h4 class="panel-title" >
                  <a data-toggle="collapse" data-parent="#accordion"  v-bind:href="'#'+c.course_id">
                    ({{c.id}}){{c.course_name}}--{{c.course_credit}}分
                  </a>
                </h4>
              </div>
              <div v-bind:id="c.course_id" class="panel-collapse collapse">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>课堂号</th>
                    <th>课程名</th>
                    <th>课程学分</th>
                    <th>课程类型</th>
                    <th>课程容量</th>
                    <th>课程余量</th>
                    <th>任课教师</th>
                    <th>开课学院</th>
                    <th>开课周数</th>
                    <th>上课时间</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td>{{c.id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_departmen}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td><button type="button" class="btn btn-primary" v-on:click="del_course(c.id,username)">退选</button></td>
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
    <div class="panel panel-default" style="width: 80%;allowance: 0 auto">

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
        stu_sel:[],
        z_b_course:[],
        z_x_course:[],
      }
    },
    created: function () {
      /*将可选课程分为必修与选修*/
      let sel_class={
        year:2019,
        semester:1 ,
        student_number:this.username
      };
      this.$http.post(this.Global_Api + '/schedule/course_list',[]).then((res) =>{
        for (let i=0;i<res.body.course_list.length;i++){
          alert(res.body.course_list[i].course_name)
          if(res.body.course_list[i].course_type==0)
            this.z_b_course.push(res.body.course_list[i])
          else{
            this.z_x_course.push(res.body.course_list[i])
          }
          if(res.body.course_list[i].course_access==1)
          {
            this.stu_sel.push(res.body.course_list[i].id)
          }
        }
        //alert(res.body.course_list[0].course_name)
      })
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
      add_course:function(id,stu_name){
        alert(stu_name+" select  "+id)/*学生选课*/
        let add_class={
          student_number:this.username,
          course_name:id
        };
        this.$http.post(this.Global_Api + '/selecourse/sele_button/', add_class).then((res) =>{
          if(res.body.select_information=="可选")
          { this.z_b_cours=[]
            this.z_x_course=[]
            this.stu_sel=[]
            alert("选课成功")
            let sel_class={
              year:'2019',
              semester:'1',
              student_number:this.username
            };
            this.$http.post(this.Global_Api + '/selecourse/student_inquiry/2016014//', sel_class).then((res) =>{
              for (var i in res.body.course_list){
                if(i.course_type=1)
                  this.z_b_course.push(i)
                else{
                  this.z_x_course.push(i)
                }
                if(i.course_access=0)
                {
                  this.stu_sel.push(i.id)
                }
              }
            })
          }
          else{
            alert("选课失败")
            this.z_b_cours=[]
            this.z_x_course=[]
            this.stu_sel=[]
            let sel_class={
              year:'2019',
              semester:'1',
              student_number:this.username
            };
            this.$http.post(this.Global_Api + '/selecourse/student_inquiry/2016014//', sel_class).then((res) =>{
              for (var i in res.body.course_list){
                if(i.course_type=1)
                  this.z_b_course.push(i)
                else{
                  this.z_x_course.push(i)
                }
                if(i.course_access=0)
                {
                  this.stu_sel.push(i.id)
                }
              }
            })
          }
        })
      },
      del_course:function(id,stu_name){
        alert(stu_name+" delete  "+id)/*删除所选课程*/
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
