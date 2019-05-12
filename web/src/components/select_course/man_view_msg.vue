<template>
    <div id="man_view_msg">
      <PC_bar></PC_bar>

      <div class="panel panel-primary" style="margin: 0 auto">
        <div class="panel-heading" ><strong class="panel-title">基本信息栏</strong> </div>
            <li class="list-group-item">专业：</li>
            <li class="list-group-item">专业号：</li>
            <li class="list-group-item">课程容量</li>
            <li class="list-group-item">授课教师：</li>
            <li class="list-group-item">授课学院：</li>
      </div>

      <div class="panel panel-primary" style="margin: 0 auto">
        <div class="panel-heading"><strong class="panel-title">说明栏</strong></div>
          <li class="list-group-item">教师：</li>
          <li class="list-group-item">专业：</li>
        <li class="list-group-item" ><font class="fa fa-camera-retro">学院：</font></li>
      </div>

        <div class="panel panel-primary" style="margin: 0 auto">
          <div class="panel-heading" ><strong class="panel-title">报表</strong> </div>
          888
        </div>

      <div style="margin: 10px auto">
        <button  style="display:block;margin:0 auto">
          <font style="font-size: 15px"> <router-link to ="/main/man_sel_course" >返回</router-link></font></button>
      </div>
    </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  export default {
    name: "man_view_msg",
    components:{
      "PC_bar":PC_bar,
    },
    data () {
      return {
        msg: {}
      }
    }
  }
</script>

<style scoped>
#man_view_msg{
  margin: 0 auto;
  background: whitesmoke;
  max-width: 960px;
  padding :5px;

}
  .panel-title{
    font: bold 18px Georgia, serif;
  }

</style>
