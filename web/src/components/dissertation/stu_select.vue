<template>
  <div>
    <PC_bar></PC_bar>
<!--    <div>-->
<!--      {{user_token}}\\\{{user_name}}\\\{{dissertation_id}}-->
        <table class="table table-bordered">
                  <tbody v-for="stu_dst_list in list">
          <tr>
            <th>课题号</th>
            <td>{{stu_dst_list.dissertation_id}}</td>
          </tr>
          <tr>
            <th>课题名称</th>
            <td>{{stu_dst_list.dissertation_title}}</td>
          </tr>
          <tr>
            <th>指导教师</th>
            <td>{{stu_dst_list.dissertation_teacher}}</td>
          </tr>
          <tr>
            <th>课题内容</th>
            <td>{{stu_dst_list.dissertation_content}}</td>
          </tr>
          <tr>
            <th>备注</th>
            <td>{{stu_dst_list.dissertation_requirement}}</td>
          </tr>
          <tr>
            <th>容量</th>
            <td>{{stu_dst_list.dissertation_capacity}}</td>
          </tr>
          <tr>
            <th>操作</th>
            <td><button type="submit" @click="choose(stu_dst_list.dissertation_id)">选择课题</button></td>
          </tr>
          <tr>
            <th>返回上一页</th>
            <td><button type="submit" @click="returnit">返回</button></td>
          </tr>
          </tbody>
        </table>
<!--    </div>-->
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
    export default {
      name: "stu_select",
      components: {PC_bar},
      data() {
        return {
          list: null,
          user_name: this.$cookie.get('username'),
          user_token: this.$cookie.get('user_token'),
          dissertation_id:this.$route.query.dissertation_id,
          // dissertation_id: '',
          dissertation: '',
        }
      },
      methods: {
        choose: function () {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
            "dissertation_id": this.dissertation_id,
          }
          this.$http.post(this.Global_Api + '/dst/stu_select', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              alert("选择成功")
              // location.reload()
            }
          })
        },
        returnit: function () {
          this.$router.push('/main/topic_select')
        }
      },
      mounted(){
        // console.log(res.data.data.dissertation_id);
        let data = {
          "user_name": this.user_name,
          "user_token": this.user_token,
          "dissertation_id": this.dissertation_id,
        }
        this.$http.post(this.Global_Api + '/dst/stu_view_dst', data).then((res) => {
          if (res.body.error_code !== 0) {
            alert(res.body.error_message)
          } else {
            this.list = res.body.stu_dst_list;
            // alert("已显示课题");
            if(this.list.length===0)
            {  alert("为空")}
          }
        })
      },
    }
</script>

<style scoped>

</style>
