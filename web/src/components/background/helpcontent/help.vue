<template>
    
    <div>
       <PC_bar></PC_bar>
        <el-menu :default-active="activeIndex" class="el-menu-demo">
      <el-submenu index="1">
        <template slot="title">
          <router-link to="/main/help/part1">排课子系统</router-link>
        </template>

        <el-menu-item index="1-1">
          <router-link to="/main/help/part1_1">客户端子系统</router-link>
        </el-menu-item>
        <el-menu-item index="1-2">
          <router-link to="/main/help/part1_2">管理端子系统</router-link>
        </el-menu-item>
      </el-submenu>

      <el-submenu index="2">
        <template slot="title">
          <router-link to="/main/help/part2">选课子系统</router-link>
        </template>
        <el-menu-item index="2-1">
          <router-link to="/main/help/part2_1">客户端子系统（学生篇）</router-link>
        </el-menu-item>
        <el-menu-item index="2-2">
          <router-link to="/main/help/part2_2">客户端子系统（教师篇）</router-link>
        </el-menu-item>
        <el-menu-item index="2-3">
          <router-link to="/main/help/part2_3">管理端子系统</router-link>
        </el-menu-item>
      </el-submenu>
      <el-menu-item>
        <router-link to="/main/help/part3">后台管理子系统</router-link>
      </el-menu-item>
      <el-submenu index="4">
        <template slot="title">
          <router-link to="/main/help/part4">毕业设计子系统</router-link>
        </template>
        <el-menu-item index="4-1">
          <router-link to="/main/help/part4_1">客户端子系统（学生篇）</router-link>
        </el-menu-item>
        <el-menu-item index="4-2">
          <router-link to="/main/help/part4_2">客户端子系统（教师篇）</router-link>
        </el-menu-item>
        <el-menu-item index="4-3">
          <router-link to="/main/help/part4_3">管理端子系统</router-link>
        </el-menu-item>
      </el-submenu>
       <el-menu-item>
        <router-link to="/main/help/part5">成绩管理子系统</router-link>
      </el-menu-item>
    </el-menu>
    <div class="right">
    <router-view></router-view>
    </div>
    </div>
</template>


<script>
import PC_bar from '../public/PC_bar';
export default {
    name:'help',
    components:{
        PC_bar,
    }
}
</script>

<style scoped>
    .el-menu-demo{
        float: left;
    }
    .right{
        margin-left: 250px;
        line-height: 1.5em;
        font-size: 20px;
        text-indent: 2px;
    }
    .right h1{
        text-align: center;
    }
</style>


