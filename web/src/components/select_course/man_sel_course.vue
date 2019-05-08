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
                <option value="01">化学工程学院</option>
                <option value="02">材料科学与工程学院</option>
                <option value="03">机电工程学院</option>
                <option value="04">信息科学与技术学院</option>
                <option value="05">经济管理学院</option>
                <option value="06">理学院</option>
                <option value="07">文法学院</option>
                <option value="08">生命科学与技术学院</option>
                <option value="09">马克思主义学院</option>
                <option value="10">国际教育学院</option>
                <option value="11">巴黎居里工程师学院</option>
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
        <button v-on:click="Filter()" type="button" id="btn1" class="btn btn-primary ">查询</button>
      </div>
      <div class="table-responsive table" style="overflow: scroll; -webkit-overflow-scrolling: touch;height: 400px">
        <table class="table table-striped table-item">
          <thead>
          <tr>
            <th>课程名称</th>
            <th>课程号</th>
            <th>任课老师</th>
            <th>上课教室</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="course in courses">
            <td>{{course.课程名称}}</td>
            <td>{{course.课程号}}</td>
            <td>{{course.任课老师}}</td>
            <td>{{course.上课教室}}</td>

          </tr>
          </tbody>
        </table>
      </div>


      <div>
        {{info.year}}
        {{info.academy}}
        {{info.course}}
        {{info.teacher}}
        {{info.semester}}
      </div>
    </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
    export default {
      name: "man_sel_course",
      data () {
        return {
          info:{
            year:"all",
            academy:"all",
            course:"null",
            teacher:"null",
            semester:"1"
          },
          courses:[],
          flag:-1,
          info_collection:{"课程名称":"a","任课老师":"t","学年":"2010","学院":"01"}
        }
      },
      methods:{
        Filter:function () {
          this.courses=[
            {"课程名称":"a","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2010","学院":"01"},
            {"课程名称":"a","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2010","学院":"02"},
            {"课程名称":"a","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2012","学院":"02"},
            {"课程名称":"a","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2011","学院":"01"},
            {"课程名称":"a","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2011","学院":"03"},
            {"课程名称":"bb","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2011","学院":"01"},
            {"课程名称":"b","课程号":"01","任课老师":"t","上课教室":"aa","学年":"2012","学院":"04"},
          ]
          if (this.info.year=="all"&&this.info.academy=="all"){
            alert("请指定学年和学院！");
            return ;
          }
          else if(this.info.year=="all")
          {
            alert("请指定学年！");
            return ;
          }
          else if(this.info.academy=="all"){
            alert(("请指定学院！"));
            return ;
          }

          if(this.info.year!="all"&&this.info.academy!="all"){
            this.info_collection.学年=this.year;
            this.info_collection.学院=this.academy;
          }
          if(this.info.course!="null"){
            this.info_collection.课程名称=this.info.course;
          }
          else {
            this.info_collection.课程名称="null"
          }

          if(this.info.teacher!="null"){
            this.info_collection.任课老师=this.info.teacher;
          }
          else {
            this.info_collection.任课老师="null";
          }

          var new_courses=[];
          new_courses=this.courses.filter(
            function (courses) {
            return courses.课程名称=="b";
          }
          );
          this.course=new_courses;
        }
      },
      computed:{

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
  .table-item{
    border: 1px solid #e3e3e3;
  }
  select{
    height: 30px;
    width: 200px;
    background: white;
    border: 1px solid #e3e3e3;

    /*appearance:none;*/
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


</style>
