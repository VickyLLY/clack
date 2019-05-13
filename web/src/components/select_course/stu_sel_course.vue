<template>
  <div style="overflow: hidden;position:relative;">
    <nav class="navbar navbar-default navbar-fixed-top">
      <a href="/main" class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="">自主选课</a></li>
        <li><a href="javascript:void(0)" @click="enter_timetable">查看课表</a></li>
        <li><a href="javascript:void(0)" @click="enter_attention">其他注意事项</a></li>
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
          <p
            style="width:15px;height: 20px;position: absolute;top:420px;border-radius: 50%;background: white;text-align: center">
            {{count}}</p>
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
              <td :class=td[n-1]>{{n}}</td>
              <td v-for="m in 7" class="init" class_count=0>
              </td>
            </tr>
            <tr>
              <td colspan="3"><span class="little_course"
                                    style="width: 25px;height: 15px;display: inline-block;vertical-align: center"></span><span>上课周数0-5周</span>
              </td>
              <td colspan="3"><span class="middle_course"
                                    style="width: 25px;height: 15px;display: inline-block;"></span><span>上课周数5-10周</span>
              </td>
              <td colspan="3"><span class="large_course"
                                    style="width: 25px;height: 15px;display: inline-block"></span><span>上课周数大于10周</span>
              </td>
            </tr>
          </table>
        </div>
      </div>
      <div class="row" style="overflow:scroll;">
        <div v-html="once">

        </div>
      </div>
    </div>
    <div class="panel panel-default" style="width: 95%;allowance: 0 auto">

      <div class="panel-body">
        <div class="panel-heading">
          <h2  style="text-align:center;"><strong>2019学年第1学期选课</strong></h2>
          <h3 style="text-align:right;">
            <!--<font size="3" ><strong>剩余<font color="red">{{day}}</font>天</strong></font>
            <font size="2">选课要求总学分最低<font color="red">{{min_lp}}</font></font>
            <font size="2">最高学分<font color="red">{{max_lp}}</font></font>
            <font size="2">已获得学分<font color="red">{{get_lp}}</font></font>
            <font size="2">本学期已选<font color="red">{{sel_lp}}</font></font>-->
            <font size="3" style="color: #204d74;background: #66afe9">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</font>
            <font size="3" ><strong>待选</strong></font>
            <font size="3" style="color: #204d74;background: lightgreen">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</font>
            <font size="3" ><strong>已选</strong></font>
          </h3>
        </div><!--选课标题-->
        <hr/>
        <div>
          <h1>
            <font size="3" color="red" ><span class="glyphicon glyphicon-list-alt"></span> <strong>专业必修</strong></font>
            <!--<font size="2">要求修读<font color="red">2</font>学分,</font>
            <font size="2">以获得<font color="red">2</font>学分,</font>
            <font size="2">本学期已选<font color="red">2</font>学分</font>-->
          </h1>
          <div v-for="c in z_b_course">
            <div v-if="-1==stu_sel.indexOf(c.course_id)" class="panel panel-default">
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
                  <tr >
                    <td>{{c.course_id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_department}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td v-if="c.course_allowance > 0" ><button type="button" class="btn btn-primary" v-on:click="add_course(c.course_id,username)" >选课</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div v-else>
              <div class="panel-heading" style="color: #204d74;background:lightgreen">
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
                    <td>{{c.course_id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_department}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td><button type="button" class="btn btn-primary" v-on:click="del_course(c.course_id,username)">退选</button></td>
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
            <!--<font size="2">要求修读<font color="red">2</font>学分,</font>
            <font size="2">以获得<font color="red">{{get_lp}}2</font>学分,</font>
            <font size="2">本学期已选<font color="red">{{sel_lp}}2</font>学分</font>-->
          </h1>
          <!--<ul>-->

          <div v-for="c in z_x_course">
            <div v-if="-1==stu_sel.indexOf(c.course_id)" class="panel panel-default">
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
                    <td>{{c.course_id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_department}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td v-if="c.course_allowance > 0" ><button type="button" class="btn btn-primary" v-on:click="add_course(c.course_id,username)" >选课</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div v-else>
              <div class="panel-heading" style="color: #204d74;background:lightgreen">
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
                    <td>{{c.course_id}}</td>
                    <td>{{c.course_name}}</td>
                    <td>{{c.course_credit}}</td>
                    <td>{{c.course_type}}</td>
                    <td>{{c.course_capacity}}</td>
                    <td>{{c.course_allowance}}</td>
                    <td>{{c.course_teacher}}</td>
                    <td>{{c.course_department}}</td>
                    <td>{{c.start_week+"-"+c.end_week}}</td>
                    <td>{{"星期"+c.day_of_week+"  "+c.start+"-"+c.end}}</td>
                    <td><button type="button" class="btn btn-primary" v-on:click="del_course(c.course_id,username)">退选</button></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <!--</ul>-->

        </div>
      </div>
      <br><br><br><br><br><br><br><br><br>
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
        once:`` ,
        current: ``,
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
    created(){
      //alert(123)
      /*将可选课程分为必修与选修*/
      let sel_class={
        "year":2018,
        "semester":1 ,
        "student_number":this.username
      };
      this.$http.post(this.Global_Api + '/selecourse/student_inquiry',sel_class).then((res) =>{
        for (let i=0;i<res.body.course_list.length;i++){
          //alert(res.body.course_list[i].course_name)
          if(res.body.course_list[i].course_type==0)
            this.z_b_course.push(res.body.course_list[i])
          else{
            this.z_x_course.push(res.body.course_list[i])
          }
          if(res.body.course_list[i].course_access==false)
          {
            this.stu_sel.push(res.body.course_list[i].course_id)
          }
          if(this.stu_sel.length)
            this.count=this.stu_sel.length;
        }
        //alert(res.body.course_list[0].course_name)
      })

    },
    methods: {
      enter_timetable: function () {
        this.$router.push('stu_sel_course/stu_timetable');
      },
      enter_attention: function () {
        this.$router.push('stu_sel_course/attention');
      },
      quit: function () {
        this.$cookie.delete('username');
      },
      add_course:function(id,stu_name){
        //alert(stu_name+" select  "+id+this.stu_sel)/*学生选课*/
        let add_class={
          student_number:this.username,
          course_id:id
        };
        this.$http.post(this.Global_Api + '/selecourse/sele_button', add_class).then((res) =>{
          if(res.body.error_code==0)
          {this.stu_sel.push(id)
            alert("选课成功")
            this.count++;
            //location.reload()
            /*for (var i=0;i<this.stu_sel.length;i++)
          {alert("ok123")
            if (this.stu_sel[i]==id)
            {
              alert("ok")
              Vue.set(this.stu_sel,i,"")

            }
          }*/
          }
          else{
            alert("选课失败")
          }
        })
      },
      del_course:function(id,stu_name){
        //alert(stu_name+" delete  "+id)/*删除所选课程*/
        let del_class={
          student_number:this.username,
          course_id:id
        };
        this.$http.post(this.Global_Api + '/selecourse/dele_button', del_class).then((res) =>{
          if(res.body.error_code==0)
          {for(var i=0;i<this.stu_sel.length;i++)
          {
            if(this.stu_sel[i]==id)
            {
             delete this.stu_sel[i]
              break
            }
          }
            alert("退选成功")
            this.count--;
            //location.reload()
            /*for (var i=0;i<this.stu_sel.length;i++)
          {alert("ok123")
            if (this.stu_sel[i]==id)
            {
              alert("ok")
              Vue.set(this.stu_sel,i,"")

            }
          }*/
          }
          else{
            alert("退课失败")
          }
        })

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
      reColor: function () {
        alert("get_course");
        let data = {
          "year": 2018,
          "semester": 1,
          "student_number": this.username,
        };
        this.$http.post(this.Global_Api + '/selecourse/course_inquiry', data).then((res) => {
          // alert(res.body.error_code);
          // alert(res.body.course_list.length);
          for (let i = 0; i < res.body.course_list.length; i++) {
            for(let j=res.body.course_list[i].start;j<=res.body.course_list[i].end;j++){
              let k=res.body.course_list[i].day_of_week;
              let m=res.body.course_list[i].end_week-res.body.course_list[i].start_week+1;
              let selector=$("."+this.td[j-1]);
              let new_attr=String(parseInt(selector.nextAll()[k-1].getAttribute("class_count"))+5);
              selector.nextAll()[k-1].setAttribute("class_count",new_attr);
            }
          }
          alert("reColor");
          for (let i = 0; i < this.td.length; i++) {
            let selector = this.td[i];
            for (let j of $("." + selector).nextAll()) {
              if (parseInt(j.getAttribute("class_count")) === 0) {
                j.className = 'init';
              } else if (parseInt(j.getAttribute("class_count")) > 0 && parseInt(j.getAttribute("class_count")) <= 5) {
                j.className = 'little_course';
              } else if (parseInt(j.getAttribute("class_count")) > 5 && parseInt(j.getAttribute("class_count")) <= 10) {
                j.className = 'middle_course';
              } else if (parseInt(j.getAttribute("class_count")) > 10) {
                j.className = 'large_course';
              }
            }
          }
        })
      },
      set_attribution: function () {
        alert("set");
        for (let i = 0; i < this.td.length; i++) {
          let selector = this.td[i];
          $("." + selector).nextAll().attr("class_count", 0);
        }
      },
    },
    mounted: function () {
      var that = this;
      var oDiv1 = document.getElementById('aside');
      this.$nextTick(() => {
        that.set_attribution();
        that.reColor();
        if (that.timer) {
          clearInterval(that.timer);
        }
        that.timer = setInterval(() => {
          that.updateTime(that);
        }, 1000);
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
    computed: {},
    watch: {}
  }
</script>

<style scoped>
  #clock {
    font-family: 'Microsoft YaHei', 'Lantinghei SC', 'Open Sans', Arial, 'Hiragino Sans GB', 'STHeiti', 'WenQuanYi Micro Hei', 'SimSun', sans-serif;
    color: black;
    text-align: center;
    position: absolute;
    left: 60%;
    top: 10px;
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

  .init {
    background: green;
  }

  .little_course {
    background: blue;
  }

  .middle_course {
    background: yellow;
  }

  .large_course {
    background: red;
  }

</style>
