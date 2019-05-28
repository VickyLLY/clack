<template>
  <div>
    <PC_bar></PC_bar>
      <h3>发布公告</h3>
      <div class="v_select">
        <v-select max-height="80px" placeholder="请选择通知接收者(0: 管理员，1：教师，2：学生，3：全体成员)" :options="receiver" v-model="notice_receiver"></v-select>
        <v-select max-height="80px" placeholder="请选择系统(0：后台管理系统 1：毕设管理系统)" :options="author" v-model="notice_author"></v-select>
      </div>
      <p>公告标题：</p>

      <textarea class="form-control title" style="height: 35px;" placeholder="请输入公告标题..." v-model="notice_title" required="required"></textarea>

      <p>公告内容：</p>
      <div class = "text-area">

        <textarea class="form-control text" style="height: 600px;" contenteditable="true" placeholder="请输入公告内容..." v-model="notice_content" required="required"></textarea>
      </div>
      <button  class="btn" @click="confirm">确认发布</button>
    </form>

  </div>
</template>

<script>
  let receiver = ['0', '1', '2', '3'];
  let author = ['0', '1'];


  import PC_bar from "../public/PC_bar";
  Date.prototype.Format = function (fmt) {
    var o = {
      "M+": this.getMonth() + 1, //月份
      "d+": this.getDate(), //日
      "H+": this.getHours(), //小时
      "m+": this.getMinutes(), //分
      "s+": this.getSeconds(), //秒
      "q+": Math.floor((this.getMonth() + 3) / 3), //季度
      "S": this.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
      if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
  }




  export default {
    name: "add_notice",
    components: {PC_bar},
    data() {
      return {
        receiver: receiver,
        author: author,
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        notice_date: '',
        notice_title: '',
        notice_content: '',
        notice_receiver:'',
        notice_author:'',
      }
    },



    "methods": {

      confirm: function () {
        // alert(111)
        // console.log(this.user_name)
        if (this.notice_receiver === "" || this.notice_author === "" ||this.notice_title === "" || this.notice_content === "")
          alert("信息未填写完全")

        else {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
            "notice":{
              "notice_receiver": parseInt(this.notice_receiver),
              "notice_author": parseInt(this.notice_author),
              "notice_title": this.notice_title,
              "notice_content": this.notice_content,
              "notice_date" : new Date().Format("yyyy-MM-dd HH:mm:ss"),
            },
          }
          console.log(data)
          this.$http.post(this.Global_Api + '/background/add_notice',data).then((res) => {
            console.log(res.body)
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              alert("添加成功")
            }
          })
        }
      }
    }
  }

</script>

<style scoped>
  .title{
    width: 90%;
    margin: 0 auto;
    border-top:1px solid gainsboro;
    border-bottom:1px solid gainsboro;

  }
  .title textarea {
    width: 100%;
    margin: 5px  5px;
    border: 20px;
    outline: none;
    padding-left: 5px;
    height:  30px;
  }

  .title textarea::-webkit-input-placeholder {
    color: #9E9E9E;

  }

  .text{
    width: 90%;
    margin: 0 auto;
    border-top:1px solid gainsboro;
    border-bottom:1px solid gainsboro;

  }
  .text textarea {
    width: 100%;
    margin: 5px  0;
    border: 20px;
    outline: none;
    padding-left: 5px;
    height:  600px;
  }

  .text textarea::-webkit-input-placeholder {
    color: #9E9E9E;

  }

  h3 {
    text-align: center;
  }
  p {
    text-align: center;
    float-displace: 600px;
  }

  div.v_select {
    display: block;
    margin: 5px auto;
    width: 450px;
  }

  button.btn {
    display: block;
    text-align: center;
    margin: 20px auto;
    width: 300px;
  }

</style>


