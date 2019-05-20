<template>
  <div>
    <PC_bar></PC_bar>
    <h3>对课题编号为{{dissertation_id}}学号为{{student_number}}的学生评分</h3>
    <div>
      <input type="text" placeholder="课题评分(百分制)" v-model="score">
      <textarea class="text_" rows="10" cols="30" placeholder="指导评语" v-model="comment"></textarea>
      <button  type="submit" class="btn btn-default" @click="submit">确认提交</button>
  </div>
  </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  export default {
    name: "tea_comment",
    components: {PC_bar},
    data()
    {
      return{
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        dissertation_id:this.$route.query.dissertation_id,
        student_number:this.$route.query.student_number,
        score:'',
        comment:''
      }
    },
    methods:{
      submit:function(){
        if (this.score === "" || this.comment === "") {
          alert("请输入完整的信息")
        } else {
          let data = {
            "dissertation_id":parseInt(this.dissertation_id),
            "student_number":parseInt(this.student_number),
            "score":parseInt(this.score),
            "comment":this.comment,
            "user_name":this.user_name,
            "user_token":this.user_token,
          }
          this.$http.post(this.Global_Api + '/dst/upload_score', data).then((res) =>{
            if (res.body.error_code !== 0) {
              alert("评价失败" + res.body.error_message)
            } else {
              alert("评价成功")
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
