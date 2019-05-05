<template>
  <div style="overflow: hidden" class="clearfix">
    <nav class="navbar navbar-default navbar-fixed-top">
      <a class="navbar-brand"><strong>教务管理系统</strong></a>
      <ul class="nav navbar-nav">
        <li><a href="">本科生选课</a></li>
        <li><a href="">研究生选课</a></li>
        <li><a href="">查看课表</a></li>
        <li><a href="">其他注意事项</a></li>
      </ul>
      <div id="clock">
        <p class="date">{{ date }}</p>
        <p class="time">{{ time }}</p>
      </div>
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


    <div id="aside" class="container pull-right"
         style="width:700px;height:700px;border:1px solid red;position:relative;top:100px;left:640px;">
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
            <tr v-for="n in 13">
              <td :class=td[n]>{{n}}</td>
              <td v-for="m in 7" class="init">
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
  import $ from 'jquery'
  export default {
    name: "stu_sel_course",
    data() {
      return {
        username: this.$cookie.get('username'),
        realname: this.$cookie.get('realname'),
        time: '',
        date: '',
        week: ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
        td:['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen'],
      }
    },
    methods: {
      quit: function () {
        this.$cookie.delete('username');
      },
      getStyle: function (obj, name) {
        if (obj.currentStyle) {
          return obj.currentStyle[name];
        } else {
          return getComputedStyle(obj, false)[name];
        }
      },
      startMove: function (obj, attr, iTarget, vueObject) {
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
          var cur = 0;

          if (attr === 'opacity') {
            cur = parseFloat(vueObject.getStyle(obj, attr)) * 100;
          } else {
            cur = parseInt(vueObject.getStyle(obj, attr));
          }

          var speed = (iTarget - cur) / 6;
          speed = speed > 0 ? Math.ceil(speed) : Math.floor(speed);
          console.log(speed);
          if (cur === iTarget) {
            clearInterval(obj.timer);
          } else {
            if (attr === 'opacity') {
              obj.style.filter = 'alpha(opcity:' + (cur + speed) + ')';
              obj.style.opacity = (cur + speed) / 100;
              document.getElementById('txt1').value = obj.style.opacity;
            } else {
              obj.style[attr] = cur + speed + 'px';
            }
          }
        }, 30);
      },
      updateTime: function (vueObject) {
        var cd = new Date();
        vueObject.time = vueObject.zeroPadding(cd.getHours(), 2) + ':' + vueObject.zeroPadding(cd.getMinutes(), 2) + ':' + vueObject.zeroPadding(cd.getSeconds(), 2);
        vueObject.date = vueObject.zeroPadding(cd.getFullYear(), 4) + '-' + vueObject.zeroPadding(cd.getMonth() + 1, 2) + '-' + vueObject.zeroPadding(cd.getDate(), 2) + ' ' + vueObject.week[cd.getDay()];
      },
      zeroPadding: function (num, digit) {
        var zero = '';
        for (let i = 0; i < digit; i++) {
          zero += '0';
        }
        return (zero + num).slice(-digit);
      },

    },
    mounted: function () {
      var that = this;
      var oDiv1 = document.getElementById('aside');
      this.$nextTick(() => {
        if(that.timer){
          clearInterval(that.timer);
        }
        that.timer=setInterval(()=>{
          that.updateTime(that);
        },1000);
        that.updateTime(that);
        oDiv1.onmouseover = function () {
          that.startMove(oDiv1, 'left', 10, that);
        };
        oDiv1.onmouseout = function () {
          that.startMove(oDiv1, 'left', 640, that);
        };

      })
    },
    computed:{
      reColor:function () {
        
      }
    },
  }
</script>

<style scoped>
  #clock {
    font-family: 'Microsoft YaHei','Lantinghei SC','Open Sans',Arial,'Hiragino Sans GB','STHeiti','WenQuanYi Micro Hei','SimSun',sans-serif;
    color: #2b669a;
    text-align: center;
    position: absolute;
    left: 60%;
    top:10px;
    text-shadow: 0 0 20px #2aabd2, 0 0 20px rgba(100, 100, 200, 0.5);
  }
  #clock .time {
    letter-spacing: 0.05em;
    font-size: 20px;
    padding: 5px;
    display: inline-block;
  }
  #clock .date {

    display: inline-block;
    letter-spacing: 0.1em;
    font-size: 20px;
  }
  .init{
    background: green;
  }
</style>
