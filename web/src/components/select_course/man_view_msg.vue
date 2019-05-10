<template>
    <div id="man_view_msg">
      <PC_bar></PC_bar>

      <div class="panel panel-primary" style="margin: 0 auto">
        <div class="panel-heading" ><strong class="panel-title">基本信息栏</strong> </div>
            <li class="list-group-item">专业名称：{{msg.course_name}}</li>
            <li class="list-group-item">授课教师：{{msg.course_teacher}}</li>
            <li class="list-group-item">授课学院：{{msg.course_department}}</li>
            <li class="list-group-item">课程容量:{{msg.course_capacity}}</li>
      </div>

      <div class="panel panel-primary" style="margin: 0 auto">
        <div class="panel-heading"><strong class="panel-title">介绍栏</strong></div>
          <li class="list-group-item">教师：</li>
          <li class="list-group-item">专业：</li>
        <li class="list-group-item" ><font class="fa fa-camera-retro">学院：</font></li>
      </div>

        <div class="panel panel-primary" style="margin: 0 auto">
          <div class="panel-heading" ><strong class="panel-title">报表</strong> </div>
             <canvas id="canvas"  width="300" height="400" ></canvas>
              <font style="font-size: 15px;font-style: oblique;">已选容量（红色区域{{percent[0]*100+"%"}}）：{{list[1]	}}
                剩余容量（黄色区域{{percent[1]*100+"%"}}）:{{list[0]-list[1]}}</font>

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
      "PC_bar":PC_bar
    },

    data () {
      return {
        msg: {
          course_name:"computer",
          course_teacher: "万七",
          course_department:"信院",
          course_capacity: "150"

        },

        list:[100,75],
        percent:[]
      }
    },

    props: {
      info: {
        type:Object,
        required:true
      }
    },

    // created(){
    //   this.$http.get(this.Global_Api + '/selecourse/admin_reports', {year:"",
    //     semester:"",course_department:"",teacher_name:"",course_name:""
    //   }).then((res) => {
    //     this.list = res.body;})
    // },
    mounted() {
      this.percent = [this.list[1]/this.list[0],(this.list[0]-this.list[1])/this.list[0]];
      this.drawCircle(this.percent);
    },

    methods: {
      drawCircle: function (list) {
        var color = ['#FF0000', '#EEEE00'];
        var precent = list;

        var can = document.getElementById("canvas");
        //document.getElementById( id名 )是获取id属性值为“id名”的标签，而document.getElementById( id名 ).value是获取该标签的value值

        var ctx = can.getContext('2d');
        //2D Context的 坐标开始于元素的左上角，原点坐标是(0,0)。所有坐标值都基于这个原点计算，x 方向自左向右为正，y 方向自上而下为正。

        var radius = can.width * 0.5 - 20; //半径
        ctx.clearRect(0,0,300,400);
        var ox = radius + 20; //圆心x
        var oy = radius + 20; //圆心y
        var startAngle = 0; //开始
        var endAngle = 0; //结束

        for(var i = 0; i < color.length; i++) {
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
