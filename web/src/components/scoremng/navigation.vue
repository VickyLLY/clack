<template>
  <div>

    <PC_bar></PC_bar>

    <div class="panel panel-default" style="width: 80%;margin: 0 auto"><!--首页新闻部分-->
      <div class="panel-body" style="height: 500px">

        <div style="margin: 0 auto;width:20%;height: 100%;float:left;">
          <!--    管理员导航栏-->
          <div v-if="user_type==='0'">
            <ul class="nav nav-pills nav-stacked">
              <li class="active"><a href="#">学生成绩管理</a></li>
              <li><a ><router-link :to="{name:'admin_score'}">查看学生成绩</router-link></a></li>
            </ul>
          </div>
          <!--    教师导航栏-->
          <div v-else-if="user_type==='1'">
            <ul class="nav nav-pills nav-stacked">
              <li class="active"><a href="#">学生成绩管理</a></li>
              <li><a ><router-link :to="{name:'Tea_upload'}">提交学生成绩</router-link></a></li>
              <li><a ><router-link :to="{name:'Tea_query'}">查询学生成绩</router-link></a></li>
            </ul>
          </div>
          <!--    学生导航栏-->
          <div v-else="user_type==='2'">
            <ul class="nav nav-pills nav-stacked">
              <li class="active"><a href="#">学生成绩管理</a></li>
              <li><a ><router-link :to="{name:'stu_score'}">学生查询成绩</router-link></a></li>
              <li><a ><router-link :to="{name:'stu_evaluation'}">学生课程评价</router-link></a></li>
            </ul>
          </div>

        </div>

        <div class="content">
          <router-view></router-view>
        </div>

      </div>
    </div>

  </div>


</template>

<script>
  import PC_bar from '../public/PC_bar'
  export default {
    name: "navigation",
    components:{
      PC_bar,
    },
    data(){
      return{
        user_type:this.$cookie.get('user_type')
      }
    },
  }
</script>

<style scoped>

  .content{
    margin: 0 auto;
    width:70%;
    height: 100%;
    float:right;
  }
</style>
