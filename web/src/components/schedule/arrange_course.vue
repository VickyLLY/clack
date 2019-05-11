<template>
  <div>
    <PC_bar></PC_bar>
    <div class="panel panel-default" id="cnmx"><!--每一个块的新闻部分-->
      <div class="panel-heading">
        <h3 id="selecttype">筛选条件</h3>
        <get_year_semester @listenToChild="year_semester"></get_year_semester>
        <department_list @listenToChild="department"></department_list>
        <get_coursetype @listenToChild="course_type"></get_coursetype>
      </div>
      <div style="white-space: pre-wrap;" id="div-select">
        <div style="height: 458px; overflow-y: scroll">
          <ul id="ul-select" style="">
            <li class="list-group-item" v-for="each in course" @click="choose_course(each)">
              <a>{{ each.course_name }}</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div id="xianshi" class="panel-heading" style="overflow-y: scroll">
      <div id="main">
        <h3 id="title" style="margin-left: 20px; margin-top:10px;display: none">基本课程信息</h3>
        <div id="change-block">
          <div class="change-content">
            <span class="interface-title">课程名称：</span><input type="text" id="cs_name" class="form-control"
                                                             v-on:input="change($event, 'course_name')" required="required">
            <button id="cs_name_but" type="button" class="btn btn-info aabb" style="color: white" @click="confirm_name">√</button>
          </div>
          <div class="change-content">
            <span>课程学分：</span><input type="text" id="cs_credit" class="form-control" v-on:input="change($event, 'course_credit')"
                                     required="required">
            <button id="cs_credit_but" type="button" class="btn btn-info" style="color: white" @click="confirm_credit">√</button>
          </div>
          <div class="change-content">
            <span>课程类型：</span>
            <v-select :options="coursetype_name" style="width: 250px; display: inline-block" v-model="change_type"
                      @change="type_change"></v-select>
            <button id="cs_type" type="button" class="btn btn-info " style="display:none;!important; color: white" @click="confirm_type">√
            </button>
          </div>
          <div class="change-content">
            <span>课程容量：</span><input type="text" id="cs_capacity" class="form-control" v-on:input="change($event, 'course_capacity')"
                                     required="required">
            <button id="cs_capacity_but" type="button" class="btn btn-info" style=" color: white" @click="confirm_capacity">√</button>
          </div>
          <div class="change-content">
            <span>开课学院：</span>
            <v-select max-height="80px" :options="department_list" style="width: 250px; display: inline-block" v-model="change_department" @change="department_change"></v-select>
            <button id="cs_department" type="button" class="btn btn-info " style="display:none;!important; color: white" @click="confirm_department">√
            </button>
          </div>
          <div class="change-content">
            <span>任课教师：</span>
            <v-select max-height="80px" :options="teacher_list" style="width: 250px; display: inline-block" v-model="change_teacher" @change="teacher_change"></v-select>
            <button id="cs_teacher" type="button" class="btn btn-info " style="display:none;!important; color: white" @click="confirm_teacher">√
            </button>
          </div>
        </div>
        <h3 id="title2" style="margin-left: 20px; margin-top:10px;display: none">上课时间教室</h3>
        <div id="change-block2">
          <div v-for=" (each,index) in added">
            <div class="hello">
              <span>开始周数：</span><v-select class="select-pt"
                                          max-height="80px"
                                          v-model=each.start_week
                                          :options="weeknum"
                                          @change="added_change(index)"
                                          required="required">
            </v-select>
              <span>结束周数：</span><v-select class="select-pt"
                                          max-height="80px"
                                          v-model=each.end_week
                                          :options="weeknum"
                                          @change="added_change(index)"
                                          required="required">
            </v-select>
              <span style="white-space: pre-wrap">星 期：</span><v-select class="select-pt"
                                                                       max-height="80px"
                                                                       v-model=each.day_of_week
                                                                       :options="week"
                                                                       @change="added_change(index)"
                                                                       required="required">
            </v-select>
              <br>
              <span>开始节数：</span><v-select class="select-pt"
                                          max-height="80px"
                                          v-model=each.start
                                          :options="jienum"
                                          @change="added_change(index)"
                                          required="required">
            </v-select>
              <span>结束节数：</span><v-select class="select-pt"
                                          max-height="80px"
                                          v-model=each.end
                                          :options="jienum"
                                          @change="added_change(index)"
                                          required="required">
            </v-select>
              <span>教 室：</span><v-select class="select-pt"
                                          max-height="80px"
                                          v-model=each.classroom
                                          :options=classrooms[index]
                                          @change="added_change(index)"
                                          required="required">
            </v-select>
              <button @click="delete_added(index)" class="btn5 btn-danger">删除</button>
              <button class="btn btn-info added" style="color: white" @click="confirm_change(index)">√</button>

            </div>

          </div>
          <div class="hello">
            <button @click="add" class="btn2 btn-success">+</button>
          </div>
            <test v-for=" (x,index) in items"
                  :key="index"
                  :index="index"
                  :items="items"
                  :course="select_course"
                  @del="delete_time"
                  @add_del="add_del"
                  @myfun="change"
            >
            </test>
        </div>
        <h3 id="title3" style=" margin-left: 20px; margin-top:40px;display: none">考试时间地点</h3>
        <div id="change-block3">
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
        coursetype_name: [
          {
            label: "必修",
            value: 0,
          },
          {
            label: "选修",
            value: 1
          }
        ],
        teacher_list:[],
        department_list:[],
        select_course: null,//当前所选课程
        change_type: null,
        change_department: null,
        change_teacher: null,
        list: '',
        course: [],
        items: [],//课程时间地点具体请问ppg
        count: 0,
        dataRec: [],
        //下列为课程已被安排所需信息
        week:[1,2,3,4,5,6,7],
        weeknum:[1,2,3,4,5,6,7,8,9,10,11,12,13],
        jienum:[1,2,3,4,5,6,7,8,9,10,11,12,13],
        classrooms:[],
        copy_classrooms:[],
        added: [],
        copy_added: [],
        change_index:null,
      }
    },
    mounted() {
      if (this.$cookie.get('username') == null)
        this.$router.push('/')
      this.$http.post(this.Global_Api + '/schedule/course_list', {}).then((res) => {
        this.list = res.body.course_list
        for (let i = 0; i < this.list.length; i++)
          this.course.push(this.list[i])
      });
      let data={
        "user_name": this.$cookie.get('username'),
        "user_token": this.$cookie.get('user_token')
      };
      this.$http.post(this.Global_Api + '/schedule/teacher_list', data).then((res) => {
        for(let i=0;i<res.body.teacher_list.length;i++){
          let each={
            label:res.body.teacher_list[i].teacher_name,
            value:res.body.teacher_list[i].teacher_number
          };
          this.teacher_list.push(each);
        }
      })
    },
    methods: {
      delete_time: function (e) {
        this.items.splice(e, 1)
      },
      add_del:function(index){
        //console.log(this.select_course.course_id);
        let data={
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id
        };
        this.$http.post(this.Global_Api + '/schedule/course_info', data).then((res) => {
          console.log(res.body.error_message)
          if(res.body.error_code===0){
            let val=res.body.course
            this.added=[];
            this.classrooms=[];
            this.copy_classrooms=[];
            for(let i = 0; i<val.date_and_classroom.length; i++)
            {
              this.added.push(
                {
                  id:val.date_and_classroom[i].id,
                  classroom:{
                    label:val.date_and_classroom[i].classroom.classroom_name,
                    value:val.date_and_classroom[i].classroom.classroom_id,
                    classroom_capacity: val.date_and_classroom[i].classroom.classroom_capacity
                  },
                  year:val.date_and_classroom[i].year,
                  semester:val.date_and_classroom[i].semester,
                  start_week:val.date_and_classroom[i].start_week,
                  end_week:val.date_and_classroom[i].end_week,
                  day_of_week:val.date_and_classroom[i].day_of_week,
                  start:val.date_and_classroom[i].start,
                  end:val.date_and_classroom[i].end,
                }
              );
              let data={
                capacity_range:{
                  min_capacity:val.course_capacity
                },
                course_data:{
                  year:val.date_and_classroom[i].year,
                  semester:val.date_and_classroom[i].semester,
                  start_week:val.date_and_classroom[i].start_week,
                  end_week:val.date_and_classroom[i].end_week,
                  day_of_week:val.date_and_classroom[i].day_of_week,
                  start:val.date_and_classroom[i].start,
                  end:val.date_and_classroom[i].end,
                  id:val.date_and_classroom[i].id,
                }
              };
              this.$http.post(this.Global_Api + '/schedule/classroom_list', data).then((res) => {
                if(res.body.error_code!==0)
                  console.log(res.body.error_message)
                else {
                  let arr=[];
                  for(let j = 0; j<res.body.classroom_list.length;j++) {
                    arr.push(
                      {
                        label: res.body.classroom_list[j].classroom_name,
                        value: res.body.classroom_list[j].classroom_id,
                        capacity: res.body.classroom_list[j].classroom_capacity
                      }
                    );
                  }
                  this.classrooms.push(arr);
                  //console.log(this.classrooms[i])
                  this.copy_classrooms.push(arr);
                }
              })
            }

            this.copy_added=JSON.parse(JSON.stringify(this.added)) //深拷贝

          }
        })
        this.items.splice(index, 1)
      },
      add: function () {
        this.items.push({time: '', place: ''})
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
      choose_course: function (val) {
        this.items=[];
        this.select_course = val;
        if(this.select_course.teachers.length!==0){
          let teacher={
            label:this.select_course.teachers[0].teacher_name,
            value:this.select_course.teachers[0].teacher_number
          }
          this.change_teacher = teacher;
        }
        else{
          this.change_teacher = null;
        }
        document.getElementById("change-block").style.display = "block";
        document.getElementById("title").style.display = "block";
        document.getElementById("title2").style.display = "block";
        document.getElementById("title3").style.display = "block";
        document.getElementById("change-block2").style.display = "block";
        document.getElementById("change-block3").style.display = "block";
        document.getElementById("cs_name").value = val.course_name;
        document.getElementById("cs_credit").value = val.course_credit;
        this.change_type = this.coursetype_name[this.select_course.course_type];
        //console.log(this.change_type)
        document.getElementById("cs_capacity").value = val.course_capacity;
        this.$http.get(this.Global_Api + '/entity/department_list').then((res) => {
          this.list = res.body.department_list;
          for (let i = 0; i < this.list.length; i++) {
            let dic={
              label: this.list[i].department_name,
              value: this.list[i].department_id,
            };
            this.department_list.push(dic);
            if(dic.value===this.select_course.course_department.department_id)
              this.change_department=dic;
          }
        });

        document.getElementById('cs_type').style.display = 'none';
        document.getElementById('cs_department').style.display = 'none';
        document.getElementById('cs_teacher').style.display = 'none';

        this.added=[];
        this.classrooms=[];
        this.copy_classrooms=[];
        for(let i = 0; i<val.date_and_classroom.length; i++)
        {
          this.added.push(
            {
              id:val.date_and_classroom[i].id,
              classroom:{
                label:val.date_and_classroom[i].classroom.classroom_name,
                value:val.date_and_classroom[i].classroom.classroom_id,
                classroom_capacity: val.date_and_classroom[i].classroom.classroom_capacity
              },
              year:val.date_and_classroom[i].year,
              semester:val.date_and_classroom[i].semester,
              start_week:val.date_and_classroom[i].start_week,
              end_week:val.date_and_classroom[i].end_week,
              day_of_week:val.date_and_classroom[i].day_of_week,
              start:val.date_and_classroom[i].start,
              end:val.date_and_classroom[i].end,
            }
          );
          let data={
            capacity_range:{
              min_capacity:val.course_capacity
            },
            course_data:{
              year:val.date_and_classroom[i].year,
              semester:val.date_and_classroom[i].semester,
              start_week:val.date_and_classroom[i].start_week,
              end_week:val.date_and_classroom[i].end_week,
              day_of_week:val.date_and_classroom[i].day_of_week,
              start:val.date_and_classroom[i].start,
              end:val.date_and_classroom[i].end,
              id:val.date_and_classroom[i].id,
            }
          };
          this.$http.post(this.Global_Api + '/schedule/classroom_list', data).then((res) => {
            if(res.body.error_code!==0)
              alert(res.body.error_message)
            else {
              let arr=[];
              for(let j = 0; j<res.body.classroom_list.length;j++) {
                arr.push(
                    {
                      label: res.body.classroom_list[j].classroom_name,
                      value: res.body.classroom_list[j].classroom_id,
                      capacity: res.body.classroom_list[j].classroom_capacity
                    }
                );
              }
              this.classrooms.push(arr);
              //console.log(this.classrooms[i])
              this.copy_classrooms.push(arr);
            }
          })
        }

        this.copy_added=JSON.parse(JSON.stringify(this.added)) //深拷贝
      },
      change: function (node, dochange) {
        var thisDom = node.currentTarget;
        if(dochange==="course_name"){
          if(thisDom.value!==this.select_course.course_name)
            thisDom.parentNode.lastChild.style.display = "inline-block"
          else
            thisDom.parentNode.lastChild.style.display = "none"
        }
        if(dochange==="course_credit"){
          if(parseInt(thisDom.value)!==this.select_course.course_credit)
            thisDom.parentNode.lastChild.style.display = "inline-block"
          else
            thisDom.parentNode.lastChild.style.display = "none"
        }
        if(dochange==="course_capacity"){
          if(parseInt(thisDom.value)!==this.select_course.course_capacity)
            thisDom.parentNode.lastChild.style.display = "inline-block"
          else
            thisDom.parentNode.lastChild.style.display = "none"
        }
        //alert(thisDom.value)
      },
      show: function () {
        alert(this.items[0].place)
      },
      type_change: function () {
        //alert(this.change_type.value);
        if(this.change_type !=null) {
          if (this.change_type.value !== this.select_course.course_type)
            document.getElementById('cs_type').style.display = 'inline-block'
          else
            document.getElementById('cs_type').style.display = 'none'
        }
      },
      department_change:function(){
        if(this.change_department!=null) {
          if (this.change_department.value !== this.select_course.course_department.department_id)
            document.getElementById('cs_department').style.display = 'inline-block'
          else
            document.getElementById('cs_department').style.display = 'none'
        }
      },
      teacher_change:function(){
        if( this.select_course.teachers.length === 0 ){
          if(this.change_teacher!==null)
            document.getElementById('cs_teacher').style.display = 'inline-block'
          else
            document.getElementById('cs_teacher').style.display = 'none'
        }
        else if(this.change_teacher!=null){
          if (this.change_teacher.value !== this.select_course.teachers[0].teacher_number)
            document.getElementById('cs_teacher').style.display = 'inline-block'
          else
            document.getElementById('cs_teacher').style.display = 'none'
        }
      },
      confirm_name: function () {
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "course_name": document.getElementById("cs_name").value
        };
        this.$http.post(this.Global_Api + '/schedule/change_course_name', data).then((res) => {
          alert(res.body.error_message);
          if(res.body.error_code===0) {
            data = {};
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
              document.getElementById('cs_name_but').style.display = 'none';
              //console.log(this.select_course.course_id)
              this.select_course = this.course[this.select_course.course_id-1];
              //console.log(this.select_course.course_name)
            })
          }
        })
      },
      confirm_credit: function () {
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "course_credit": parseInt(document.getElementById("cs_credit").value)
        };
        this.$http.post(this.Global_Api + '/schedule/change_course_credit', data).then((res) => {
          alert(res.body.error_message);
          if(res.body.error_code===0) {
            data = {};
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
                this.course.push(this.list[i]);
              document.getElementById('cs_credit_but').style.display = 'none';
              this.select_course = this.course[this.select_course.course_id-1];
            })
          }
        })
      },
      confirm_capacity: function () {
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "course_capacity": parseInt(document.getElementById("cs_capacity").value)
        };
        this.$http.post(this.Global_Api + '/schedule/change_course_capacity', data).then((res) => {
          alert(res.body.error_message);
          if(res.body.error_code===0) {
            data = {};
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
              document.getElementById('cs_capacity_but').style.display = 'none';
              this.select_course = this.course[this.select_course.course_id-1];
            })
          }
        })
      },
      confirm_type: function () {
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "course_type": this.change_type.value
        };
        this.$http.post(this.Global_Api + '/schedule/change_course_type', data).then((res) => {
          alert(res.body.error_message);
          if(res.body.error_code===0) {
            data = {};
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
              document.getElementById('cs_type').style.display = 'none';
              this.select_course = this.course[this.select_course.course_id-1];
            })
          }
        })
      },
      confirm_department: function () {
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "course_department_id": this.change_department.value
        };
        this.$http.post(this.Global_Api + '/schedule/change_course_department', data).then((res) => {
          alert(res.body.error_message);
          if(res.body.error_code===0) {
            data = {};
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
              document.getElementById('cs_department').style.display = 'none';
              this.select_course = this.course[this.select_course.course_id-1];
            })
          }
        })
      },
      confirm_teacher:function(){
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "teacher_number": this.change_teacher.value
        };
        this.$http.post(this.Global_Api + '/schedule/course_add_teacher', data).then((res) => {
          alert(res.body.error_message);
          if(res.body.error_code===0) {
            data = {};
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
              document.getElementById('cs_teacher').style.display = 'none';
              this.select_course = this.course[this.select_course.course_id-1];
            })
          }
        })
      },
      added_change:function(index){
        if(
          this.added[index].start_week!==this.copy_added[index].start_week ||
          this.added[index].end_week!==this.copy_added[index].end_week ||
          this.added[index].day_of_week!==this.copy_added[index].day_of_week ||
          this.added[index].start!==this.copy_added[index].start ||
          this.added[index].end!==this.copy_added[index].end ||
          this.added[index].classroom.value!==this.copy_added[index].classroom.value
        ) {
          // console.log(false)
          let data={
            capacity_range:{
              min_capacity:this.select_course.course_capacity
            },
            course_data:{
              year:this.added[index].year,
              semester:this.added[index].semester,
              start_week:this.added[index].start_week,
              end_week:this.added[index].end_week,
              day_of_week:this.added[index].day_of_week,
              start:this.added[index].start,
              end:this.added[index].end,
              id:this.added[index].id,
            }
          };
          this.$http.post(this.Global_Api + '/schedule/classroom_list', data).then((res) => {
            if(res.body.error_code!==0)
              console.log(res.body.error_message)
            else {
              let arr=[];
              for(let j = 0; j<res.body.classroom_list.length;j++) {
                arr.push(
                  {
                    label: res.body.classroom_list[j].classroom_name,
                    value: res.body.classroom_list[j].classroom_id,
                    capacity: res.body.classroom_list[j].classroom_capacity
                  }
                );
              }
              this.classrooms[index]=JSON.parse(JSON.stringify(arr));
            }
          });
          document.getElementsByClassName("added")[index].style.display = "inline-block"
        }
        else {
          // console.log(true);
          document.getElementsByClassName("added")[index].style.display = "none";
          //console.log(this.classrooms[index])
          if(typeof this.classrooms[index] !=="undefined")  //解决选择课程后初始化会抛错
            this.classrooms[index]=JSON.parse(JSON.stringify(this.copy_classrooms[index]));
        }
      },
      confirm_change:function (index) {
        //console.log(this.added[index].classroom.value)
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.select_course.course_id,
          "classroom_id": this.added[index].classroom.value,
          "id": this.added[index].id,
          "date": {
            "end": this.added[index].end,
            "start": this.added[index].start,
            "day_of_week": this.added[index].day_of_week,
            "end_week": this.added[index].end_week,
            "start_week": this.added[index].start_week,
          }
        };
        this.$http.post(this.Global_Api + '/schedule/course_add_dc', data).then((res) => {
          alert(res.body.error_message)
          if(res.body.error_code===0) {
            document.getElementsByClassName("added")[index].style.display = "none";
            this.copy_added[index]=JSON.parse(JSON.stringify(this.added[index]));
            console.log(this.added[index].classroom);
            console.log(this.copy_added[index].classroom);
            data = {};
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
          }
        })
      },
      delete_added:function (index) {
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "id": this.added[index].id,
        };
        this.$http.post(this.Global_Api + '/schedule/del_dc', data).then((res) => {
          alert(res.body.error_message)
          if(res.body.error_code===0) {
            this.added.splice(index, 1);
            this.copy_added.splice(index, 1);
            data = {};
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
          }
        })
      }
    }
  }
