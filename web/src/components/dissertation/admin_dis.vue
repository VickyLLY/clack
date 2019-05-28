<template>
  <div>
    <PC_bar></PC_bar>
    <div>
      <table class="table table-bordered">
        <caption class="table-bar" style="font-size: larger; font-weight: bolder">权限开放</caption>
        <tbody class="table-bar">
        <tr>
          <th class="table-bar">0-教师发布课题 1-审核时间 2-学生选题 3-教师选成员 4-学生上传 5-答辩时间 6-学生成绩确认 9-系统关闭阶段</th>
          <td><input type="text" placeholder="请输入权限对应数字" v-model="flag"><button type="submit" @click="submit(flag)">确定</button></td>
        </tr>
        </tbody>
      </table>
    </div>
    <br>
    <div><button class="btn btn-default" type="submit" @click="t_group" >教师分组</button></div>
    <td><input type="text" placeholder="请输入年份" v-model="year"><button type="submit" @click="submit_y(year)">确定</button></td>
    <br>
    <br>
    <div><button class="btn btn-default" type="submit" @click="distribute" >一键调剂</button></div>
    <br>
    <div>
      <br><br><br>
      <div>
        <button class="btn btn-default" type="submit" @click="un_approval" >显示未审核课题</button>
        <table class="table table-bordered">
          <caption class="table-bar" style="font-size: larger; font-weight: bolder">课题信息</caption>
          <thead>
          <tr>
            <th class="table-bar">课题号</th>
            <th class="table-bar">课题名称</th>
            <th class="table-bar">课题内容</th>
            <th class="table-bar">课题要求</th>
            <th class="table-bar">容量</th>
            <th class="table-bar">发布时间</th>
            <th class="table-bar">指导教师</th>
            <th class="table-bar">审核状态</th>
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
            <td>{{dissertation.dissertation_pub_time}}</td>
            <td>{{dissertation.dissertation_teacher}}</td>
            <td>{{dissertation.dissertation_approval}}</td>
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
  export default {
        name: "admin_dis",
    components: {
      PC_bar
    },
    data(){
          return {
            dissertation_id:'',
            user_name:this.$cookie.get('username'),
            user_token:this.$cookie.get('user_token'),
            list:null,
            flag:'',
            year:''
          }
    },
    methods:{
          choose:function (dissertation_id) {
            this.$router.push({
              path: '/main/admin_approval',
              query:{
                'dissertation_id':dissertation_id,
              }
            })
          },
      un_approval:function () {
        if(parseInt(this.flag) !== 1){
          alert("未到审核时间！")
        }else {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
            "dissertation_id": this.dissertation_id,
          }
          this.$http.post(this.Global_Api + '/dst/dst_list_need_approval', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              this.list = res.body.dst_list;
              if (this.list.length === 0) {
                alert("为空")
              }
            }
          })
        }
      },
      submit:function (flag) {
        if(flag !== ''){
          let data = {
            "user_name":this.user_name,
            "user_token":this.user_token,
            "flag":parseInt(flag)
          }
          this.$http.post(this.Global_Api + '/dst/get_flag', data).then((res) => {
            // if (res.body.error_code !== 0) {
            //   alert(res.body.error_message)
            // } else {
              alert("更改成功")
            // }
          })
        }
      },
      distribute:function () {
        if(parseInt(this.flag) !== 3){
          alert("未到调剂时间！")
        }else {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
          }
          this.$http.post(this.Global_Api + '/dst/dst_adjust', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              alert("调剂成功！")
            }
          })
        }
      },
      t_group:function () {
        let data = {
        }
        this.$http.post(this.Global_Api + '/background/group_teacher', data).then((res) => {
          if (res.body.error_code !== 0) {
            alert(res.body.error_message)
          } else {
            alert("分组成功！")
          }
        })
      },
      submit_y:function (year) {
        let data = {
          "year": year,
        }
        this.$http.post(this.Global_Api + '/background/time_place', data).then((res) => {
          if (res.body.error_code !== 0) {
            alert(res.body.error_message)
          } else {
            alert("安排成功！")
          }
        })
      }
    }
    }
</script>

<style scoped>
  button.btn {
    margin-right: 60px;
    width: 125px;
  }
</style>
