<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top">
      <a class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="">本科生选课</a></li>
        <li><a href="">研究生选课</a></li>
        <li><a href="">查看课表</a></li>
        <li><a href="">其他注意事项</a></li>

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
        <div class="col-lg-1" style="background: red;height:700px;position: relative;">
          <p style="width: 20px;height: 100px;position:absolute;top:140px;line-height: 30px;">选课信息</p>
          <p style="width: 20px;height: 100px;position: absolute;top:350px;line-height: 30px">已选</p>
        </div>
        <div class="col-lg-11">
          <table class="table table-bordered text-center">
            <thead>
            <tr>
              <td>节次</td>
              <td>星期一</td>
              <td>星期二</td>
              <td>星期三</td>
              <td>星期四</td>
              <td>星期五</td>
              <td>星期六</td>
              <td>星期日</td>
            </tr>
            </thead>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>2</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>3</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>4</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>5</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>6</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>7</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>8</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>9</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>10</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>11</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>12</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>13</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
  window.onload=function ()
  {
    var oDiv1=document.getElementById('aside');
    alert(oDiv1);
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
        oDiv1: document.getElementById('aside'),
        username: this.$cookie.get('username'),
        realname: this.$cookie.get('realname'),
      }
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
      stu_sel_course: function () {
        this.$router.push('/stu_sel_course')
        location.reload()
      }
    },
  }
</script>

<style scoped>

</style>
