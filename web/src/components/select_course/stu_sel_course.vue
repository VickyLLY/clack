<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <a class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="">本科生选课</a></li>
        <li><a href="">研究生选课</a></li>
        <li><a href="">查看课表</a></li>
        <li><a href="">其他注意事项</a></li>

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
    <div id="aside" class="container right"
         style="width:700px;height:700px;border:1px solid red;position:relative;top:100px;left:1140px;">
      <div class="row">
        <div class="col-lg-1" style="background: red;height:700px;position: relative;">
          <p style="width: 20px;height: 100px;position:absolute;top:140px;line-height: 30px;">选课信息</p>
          <p style="width: 20px;height: 100px;position: absolute;top:350px;line-height: 30px">已选</p>
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
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>3</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>4</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>5</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>6</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>7</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>8</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>9</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>10</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>11</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>12</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>13</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </table>
        </div>
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
            <div class="panel panel-default">
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
                    <td><button type="button" class="btn btn-primary">选课</button></td>
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
                                <td v-if="co.co_margin > 0" ><button type="button" class="btn btn-primary">选课</button></td>
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
                      <td v-if="co.co_margin > 0" ><button type="button" class="btn btn-primary">选课</button></td>
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
  export default {
    name: "stu_sel_course",
    data() {
      return {
        username: this.$cookie.get('username'),
        realname: this.$cookie.get('realname'),
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
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      }
    },
    mounted: function () {
      var oDiv1=document.getElementById('aside');
      alert(oDiv1);
      oDiv1.onmouseover = function () {
        startMove(this, 'left',500 );

      };
      oDiv1.onmouseout = function () {
        startMove(this, 'left', 1140);
      };

      function getStyle(obj, name) {
        if (obj.currentStyle) {
          return obj.currentStyle[name];
        } else {
          return getComputedStyle(obj, false)[name];
        }
      }

      function startMove(obj, attr, iTarget) {
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
          var cur = 0;

          if (attr === 'opacity') {
            cur = parseFloat(getStyle(obj, attr)) * 100;
          } else {
            cur = parseInt(getStyle(obj, attr));
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
      }
    }
  }
</script>

<style scoped>

</style>
