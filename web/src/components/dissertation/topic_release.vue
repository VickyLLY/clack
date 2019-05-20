<template>
  <div>
    <PC_bar></PC_bar>
    <div>
      <input type="text" placeholder="课题题目" v-model="dissertation_title">
      <textarea class="text_" rows="10" cols="30" placeholder="课题内容" v-model="dissertation_content"></textarea>
      <input type="text" placeholder="请对课题进行额外补充" v-model="dissertation_requirement">
      <input type="text" placeholder="课题容量（范围在1~5之间）" v-model="dissertation_capacity">
      <button type="submit"  class="btn btn-default" v-on:click="submit">确认提交</button>
    </div>
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  export default {
    name: "topic_release",
    components: {PC_bar},
    data(){
      return{
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        dissertation_title:'',
        dissertation_content: '',
        dissertation_requirement:'',
        dissertation_capacity:''
      }
    },
    methods:{
      submit:function(){
        if (this.dissertation_title === "" || this.dissertation_content === ""||this.dissertation_capacity ==="") {
          alert("请输入完整的课题信息")
        } else {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
            "dissertation":{
              'dissertation_title': this.dissertation_title,
              'dissertation_content': this.dissertation_content,
              'dissertation_requirement':this.dissertation_requirement,
              'dissertation_capacity':parseInt(this.dissertation_capacity),
            }
          }
          this.$http.post(this.Global_Api + '/dst/new_dst', data).then((res) =>{
            if (res.body.error_code !== 0) {
              alert("提交失败" + res.body.error_message)
            }
            else
            {  alert("提交成功")
              location.reload()
            }
          })
        }
      }
    },
    mounted() {
      if (this.$cookie.get('username') == null)
        this.$router.push('/')
    },
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
