<template>
    <div id="man_sel_course">
      <PC_bar></PC_bar>
      <div class="serach">
          <form class="form">
            <div class="label-one">
              <span class="red">*</span>
            <label>课程</label>
            <input class="serach-one" type="text" placeholder=" 请输入课程名称查询">
            </div>
            <div class="label-two">
              <span class="red">*</span>

              <label>教师</label>
            <input class="search-two" type="text" placeholder=" 请输入老师名字查询">
            </div>
          </form>
      </div>
      <div class="button">
        <button type="button" id="btn1" class="btn btn-primary ">查询</button>
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
          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>
          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>          <tr>
            <th>1</th>
            <th>1</th>
            <th>1</th>
            <th>1</th>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
    export default {
      name: "man_sel_course",
      components:{
          "PC_bar":PC_bar,
      }
    }
</script>

<style scoped>
.serach{
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
    width: 300px;
  }
  .label-one{
    position: relative;
    right: 30%;
  }

.label-two{
  position: relative;
  right: 7%;
}
  .button{
    background: #eeeeee;
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
    /*border:1px solid #e3e3e3;*/
    padding:10px;

  }
  .table-item{
    border: 1px solid #e3e3e3;
  }


</style>
