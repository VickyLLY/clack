<template>
  <div>
    <PC_bar></PC_bar>
    <div>
      <div>
        <input class="search " type="text" placeholder="按教师姓名查询" v-model="dissertation_tea">
        <button  class="btn btn-default" type="submit" @click="search_tea(dissertation_tea)">查询</button>
        <input class="search" type="text" placeholder="按课题题目关键字查询" v-model="dissertation_tit">
        <button  class="btn btn-default" type="submit" @click="search_key(dissertation_tit)">查询</button>
      </div>

      <br><br><br>

      <div>

        <table class="table table-bordered">
          <caption class="table-bar" style="font-size: larger; font-weight: bolder">课题信息</caption>

          <thead>
          <tr>
            <th class="table-bar">课题号</th>
            <th class="table-bar">课题名称</th>
            <th class="table-bar">课题内容</th>
            <th class="table-bar">课题要求</th>
            <th class="table-bar">容量</th>
            <!--            <th class="table-bar">审核状态</th>-->
            <!--            <th class="table-bar">发布时间</th>-->
            <th class="table-bar">指导教师</th>
            <th class="table-bar">操作</th>
          </tr>
          </thead>
          <tbody class="table-bar">
          <tr v-for="dissertation in list">
            <td>{{dissertation.dissertation_id}}</td>
            <td>{{dissertation.dissertation_title}}</td>
            <td>{{dissertation.dissertation_content}}</td>
            <td>{{dissertation.dissertation_requirement}}</td>
            <td>{{dissertation.dissertation_capacity}}</td>
            <!--            <td>{{dissertation.dissertation_approval}}</td>-->
            <!--            <td>{{dissertation.dissertation_pub_time}}</td>-->
            <td>{{dissertation.dissertation_teacher}}</td>
            <td><button type="submit" @click="choose(dissertation.dissertation_id)" >查看详情</button></td>
          </tr>
          </tbody>
        </table>

      </div>
    </div>
  </div>
</template>

<script>
  import PC_bar from '../public/PC_bar'
  let i = 0;
  let flag = 0;
  export default {
    name: "topic_sel_view",
    components: {
      PC_bar
    },
    data(){
      return{
        // flag:'',
        dissertation_tit: '',
        dissertation_tea:'',
        list:null,
        title_key:'',
        dissertation_id: '',
        dissertation:'',
      }
    },
    methods: {
      search_tea: function (dissertation_tea) {
        if (this.dissertation_tea !== "") {
          let data = {
            "teacher_name":this.dissertation_tea,
            "user_name": this.$cookie.get('username'),
            "user_token": this.$cookie.get('user_token'),
          }
          this.$http.post(this.Global_Api + '/dst/select_dst_teacher_name', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            } else {
              this.list = res.body.select_dst_teacher_name_list;
              if (this.list.length === 0) {
                alert("没有这个教师！");
              }
            }
          })
        } else {
          let data = {
            "user_name": this.$cookie.get('username'),
            "user_token": this.$cookie.get('user_token'),
          }

          this.$http.post(this.Global_Api + '/dst/dst_list', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            } else {
              this.list = res.body.dst_list;
              // alert("已显示全部可选课题。");
              if(this.list.length===0)
              {  alert("为空")}
            }
          })
        }
      },
      search_key: function (dissertation_tit) {
        if (this.dissertation_tit !== "") {
          let data = {
            "user_name": this.$cookie.get('username'),
            "user_token": this.$cookie.get('user_token'),
            "dissertation_title":this.dissertation_tit,
          }
          this.$http.post(this.Global_Api + '/dst/select_dst_dst_title', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            } else {
              this.list = res.body.select_dst_dst_title;
              // alert("已显示！")
              if (this.list.length === 0) {
                alert("没有相关关键字！")
              }
            }
          })
        } else {
          let data = {
            "user_name": this.$cookie.get('username'),
            "user_token": this.$cookie.get('user_token'),
          }
          this.$http.post(this.Global_Api + '/dst/dst_list', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            } else {
              this.list = res.body.dst_list;
              // alert("已显示全部可选课题。");
              if(this.list.length===0)
              {  alert("为空")}
            }
          })
        }
      },
      choose:function (dissertation_id) {
        // this.$cookie.set('dissertation_id', this.dissertation_id, 600);
        // this.$router.push('/stu_select')
        flag = 1;
        this.$router.push({
          path: '/stu_select',
          query:{
            'dissertation_id':dissertation_id,
          }
        })
      }
    },
    mounted: function(){
        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
        }
        this.$http.post(this.Global_Api + '/dst/dst_list', data).then((res) => {
          if (res.body.error_code !== 0) {
            alert("error!  " + res.body.error_message)
          } else {
            this.list = res.body.dst_list;
            // alert("已显示全部可选课题。");
            if(this.list.length===0)
            {  alert("为空")}
          }
        })
    }
  }
</script>

<style scoped>
  input {
    /*display: block;*/
    width: 200px;
    height: 40px;
    line-height: 40px;
    margin-left: 100px;
    margin-bottom: 10px;
    margin-top: 10px;
    border: 1px solid #888;
    padding: 10px;
    box-sizing: border-box;
  }
  button.btn {
    margin-right: 60px;
    width: 80px;
  }
</style>
