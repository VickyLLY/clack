<template>
    <div>
      <PC_bar></PC_bar>
      <div>
        <div>
          <table class="table table-bordered">
                    <tbody v-for="value in list">
            <tr>
              <th>课题号</th>
                                  <td>{{value.dissertation_id}}</td>
            </tr>
            <tr>
              <th>课题名称</th>
                        <td>{{value.dissertation_title}}</td>
            </tr>
            <tr>
              <th>指导教师</th>
                        <td>{{value.dissertation_teacher}}</td>
            </tr>
            <tr>
              <th>课题内容</th>
                        <td>{{value.dissertation_content}}</td>
            </tr>
            <tr>
              <th>备注</th>
                        <td>{{value.dissertation_requirement}}</td>
            </tr>
            <tr>
              <th >容量</th>
                        <td>{{value.dissertation_capacity}}</td>
            </tr>
            <tr>
              <th v-if="parseInt(flag)===2">操作</th>
              <td v-if="parseInt(flag)===4">
                <input type="file" class="file" @change="getFile" placeholder="上传文件"><button type="submit" @click="stu_up">上传</button>
              </td>
              <td v-if="parseInt(flag)===2"><button type="submit" @click="choose">退选</button></td>
            </tr>
                    </tbody>
          </table>
        </div>

      </div>
    </div>
</template>

<script>
    import PC_bar from "../public/PC_bar";
    export default {
        name: "stu_check_dis",
      components: {
          PC_bar
      },
      data(){
        return{
          list:null,
          user_name: this.$cookie.get('username'),
          user_token: this.$cookie.get('user_token'),
          student_number: this.$cookie.get('student_number'),
          dissertation_file:'',
          flag:this.$route.query.flag
        }
      },
      methods:{
        getFile: function() {
          this.dfile = event.target.files[0];
          console.log(this.dfile);
        },
        stu_up: function () {
          event.preventDefault();//取消默认行为
          //创建 formData 对象
          let dissertation_file = new FormData(); // 向 formData 对象中添加文件
          dissertation_file.append('dissertation_file',this.dfile);
          // let data = {
          //   "user_name": this.user_name,
          //   "user_token": this.user_token,
          //   "myfile": this.dissertation_file
          // }
          // this.$http.post("/dst/upload_file",dissertation_file).then(function (response) {
          //   // console.log("res: ",response);
          //   if (res.body.error_code !== 0) {
          //     alert(res.body.error_message)
          //   } else {
          //     alert("提交成功")
          //   }
          // })
          alert("上传成功")
          location.reload()
        },
        choose:function () {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
          }
          this.$http.post(this.Global_Api + '/dst/del_select', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              alert("已退选");
              location.reload()
            }
          })

        }
      },
      mounted(){
        if(parseInt(this.flag)!==2){
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
          }
          this.$http.post(this.Global_Api + '/dst/stu_dst_list', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              this.list = res.body.stu_dst_list
            }
          })
        }else{
          let data = {
            "user_name": this.$cookie.get('username'),
            "user_token": this.$cookie.get('user_token'),
          }
          this.$http.post(this.Global_Api + '/dst/stu_dst_list_temp', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert("error!  " + res.body.error_message)
            } else {
              this.list = res.body.stu_dst_list;
            }
          })
        }
      }
    }
</script>

<style scoped>
  h3 {
    text-align: center;
  }
  .table{
    margin-left: 200px;
    width: 800px;
  }
</style>
