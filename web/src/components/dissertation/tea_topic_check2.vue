<template>
  <div>
    <PC_bar></PC_bar>
 <div>
   {{teacher_number}}
    <table class="table table-bordered">
      <thead>
      <tr>
        <th>编号</th>
        <th>题目</th>
        <th>容量</th>
        <th>操作</th>
      </tr>
      </thead>
      <tbody v-for="d_a in list">
      <tr>
        <th>{{d_a.id}}</th>
        <td>{{d_a.title}}</td>
        <td>{{d_a.now_capacity}}/{{d_a.fixed_capacity}}</td>
        <td><button @click="select_stu(d_a.id)" type="button">查看学生</button></td>
      </tr>
      </tbody>
    </table>
 </div>
  </div>
</template>

<script>
    import PC_bar from "../public/PC_bar";
    export default {
        name: "tea_topic_check2",
      components: {PC_bar},
      data()
      {
        return {
         list:[],
          // teacher_number:'',
          user_name:this.$cookie.get('username'),
          user_token:this.$cookie.get('user_token'),
          dissertation_id: this.$route.query.dissertation_id,
          teacher_number:parseInt(this.$cookie.get('user_teacher_number')),
          flag:this.$route.query.flag
        }
      },
      mounted(){
          if(parseInt(this.flag)===3||parseInt(this.flag)===2){
            let data={
              'teacher_number':parseInt(this.teacher_number),
              'user_name':this.user_name,
              'user_token':this.user_token,
            }
            this.$http.post(this.Global_Api + '/dst/view_selected', data).then((res) =>{
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              }else{
                this.list = res.body.view_list
                if(this.list.length ===0)
                  alert("为空")
              }
            })
          }else {
            let data = {
              'teacher_number': parseInt(this.teacher_number),
              'user_name': this.user_name,
              'user_token': this.user_token,
            }
            this.$http.post(this.Global_Api + '/dst/view_selected_d', data).then((res) => {
              if (res.body.error_code !== 0) {
                alert("error!  " + res.body.error_message)
              } else {
                this.list = res.body.view_list
                if (this.list.length === 0)
                  alert("为空")
              }
            })
          }
    },
    methods:
    {
      select_stu:function (id) {
        if (parseInt(this.flag) === 3||parseInt(this.flag) === 2) {
          this.$router.push({
            path: '/main/tea_stu_select',
            query: {
              'flag':this.flag,
              'dissertation_id': id,
            }
          })
        } else if (parseInt(this.flag) === 4 || parseInt(this.flag) === 5 || parseInt(this.flag) === 6) {
          this.$router.push({
            path: '/main/tea_stu_comment',
            query: {
              'dissertation_id': id,
            }
          })
        }
      }
    }
  }
</script>

<style scoped>

</style>