</script>

<style scoped>
  .hello {
    animation: donghua 1s;
  }

  * {
    list-style: none;
    text-decoration: none;
    color: black;
    outline: 0 none;
  }

  a {
    text-decoration: none;
    outline: 0 none;
  }

  a:hover {
    color: black;
  }

  li {
    display: block;
    height: 50px;
    width: 313px;
    border-left: 0px solid black;
    border-bottom: 0px solid black;
    border-right: 0px solid black;
    line-height: 50px;
    padding: 0;
  }

  li::before {
    content: "";
    display: inline-block;
    width: 30px;
  }

  ul {
    margin-left: -55px;
  }

  li:hover {
    background: #f5f5f5;
  }

  ::-webkit-scrollbar {
    width: 0px; /* Remove scrollbar space */
    background: transparent; /* Optional: just make scrollbar invisible */
  }

  #cs_type {
    display: none;
  }

  #cnmx {
    margin-left: 15%;
    margin-top: 30px;
    height: 600px;
    width: 300px;
    float: left
  }

  #selecttype {
    padding: 0;
    margin: 10px;
  }

  #xianshi {
    border: 1px solid #ddd;
    position: absolute;
    width: 50%;
    height: 79.5%;
    margin-left: 40%;
    margin-top: 31px;
  }

  #change-block, #change-block2, #change-block3{
    border: 3px solid #f5f5f5;
    width: 90%;
    height: 75%;
    display: none;
    margin: 0 auto;
    margin-top: 15px;
    background-color: #f5f5f5;
    animation: donghua 1s;
  }

  .hello {
    margin-left: 34px;
    width: 90%;
  }

  #change-block span,
  #change-block2 span {
    font-weight: bold;
  }
  #change-block3 span {
    font-weight: bold;
  }

  li {
    cursor: pointer;
  }

  .change-content {
    border-bottom: 1px solid #ddd;
    margin: 30px 10%;
    padding: 5px;
  }

  .btn-info {
    display: none;
    margin-left: 50px;
    height: 30px;
    vertical-align: 0px;
    animation: donghua 2s;
  }

  #change-block v-select {
    width: 50px;
  }

  #title, #title2 ,#title3{
    animation: donghua 2s;
  }

  @keyframes donghua {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  .form-control, .form-select {
    width: 250px;
    display: inline-block;
  }

  #change-block {
    margin-bottom: 50px;
  }

  #title, #title2,#title3 {
    border-left: 2px solid rgb(35, 149, 241);
    padding-left: 10px;
  }

  .btn2 {
    width: 35px;
    border: 0;
    height: 35px;
    line-height: 35px;
    border-radius: 5px;
    font-size: 22px;
    margin: 25px;
    color: white;
  }
  .select-pt{
    white-space: nowrap;
    width: 150px;
    display: inline-block;
    margin-bottom: 25px;
    margin-right: 10px;
  }
  .btn5{
    width: 60px;
    border: 0;
    height: 30px;
    line-height: 30px;
    border-radius: 5px;
    font-size: 17px;
    margin-left: 25px;
    margin-right: 25px;
    color: white;
  }

</style>
