<template>
  <div>
    <PC_bar></PC_bar>
        <div class="panel panel-default" id="cnmx"><!--每一个块的新闻部分-->
          <div class="panel-heading">
            <h3 id="selecttype">筛选条件</h3>
            <get_year_semester @listenToChild="year_semester" ></get_year_semester>
            <department_list @listenToChild="department"></department_list>
            <get_coursetype @listenToChild="course_type" ></get_coursetype>
          </div>
          <div style="white-space: pre-wrap;" id="div-select">
            <div style="height: 458px; overflow-y: scroll">
              <ul id="ul-select" style="">
                <li class="list-group-item" v-for="each in course" @click="fun(each)">
                  <a>{{ each.course_name }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div id="xianshi" class="panel-heading" style="overflow-y: scroll">
          <div id="main" >
            <h3 id="title" style="margin-left: 20px; margin-top:10px;display: none">基本课程信息</h3>
            <div id="change-block">
              <div class="change-content">
                <span class="interface-title">课程名称：</span><input type="text" id="cs_name" class="form-control" v-on:input ="myfun($event)" required="required">
                <button id="but1" type="button" class="btn btn-info aabb"  style="color: white" @click="confirm">√</button>
              </div>
              <div class="change-content">
                <span>课程学分：</span><input type="text" id="cs_credit" class="form-control" v-on:input ="myfun($event)" required="required">
                <button type="button" class="btn btn-info" style="color: white">√</button>
              </div>
              <div class="change-content">
                <span>课程类型：</span><input type="text" id="cs_type" class="form-control" v-on:input ="myfun($event)" required="required">
                <button type="button" class="btn btn-info" style="color: white">√</button>
              </div>
              <div class="change-content">
                <span>课程容量：</span><input type="text" id="cs_capacity" class="form-control" v-on:input ="myfun($event)" required="required">
                <button type="button" class="btn btn-info" style="color: white">√</button>
              </div>
              <div class="change-content">
                <span>开课学院：</span><input type="text" id="cs_department" class="form-control" v-on:input ="myfun($event)" required="required">
                <button type="button" class="btn btn-info" style="color: white">√</button>
              </div>
            </div>
            <h3 id="title2" style="margin-left: 20px; margin-top:10px;display: none">上课时间教室</h3>
            <div id="change-block2">
              <div class="hello">
                <button @click="add" class="btn2 btn-success">+</button>
                <test v-for=" (x,index) in items"
                      :index="index"
                      :items="items"
                      @del="delete_time"
                      @myfun="myfun"
                >
                </test>
              </div>
            </div>
          </div>
        </div>
  </div>
</template>

<script>
    import test from '../mob/test'
    import get_coursetype from './get_coursetype'
    import get_year_semester from './get_year_semester'
    import PC_bar from '../public/PC_bar'
    import department_list from '../public/department_list'
    export default {
      name: "arrange_course",
      components: {
        get_year_semester,
        PC_bar,
        department_list,
        get_coursetype,
        test,
      },
      data() {

        return {
          year: undefined,
          semester: undefined,
          department_id: undefined,
          coursetype: undefined,
          list: '',
          course: [],
          select_course: '',
          items: [//课程时间地点具体请问ppg
            {
              start_week: 1,
              end_week: 11,
              day_of_week: 4,
              start: 1,
              end: 3,
            },
            {
              start_week: 1,
              end_week: 2,
              day_of_week: 3,
              start: 4,
              end: 5,
            }
          ],
          count:0,
          dataRec: [],
        }
      },
      mounted() {
        if (this.$cookie.get('username') == null)
          this.$router.push('/')
        this.$http.post(this.Global_Api + '/schedule/course_list', {}).then((res) => {
          this.list = res.body.course_list
          for (let i = 0; i < this.list.length; i++)
            this.course.push(this.list[i])
          //alert(this.course.length)
        })
      },
      methods: {
        delete_time: function(e){
          this.items.splice(e, 1)
        },
        add: function () {
          this.items.push({time: '', place: ''})
        },
        del: function (index) {
          alert(123);
            this.items.splice(index, 1)
        },
        year_semester(val) {
          if (val != null) {
            this.year = val.year;
            this.semester = val.semester;
          } else {
            this.year = undefined;
            this.semester = undefined
          }
          let data = {};
          if (typeof (this.year) != "undefined")
            data['course_year'] = this.year;
          if (typeof (this.semester) != "undefined")
            data['course_semester'] = this.semester;
          if (typeof (this.department_id) != "undefined")
            data['course_department_id'] = this.department_id;
          if (typeof (this.coursetype) != "undefined")
            data['course_type'] = this.coursetype;
          this.course = [];
          this.$http.post(this.Global_Api + '/schedule/course_list', data).then((res) => {
            this.list = res.body.course_list
            for (let i = 0; i < this.list.length; i++)
              this.course.push(this.list[i])
          })
        },
        department(val) {
          if (val != null)
            this.department_id = val;
          else
            this.department_id = undefined;
          let data = {};
          if (typeof (this.year) != "undefined")
            data['course_year'] = this.year;
          if (typeof (this.semester) != "undefined")
            data['course_semester'] = this.semester;
          if (typeof (this.department_id) != "undefined")
            data['course_department_id'] = this.department_id;
          if (typeof (this.coursetype) != "undefined")
            data['course_type'] = this.coursetype;
          this.course = [];
          this.$http.post(this.Global_Api + '/schedule/course_list', data).then((res) => {
            this.list = res.body.course_list
            for (let i = 0; i < this.list.length; i++)
              this.course.push(this.list[i])
          })
        },
        course_type(val) {
          if (val != null)
            this.coursetype = val.coursetype;
          else
            this.coursetype = undefined;
          let data = {};
          if (typeof (this.year) != "undefined")
            data['course_year'] = this.year;
          if (typeof (this.semester) != "undefined")
            data['course_semester'] = this.semester;
          if (typeof (this.department_id) != "undefined")
            data['course_department_id'] = this.department_id;
          if (typeof (this.coursetype) != "undefined")
            data['course_type'] = this.coursetype;
          this.course = [];
          this.$http.post(this.Global_Api + '/schedule/course_list', data).then((res) => {
            this.list = res.body.course_list
            for (let i = 0; i < this.list.length; i++)
              this.course.push(this.list[i])
          })
        },
        fun: function (val) {
          document.getElementById("change-block").style.display = "block";
          document.getElementById("title").style.display = "block";
          document.getElementById("title2").style.display = "block";
          document.getElementById("change-block2").style.display = "block";
          document.getElementById("cs_name").value = val.course_name;
          document.getElementById("cs_credit").value = val.course_credit;
          document.getElementById("cs_type").value = val.course_type;
          document.getElementById("cs_capacity").value = val.course_capacity;
          document.getElementById("cs_department").value = val.course_department_id;
          var x = document.getElementsByClassName("btn-info");
          for (let i in x) {
            x[i].style.display = "none";
          }
        },
        confirm: function () {
          alert(document.getElementById("cs_name").value)
        },
        myfun: function (node) {
          var thisDom = node.currentTarget
          thisDom.parentNode.lastChild.style.display = "inline-block"
        },
        show: function () {
          alert(this.items[0].place)
        }
      }
    }
</script>

<style scoped>
  .hello{
    animation: donghua 1s;
  }
  *{
    list-style: none;
    text-decoration: none;
    color:black;
    outline: 0 none;
  }
  a{
    text-decoration: none;
    outline: 0 none;
  }
  a:hover{color:black;}
  li{
    display: block;
    height: 50px;
    width: 313px;
    border-left: 0px solid black;
    border-bottom: 0px solid black;
    border-right: 0px solid black;
    line-height: 50px;
    padding: 0;
  }
  li::before{
    content: "";
    display: inline-block;
    width: 30px;
  }
  ul{
    margin-left: -55px;
  }
  li:hover{
    background: #f5f5f5;
  }
  ::-webkit-scrollbar {
    width: 0px;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
  }
  #cnmx{
    margin-left:15%;
    margin-top: 30px;
    height: 600px;
    width: 300px;
    float: left
  }
  #selecttype{
    padding: 0;
    margin: 10px;
  }
  #xianshi{
    border: 1px solid #ddd;
    position: absolute;
    width: 50%;
    height: 79.5%;
    margin-left: 40%;
    margin-top: 31px;
  }
  #change-block,#change-block2{
    border: 3px solid #f5f5f5;
    width: 90%;
    height: 75%;
    display: none;
    margin: 0 auto;
    margin-top: 15px;
    background-color: #f5f5f5;
    animation: donghua 1s;
  }
  .hello{
    margin-left: 34px;
    width: 90%;
  }
  #change-block span,
  #change-block2 span{
    font-weight: bold;
  }
  li{
    cursor: pointer;
  }
  .change-content{
    border-bottom: 1px solid #ddd;
    margin: 30px 10%;
    padding: 5px;
  }
  .btn-info{
    display: none;
    margin-left: 50px;
    height: 30px;
    vertical-align:0px;
    animation: donghua 2s;
  }
  #change-block v-select{
    width: 50px;
  }
  #title,#title2{
    animation: donghua 2s;
  }
  @keyframes donghua{
    0%{
      opacity: 0;
    }
    100%{
      opacity: 1;
    }
  }
  .form-control,.form-select{
    width:250px;
    display: inline-block;
  }
  #change-block{
    margin-bottom: 50px;
  }
  #title,#title2{
    border-left:2px solid rgb(35,149,241);
    padding-left: 10px;
  }
  .btn2{
    width: 35px;
    border: 0;
    height: 35px;
    line-height: 35px;
    border-radius: 5px;
    font-size: 22px;
    margin: 25px;
    color: white;
  }

</style>
