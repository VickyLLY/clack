<template>
  <div id="man_view_msg">
    <PC_bar></PC_bar>

    <div class="panel panel-primary" style="margin: 0 auto">
      <div class="panel-heading" ><strong class="panel-title">基本信息栏</strong> </div>
      <li class="list-group-item">课程名：{{msg.course_name}}</li>
      <li class="list-group-item">课程号：{{msg.course_id}}</li>
      <li class="list-group-item">课程容量:{{" "+msg.course_capacity}}</li>
      <li class="list-group-item">授课教师：{{teacher_name}}</li>
      <li class="list-group-item">授课学院：{{department_name}}</li>
    </div>

    <!--<div class="panel panel-primary" style="margin: 0 auto">-->
      <!--<div class="panel-heading"><strong class="panel-title">介绍栏</strong></div>-->
      <!--<li class="list-group-item">教师：</li>-->
      <!--<li class="list-group-item">专业：</li>-->
      <!--<li class="list-group-item" ><font class="fa fa-camera-retro">学院：</font></li>-->
    <!--</div>-->

    <div class="panel panel-primary" style="margin: 0 auto">
      <div class="panel-heading" ><strong class="panel-title">报表</strong> </div>
        <div style="margin-top:10px;margin-bottom: 0px"><font style="font-size: 15px;font-style: oblique;text-align:center;">
            <p>已选容量（红色区域{{(percent[0]*100).toFixed(2)+"%"}}）：{{list[1]}}</p>
            <p>剩余容量（黄色区域{{(percent[1]*100).toFixed(2)+"%"}}）:{{list[0]-list[1]}}</p></font></div>
        <canvas id="canvas"  width="300" height="400" ></canvas>
    </div>

    <div style="margin: 10px auto">
      <button  style="display:block;margin:0 auto">
        <font style="font-size: 15px"> <router-link to ="/main/man_sel_course" >返回</router-link></font></button>
    </div>

  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  import bus from "../../assets/manager_to_manager";

  export default {
    name: "man_view_msg",
    components:{
      "PC_bar":PC_bar,
    },
    data () {
      return {
        msg: {},
        list:[],
        percent:[],
        teacher_name: "",
        department_name :"",
      }
    },
    created() {
      // bus.$on("getData",(data)=>this.getData(data))
      this.msg=this.$route.params.msg
    },

    mounted() {
      console.log("mounted周期后的值")
      this.getd();
      console.log(this.msg)
      this.$http.post(this.Global_Api + '/selecourse/admin_reports', {
        year:this.msg.course_year,
        semester:this.msg.course_semester,
        department_name:this.msg.course_department.department_name,
        teacher_name:this.teacher_name,
        course_name:this.msg.course_name
      }).then(res => {
        console.log("报表取数据")
        console.log(res)

        this.list[0]= res.body.reports_list[0].course_capacity;
        this.list[1]= res.body.reports_list[0].course_allowance;
        console.log("查看报表数据")
        console.log(this.list)

        console.log("画图开始")
        this.percent = [this.list[1]/this.list[0],(this.list[0]-this.list[1])/this.list[0]];
        this.drawCircle(this.percent);
      })

    },

    methods: {
      getData(data){
        this.msg=data
        this.teacher_name=data.teachers[0].teacher_name
        this.department_name=data.course_department.department_name
        console.log("jieshou")
        console.log(data)
      },

      getd:function(){
        this.msg = this.$route.params.msg
        this.teacher_name=this.msg.teachers[0].teacher_name
        this.department_name=this.msg.course_department.department_name
        console.log("jieshou")
        console.log(this.msg)
      },

      drawCircle: function (list) {
        var color = ['#FF0000', '#EEEE00'];
        var precent = list;

        var can = document.getElementById("canvas");
        //document.getElementById( id名 )是获取id属性值为“id名”的标签，而document.getElementById( id名 ).value是获取该标签的value值

        var ctx = can.getContext('2d');
        //2D Context的 坐标开始于元素的左上角，原点坐标是(0,0)。所有坐标值都基于这个原点计算，x 方向自左向右为正，y 方向自上而下为正。

        var radius = can.width * 0.5 - 20; //半径
        ctx.clearRect(0, 0, 300, 400);
        var ox = radius + 20; //圆心x
        var oy = radius + 20; //圆心y
        var startAngle = 0; //开始
        var endAngle = 0; //结束

        for (var i = 0; i < color.length; i++) {
          endAngle = endAngle + precent[i] * Math.PI * 2;
          ctx.fillStyle = color[i];	//设置填充颜色
          ctx.beginPath();			//表示要开始绘制新路径
          ctx.moveTo(ox, oy);	//从圆点移动到圆心，moveTo函数会将点移动到指定位置，但是不绘画路径
          ctx.arc(ox, oy, radius, startAngle, endAngle, false);
          //圆心(ox,oy),半径radius，角度(startAngle, endAngle)（用弧度表示）,顺时针（false）
          ctx.closePath();
          //返回画笔开始处,closePath() 方法创建从当前点到开始点的路径
          ctx.fill();//填充图像
          console.log(startAngle, endAngle, 'dd')
          startAngle = endAngle;
          console.log(precent)
        }
      }
    },

    destroyed () {
      console.log('%c%s', 'background: yellow;', 'B beforecreate！')
      bus.$off('getData')
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

  #canvas {
    position: relative;
    left: 36%;
    top: 50%;
  }
</style>

