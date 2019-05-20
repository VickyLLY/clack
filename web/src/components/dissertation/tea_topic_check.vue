<template>
  <div>
    <PC_bar></PC_bar>
    <div> <h3>教师：{{user_name}}</h3>
      <table class="table table-bordered">
        <thead>
        <tr>
          <th>序号</th>
          <th>题目</th>
          <th>内容</th>
          <th>备注</th>
          <th>容量</th>
          <th>审核状态</th>
          <th>发布时间</th>
          <th>操作</th>
        </tr>
        </thead>
        <tbody v-for="d_a in list">
        <tr>
          <td>{{d_a.dissertation_id}}</td>
          <td>{{d_a.dissertation_title}}</td>
          <td>{{d_a.dissertation_content}}</td>
          <td>{{d_a.dissertation_requirement}}</td>
          <td>{{d_a.dissertation_capacity}}</td>
          <td>{{d_a.dissertation_approval}}</td>
          <td>{{d_a.dissertation_pub_time}}</td>
          <td><button @click="change(d_a.dissertation_id)" type = "submit">查看/修改</button></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  // import {Data} from "popper.js";
  //import {Data} from "popper.js";
  export default {
    name: "tea_topic_check",
    components: {PC_bar},
    data() {
      return {
        list:[],
        user_name :this.$cookie.get('username'),
        user_token:this.$cookie.get('user_token'),
        teacher_number: this.$cookie.get('user_teacher_number'),
        //d:'',
      }
    },
    methods:
      {
        change: function (dissertation_id) {
          // let d = new Data();d.getMonth() >= 3
          // if () {
          //   alert("超过限制的修改时间")
          // } else {
          this.$router.push({
              path:'/main/tea_topic_change',
              query:{
                'dissertation_id':dissertation_id,
              }
            })
          //   }
        }
      },
    mounted() {
          //this.fun();
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
          };
          this.$http.post(this.Global_Api + '/dst/teacher_dst_list', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.error_message)
            } else {
              this.list = res.body.teacher_dst_list;
              if (this.list.length === 0)
                alert('今年无发布课题记录！')
            }
          })
        }
      }
</script>

<style scoped>

</style>
