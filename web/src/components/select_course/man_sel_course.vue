<template>
  <div id="man_sel_course">
    <PC_bar></PC_bar>
    <div class="search">
      <form>
        <div class="form">
          <div class="year">
            <span class="red">*</span>
            <label>学年</label>
            <select v-model="info.year" class="select">
              <option value="all">全部</option>
              <option value="2022">2022-2023</option>
              <option value="2021">2021-2022</option>
              <option value="2020">2020-2021</option>
              <option value="2019">2019-2020</option>
              <option value="2018">2018-2019</option>
              <option value="2017">2017-2018</option>
              <option value="2016">2016-2017</option>
              <option value="2015">2015-2016</option>
              <option value="2014">2014-2015</option>
              <option value="2013">2013-2014</option>
              <option value="2012">2012-2013</option>
              <option value="2011">2011-2012</option>
              <option value="2010">2010-2011</option>
              <option value="2009">2009-2010</option>
              <option value="2008">2008-2009</option>
              <option value="2007">2007-2008</option>
              <option value="2006">2006-2007</option>
              <option value="2005">2005-2006</option>
              <option value="2004">2004-2005</option>
            </select>
          </div>

          <div class="academy">
            <span class="red">*</span>
            <label>学院</label>
            <select  v-model="info.academy" class="select">
              <option value="all" selected="selected">全部</option>
              <option value="化学工程学院">化学工程学院</option>
              <option value="材料科学与工程学院">材料科学与工程学院</option>
              <option value="机电工程学院">机电工程学院</option>
              <option value="信息学院">信息学院</option>
              <option value="经济管理学院">经济管理学院</option>
              <option value="理学院">理学院</option>
              <option value="文法学院">文法学院</option>
              <option value="生命科学与技术学院">生命科学与技术学院</option>
              <option value="马克思主义学院">马克思主义学院</option>
              <option value="国际教育学院">国际教育学院</option>
              <option value="巴黎居里工程师学院">巴黎居里工程师学院</option>
            </select>
          </div>

          <div class="semester">
            <span class="red">*</span>
            <label>学期</label>
            <select  v-model="info.semester" class="select">
              <option value="1" selected="selected">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
            </select>
          </div>

        </div>
        <div class="form">
          <div class="course">
            <label>课程</label>
            <input v-model="info.course" type="text" placeholder=" 请输入课程名称查询">
          </div>

          <div class="teacher">
            <label>教师</label>
            <input v-model="info.teacher" type="text" placeholder=" 请输入老师名字查询">
          </div>
        </div>

      </form>
    </div>
    <div class="button">
      <button v-on:click="Filter()" type="button" id="btn1" class="btn btn-primary " >查询</button>
    </div>
    <div class="table-responsive table" style="overflow: scroll; -webkit-overflow-scrolling: touch;height: 400px">
      <table class="table table-striped table-item ">
        <thead>
        <tr>
          <th>序号</th>
          <th>课程名称</th>
          <th>课程号</th>
          <th>学分</th>
          <th>任课老师</th>
          <th>上课教室</th>
          <th>起始周</th>
          <th>结束周</th>
          <th>学年</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(course,index) in courses">
          <router-link to="/main/man_sel_course/man_view_msg" >
            <td @click="confirm(index)"><font style="margin:0 auto;text-align:center">{{index}}</font></td>
          </router-link>
          <td>{{course.course_name}}</td>
          <td>{{course.course_id}}</td>
          <td>{{course.course_credit}}</td>
          <td>{{course.course_teacher}}</td>
          <td>{{course.classroom_id}}</td>
          <td>{{course.start_week}}</td>
          <td>{{course.end_week}}</td>
          <td>{{course.course_year}}</td>

        </tr>
        </tbody>
      </table>
      <hr>
      <div class="table-border" v-show="!border_show">
        <p v-show="!conditionText">请选择筛选条件!</p>
        <p v-show="infoText">没有查询到相关信息！</p>
      </div>
    </div>

    <div>

    </div>

  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  import bus from "../../assets/manager_to_manager"

  export default {
    name: "man_sel_course",
    data () {
      return {
        info:{
          year:"all",
          academy:"all",
          semester:"1",
          course:"",
          teacher:"",
        },
        course_list:[],
        courses:[],
        update_courseList:[],
        flag:-1,
        info_collection:{"course_name":"","course_teacher":"","year":"","academy":"","semester":""},
        border_show:false,
        conditionText:false,
        infoText:false,
        data:{}
      }
    },
    methods:{
      confirm:function(index){
        this.$router.push('/main/man_sel_course/man_view_msg')
        this.data=this.update_courseList[index]
        console.log("赋值")
        console.log(this.data)
      },
      Filter:function () {
        this.border_show=true;
        if (this.info.year=="all"&&this.info.academy=="all"){
          alert("请指定year和academy！");
          return ;
        }
        else if(this.info.year=="all")
        {
          alert("请指定year！");
          return ;
        }
        else if(this.info.academy=="all"){
          alert(("请指定academy！"));
          return ;
        }
        // this.courses=this.course_list;
        console.log(this.course_list);

        if(this.info.year!="all"&&this.info.academy!="all"){
          this.info_collection.year=this.info.year;
          this.info_collection.academy=this.info.academy;
        }
        this.info_collection.semester=this.info.semester;

        if(this.info.course!=""){
          this.info_collection.course_name=this.info.course;
        }
        else {
          this.info_collection.course_name="null"
        }

        if(this.info.teacher!=""){
          this.info_collection.course_teacher=this.info.teacher;
        }
        else {
          this.info_collection.course_teacher="null";
        }

        // console.log(this.info_collection.year);
        console.log(this.info_collection.academy);
        // console.log(this.info_collection.semester);
        // console.log(this.info_collection.course_name);
        // console.log(this.info_collection.course_teacher);

        //过滤年份
        this.course_list = this.course_list.filter((kecheng) => {
          // console.log("过滤年份"+kecheng.course_year);
          return kecheng.course_year==this.info_collection.year;
        });

        console.log(this.course_list);

        // //过滤学院
        // this.course_list = this.course_list.filter((kecheng) => {
        //   // console.log("过滤学院"+kecheng.course_department.department_name);
        //   return kecheng.course_department.department_name == this.info_collection.academy;
        // });
        //
        // console.log(this.course_list);


        //过滤学期
        this.course_list = this.course_list.filter((kecheng) => {
          console.log(kecheng.course_department.department_name);
          return kecheng.course_semester==this.info_collection.semester;
        });


        console.log(this.course_list);

        //过滤课程
        if(this.info_collection.course_name!="null") {
          this.course_list = this.course_list.filter((kecheng) => {
            // console.log("过滤课程"+kecheng.course_name);
            return kecheng.course_name.match(this.info_collection.course_name)
          });
        }

        if(this.info_collection.course_teacher!="null"){
          this.course_list=this.course_list.filter((kecheng) => {
            // console.log("过滤老师"+kecheng.course_name);
            return kecheng.course_teacher.match((this.info_collection.course_teacher))
          })
        }
        this.courses=this.course_list;
        this.update_courseList=this.course_list;

        if(this.courses.length==0)
        {
          this.border_show=false;
          this.conditionText=true;
          this.infoText=true;
        }
        this.$http.post(this.Global_Api + '/schedule/course_list',[])
          .then((res)=>{
              this.course_list=res.body.course_list;
            }
          );
      }

    },
    created()
    {
      this.$http.post(this.Global_Api + '/schedule/course_list',[])
        .then((res)=>{
            this.course_list=res.body.course_list;
            console.log(this.course_list)
          }
        );
    },
    beforeDestroy () {
      console.log('A before destroy')
      bus.$emit("getData",this.data);
    },

    components:{
      "PC_bar":PC_bar,
    }
  }
