
<template>
  <div>
    <div class="wrapper">
      <!-- Sidebar  -->
      <nav id="sidebar">
        <div class="sidebar-header">
          <h3>Clack</h3>
        </div>

        <ul class="list-unstyled components">
          <h2 @click="main_mob">教务管理</h2><br>

          <!-- <li class="active">
             <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">排课子系统</a>
           </li>-->
          <li>
            <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle" @click="funfun">排课子系统</a>
            <ul class="collapse list-unstyled" id="pageSubmenu">
              <li v-if="user_type==1">
                <a @click="schedule_mob">查看课表</a>
              </li>
              <li v-if="user_type==2">
                <a @click="schedule_mob">查看课表</a>
              </li>
            </ul>
          </li>
          <li>
            <a href="#pageSubmenuxk" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">选课子系统</a>
            <ul class="collapse list-unstyled" id="pageSubmenuxk">
              <li>
                <a @click="sel_course_mob">查看课表及选课情况</a>
              </li>
            </ul>
          </li>
          <li>
            <a v-on:click="">后台管理子系统</a>
          </li>
          <li>
            <a v-on:click="graduation_mob">毕业设计子系统</a>
          </li>
          <li>
            <a v-on:click="">成绩管理系统</a>
          </li>

        </ul>
      </nav>

      <!-- Page Content  -->
      <div id="content">

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">

            <button type="button" id="sidebarCollapse" class="btn btn-info">
              <i class="fas fa-align-left"></i>
              ≡
            </button>
            <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <i class="fas fa-align-justify"></i>
              {{realname}}<!--用来修改用户姓名-->
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="nav navbar-nav ml-auto">
<!--                <li class="nav-item active">-->
<!--                  <a v-on:click="" class="nav-link" href="#">修改用户信息</a>-->
<!--                </li>-->
                <li class="nav-item">
                  <a  href="/" @click="quit" class="nav-link" >注销</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <!--用来填写正文信息-->
        <slot></slot><!--标记组件位置-->
        <router-view/>
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    name: "bar_mob",
    data(){
      return{
        username:this.$cookie.get('username'),
        realname:this.$cookie.get('realname'),
        user_type: this.$cookie.get('user_type'),
      }
    },
    created(){
      this.$nextTick(function () {
        $('#sidebarCollapse').on('click',
          function () {
            $('#sidebar').toggleClass('active');
          }
        )
      })
    },
    methods:{
      sel_course_mob:function(){
        if(this.user_type==2){
          this.$router.push({
            path: '/main_mob/stu_sel_course_mob',
          })
        }
        else if(this.user_type==1){
          this.$router.push({
            path: '/main_mob/tea_sel_course_mob',
          })
        }else if(this.user_type==0){
          alert("管理员请去PC端操作");
        }else{
          alert("系统未知错误，请联系相关人员");
        }
      },
      graduation_mob:function(){
        this.$router.push({
          path: '/graduation_mob',
        })
      },
      funfun:function(){
        if(this.user_type==0){
          alert("管理员在手机端无排课子系统功能");
        }
      },
      quit:function () {
        this.$cookie.delete('username');
      },
      schedule_mob:function () {
        if(this.user_type==2){
          this.$router.push({
            path: '/schedule_mob',
          })
        }
        else if(this.user_type==1){
          this.$router.push({
            path: '/schedule_mob_tea',
          })
        }
      },
      main_mob:function () {
        this.$router.push({
          path: '/main_mob',
        })
      }
    }
  }
</script>


<style>
  /*
    DEMO STYLE
*/

  @import "https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700";
  body {
    font-family: 'Poppins', sans-serif;
    background: #fafafa;
  }

  p {
    font-family: 'Poppins', sans-serif;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1.7em;
    color: #999;
  }

  a,
  a:hover,
  a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
  }

  .navbar {
    padding: 15px 10px;
    background: #fff;
    border: none;
    border-radius: 0;
    margin-bottom: 40px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
  }
  .wrapper {
    display: flex;
    width: 100%;
    align-items: stretch;
  }

  #sidebar {
    min-width: 240px;
    max-width: 225px;
    background: #7386D5;
    color: #fff;
    transition: all 0.3s;
  }

  #sidebar.active {
    margin-left: -250px;
  }

  #sidebar .sidebar-header {
    padding: 20px;
    background: #6d7fcc;
  }

  #sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid #47748b;
  }

  #sidebar ul p {
    color: #fff;
    padding: 10px;
  }

  #sidebar ul li a {
    padding: 10px;
    font-size: 1.1em;
    display: block;
  }

  #sidebar ul li a:hover {
    color: #7386D5;
    background: #fff;
  }

  #sidebar ul li.active>a,
  a[aria-expanded="true"] {
    color: #fff;
    background: #6d7fcc;
  }

  a[data-toggle="collapse"] {
    position: relative;
  }

  .dropdown-toggle::after {
    display: block;
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
  }

  ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #6d7fcc;
  }

  ul.CTAs a {
    text-align: center;
    font-size: 0.9em !important;
    display: block;
    border-radius: 5px;
    margin-bottom: 5px;
  }

  #content {
    width: 100%;
    padding: 20px;
    min-height: 100vh;
    transition: all 0.3s;
  }
  @media (max-width: 768px) {
    #sidebar {
      margin-left: -250px;
    }
    #sidebar.active {
      margin-left: 0;
    }
    #sidebarCollapse span {
      display: none;
    }
  }
</style>
