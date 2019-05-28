<template>
  <div>
    <PC_bar></PC_bar>
    <div>
      <h3>{{dissertation_id}}详细信息</h3>

      <table class="table table-bordered">
        <tbody v-for="old in list">
        <tr>
          <th>课题名称</th>
          <td>{{old.dissertation_title}}</td>
          <td><input type="text" placeholder="课题题目" v-model="dissertation_title"></td>
          <td><button type="submit" @click="change(old.dissertation_title,
        old.dissertation_content,old.dissertation_requirement,old.dissertation_capacity)">修改</button></td>
        </tr>
        <tr>
          <th>课题内容</th>
          <td>{{old.dissertation_content}}</td>
          <td><textarea class="text_" rows="10" cols="30" placeholder="课题内容" v-model="dissertation_content"></textarea></td>
          <td><button type="submit" @click="change(old.dissertation_title,
        old.dissertation_content,old.dissertation_requirement,old.dissertation_capacity)">修改</button></td>
        </tr>
        <tr>
          <th>备注</th>
          <td>{{old.dissertation_requirement}}</td>
          <td><input type="text" placeholder="备注" v-model="dissertation_requirement"></td>
          <td><button type="submit" @click="change(old.dissertation_title,
        old.dissertation_content,old.dissertation_requirement,old.dissertation_capacity)">修改</button></td>
        </tr>
        <tr>
          <th>容量</th>
          <td>{{old.dissertation_capacity}}</td>
          <td><input type="text" placeholder="课题容量（1-5）" v-model="dissertation_capacity"></td>
          <td><button type="submit" @click="change(old.dissertation_title,
        old.dissertation_content,old.dissertation_requirement,old.dissertation_capacity)">修改</button></td>

        </tr>
<!--        <tr>-->
<!--          <td>操作</td>-->
<!--          <td><button type="submit" @click="change(old.dissertation_title,-->
<!--        old.dissertation_content,old.dissertation_requirement,old.dissertation_capacity)">修改</button></td></tr>-->
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  // let dst = [];
  //document.getElementById("con").value="oldcontent";
  export default {
    name: "tea_topic_change",
    components: {PC_bar},
    data()
    {
      return{
        time:'',
        dissertation_id: this.$route.query.dissertation_id,
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        dissertation_title:'',
        dissertation_content: '',
        dissertation_requirement:'',
        dissertation_capacity:'',
        title:'',
        content: '',
        requirement:'',
        capacity:'',
        list:[],
      }
    },
    mounted(){
      // let data={
      //   'dissertation_id':this.dissertation_id,
      //   'user_name':this.user_name,
      //   'user_token':this.user_token
      // }
      // this.$http.post(this.Global_Api + '/dst/view_detail', data).then((res) =>{
      //   if (res.body.error_code !== 0) {
      //     alert("error!  " + res.body.error_message)
      //   }else
      //   {
      //     this.list = res.body.dlist
      //     this.new_list=res.body.dlist
      //     if(list.length===0)
      //     {
      //       alert("无")
      //     }
      //   }
      // })
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
          alert("已显示课题");
          if(this.list.length===0)
          {  alert("为空")}
        }
      })
    },
    methods:{
      change:function(dissertation_title,dissertation_content,dissertation_requirement,dissertation_capacity) {
          if (parseInt(this.dissertation_capacity) <= 0 || parseInt(this.dissertation_capacity) > 5) {
            alert("输入容量非法")
          } else{
            if(this.dissertation_title ==='')
              this.dissertation_title=dissertation_title
            if(this.dissertation_content ==='')
              this.dissertation_content=dissertation_content
            if(this.dissertation_requirement ==='')
              this.dissertation_requirement=dissertation_requirement
            if(this.dissertation_capacity ==='')
              this.dissertation_capacity = dissertation_capacity;
          }
        let data={
          "user_name": this.user_name,
          "user_token": this.user_token,
          "dissertation_id":parseInt(this.dissertation_id),
          "dissertation_title": this.dissertation_title,
          'dissertation_content': this.dissertation_content,
          'dissertation_requirement': this.dissertation_requirement,
          'dissertation_capacity': parseInt(this.dissertation_capacity),
        }
        this.$http.post(this.Global_Api + '/dst/change_dst', data).then((res)=>{
          if (res.body.error_code !== 0) {
            alert("提交失败" + res.body.error_message)
          } else {
            alert("提交成功")
            location.reload()
          }
        })
      },
    }
  }
</script>

<style scoped>
  input {
    display: block;
    width: 400px;
    height: 40px;
    line-height: 40px;
    margin: 0 auto;
    margin-bottom: 10px;
    outline: none;
    border: 1px solid #888;
    padding: 10px;
    box-sizing: border-box;
  }
  button.btn {
    display: block;
    margin: 0 auto;
    width: 300px;
  }
  textarea.text_{
    display: block;
    margin: 0 auto;
    width: 400px;
  }
</style>
