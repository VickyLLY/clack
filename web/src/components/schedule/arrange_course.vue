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
                <li class="list-group-item" v-for="name in course" >
                  <a href="javascript:void(0)" @click="fun">{{ name }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div id="xianshi" class="panel-heading">
              <div id="change-block">
                课程名字：<input id="name-course" type="text" value="">
                <button type="button" class="btn btn-info" style="color: white">√</button>
              </div>
        </div>
  </div>
</template>

<script>
    import get_coursetype from './get_coursetype'
    import get_year_semester from './get_year_semester'
    import PC_bar from '../public/PC_bar'
    import department_list from '../public/department_list'
    export default {
        name: "arrange_course",
        components:{
          get_year_semester,
          PC_bar,
          department_list,
          get_coursetype,
        },
        data(){
          return{
            year:undefined,
            semester:undefined,
            department_id:undefined,
            coursetype:undefined,
            list:'',
            course:[]
          }
        },
        mounted(){
          this.$http.post(this.Global_Api + '/schedule/course_list', {}).then((res) => {
            this.list=res.body.course_list
            for(let i=0;i<this.list.length;i++)
              this.course.push(this.list[i].course_name)
            //alert(this.course.length)
          })
        },
        methods:{
          year_semester(val) {
            if(val!=null) {
              this.year = val.year;
              this.semester = val.semester;
            }
            else{
              this.year=undefined;
              this.semester=undefined
            }
            let data={};
            if(typeof(this.year)!="undefined")
              data['course_year']=this.year;
            if(typeof(this.semester)!="undefined")
              data['course_semester']=this.semester;
            if(typeof(this.department_id)!="undefined")
              data['course_department_id']=this.department_id;
            if(typeof(this.coursetype)!="undefined")
              data['course_type']=this.coursetype;
            this.course=[];
            this.$http.post(this.Global_Api + '/schedule/course_list', data).then((res) => {
              this.list=res.body.course_list
              for(let i=0;i<this.list.length;i++)
                this.course.push(this.list[i].course_name)
            })
          },
          department(val){
            if(val!=null)
              this.department_id=val;
            else
              this.department_id=undefined;
            let data={};
            if(typeof(this.year)!="undefined")
              data['course_year']=this.year;
            if(typeof(this.semester)!="undefined")
              data['course_semester']=this.semester;
            if(typeof(this.department_id)!="undefined")
              data['course_department_id']=this.department_id;
            if(typeof(this.coursetype)!="undefined")
              data['course_type']=this.coursetype;
            this.course=[];
            this.$http.post(this.Global_Api + '/schedule/course_list', data).then((res) => {
              this.list=res.body.course_list
              for(let i=0;i<this.list.length;i++)
                this.course.push(this.list[i].course_name)
            })
          },
          course_type(val){
            if(val!=null)
              this.coursetype=val.coursetype;
            else
              this.coursetype=undefined;
            let data={};
            if(typeof(this.year)!="undefined")
              data['course_year']=this.year;
            if(typeof(this.semester)!="undefined")
              data['course_semester']=this.semester;
            if(typeof(this.department_id)!="undefined")
              data['course_department_id']=this.department_id;
            if(typeof(this.coursetype)!="undefined")
              data['course_type']=this.coursetype;
            this.course=[];
            this.$http.post(this.Global_Api + '/schedule/course_list', data).then((res) => {
              this.list=res.body.course_list
              for(let i=0;i<this.list.length;i++)
                this.course.push(this.list[i].course_name)
            })
          },
          fun:function () {
            document.getElementById("change-block").style.display="block";
            document.getElementById("name-course").value=this.innerText;
          }
        }
    }
</script>

<style scoped>
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
  margin-left:60px;
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
  width: 1100px;
  height: 605px;
  margin-left: 383px;
  margin-top: 31px;
}
  #change-block{
    border: 3px solid #f5f5f5;
    width: 1000px;
    height: 550px;
    display: none;
    margin: 20px auto;
  }

</style>
