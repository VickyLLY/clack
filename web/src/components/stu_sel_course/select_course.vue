<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <a class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="">排课子系统</a></li>
        <li>
          <a href="select_course.vue">选课子系统</a>
        </li>
        <li><a href="">后台管理子系统</a></li>
        <li><a href="">毕业设计管理子系统</a></li>
        <li><a href="">成绩管理子系统</a></li>
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
    <div id="aside" class="container left" style="width:700px;height:700px;border:1px solid red;position:relative;top:100px;" >
    <div class="row">
      <div class="col-lg-1" style="background: red;height:700px;vertical-align:">
        <p style="width: 20px;height: 100px">选课信息</p>
        <p style="width: 20px;height: 100px;">已选</p>
      </div>
      <div class="col-lg-6">

      </div>
    </div>
  </div>
  </div>
</template>


<script>
  window.onload=function ()
  {
    var oDiv1=document.getElementById('aside');

    oDiv1.onmouseover=function ()
    {
      startMove(this, 'left', 700);
    };
    oDiv1.onmouseout=function ()
    {
      startMove(this, 'left', 200);
    };
  };

  function getStyle(obj, name)
  {
    if(obj.currentStyle)
    {
      return obj.currentStyle[name];
    }
    else
    {
      return getComputedStyle(obj, false)[name];
    }
  }
  function startMove(obj, attr, iTarget)
  {
    clearInterval(obj.timer);
    obj.timer=setInterval(function (){
      var cur=0;

      if(attr==='opacity')
      {
        cur=parseFloat(getStyle(obj, attr))*100;
      }
      else
      {
        cur=parseInt(getStyle(obj, attr));
      }

      var speed=(iTarget-cur)/6;
      speed=speed>0?Math.ceil(speed):Math.floor(speed);

      if(cur===iTarget)
      {
        clearInterval(obj.timer);
      }
      else
      {
        if(attr==='opacity')
        {
          obj.style.filter='alpha(opcity:'+(cur+speed)+')';
          obj.style.opacity=(cur+speed)/100;
          document.getElementById('txt1').value=obj.style.opacity;
        }
        else
        {
          obj.style[attr]=cur+speed+'px';
        }
      }
    }, 30);
  }
  export default {
    name: "select_course",
    data() {
      return {
        username: this.$cookie.get('username'),
        realname: this.$cookie.get('realname'),
      }
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
    },
  }
</script>

<style scoped>

</style>