</script>

<style scoped>
  .search{
    margin: 30px auto;
    padding: 10px 10px;
    max-width: 1200px;
    border: 1px solid #eeeeee;
  }
  .form{
    display: flex;
    flex-direction: row;
    margin: 30px auto;
    position: relative;
    left: 40%;
  }
  input[type="text"]{
    border-radius: 5px;
    border: 1px solid #e3e3e3;
    padding: 4px;
    width: 200px;
  }
  .button{
    background: #f5f5f5;
    padding: 10px;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    bottom: 30px;
  }
  #btn1{
    position: relative;
    left: 95%;
  }
  .red{
    color: crimson;
  }
  .table{
    max-width: 1200px;
    margin: 20px auto;
    padding:10px;

  }
  thead{
    border: 1px solid #e3e3e3;
  }
  th{
    border: 1px solid #e3e3e3;
  }
  tbody{
    border: 1px solid #2aabd2;
  }
  select{
    height: 30px;
    width: 200px;
    background: white;
    border: 1px solid #e3e3e3;

    /*appearance:none;*/
  }
  .table-border{
    height: 100px;
    max-width: 1200px;
    margin: 0 auto;
    border: 2px solid #e3e3e3;
    position: relative;
    bottom: 45px;
  }
  .year{
    position: relative;
    right: 350px;
  }
  .academy{
    position: relative;
    right: 180px;
  }
  .course{
    position: relative;
    right: 340px;
  }
  .teacher{
    position: relative;
    right: 160px;
  }
  .semester{
    position: relative;
    right: 30px;
  }
  hr{
    height: 1px;
    background-color: #2aabd2;
    width: 1180px;
    position: relative;
    bottom: 22px;
  }
  p{
    text-align: center;
    line-height: 100px;
  }

</style>



