<template>
  <div>
    <PC_bar></PC_bar>
    <div class="v_select">
      <v-select max-height="80px" placeholder="请选择学年" :options="years" v-model="year"></v-select>
      <br>
      <v-select max-height="80px" placeholder="请选择学期" :options="semesters" v-model="semester"></v-select>
      <br>
    </div>
    <div class="container" style="position: relative">
          <span>添加新学期开始时间</span><date-pick v-model="new_semester" :config="config" ></date-pick>
    </div>
    <br>
    <button type="submit" class="btn btn-default" v-on:click="confirm">确认添加</button>
  </div>
</template>

<script>
  let years = [];
  let semesters = [1, 2, 3];
  for (let i = 2016; i <= 2030; i++)
    years.push(i);
  import PC_bar from '../public/PC_bar'
  export default {
        name: "add_semester",
        data(){
          return{
            new_semester:null,
            config: {
              format: 'YYYY-MM-DD',
              useCurrent: false,
            },
            semester_year:null,
            years:years,
            semesters:semesters,
            year:null,
            semester:null
          }
        },
        components:{
          PC_bar,
        },
        methods:{
          confirm:function () {
            if(this.new_semester==null){
              alert("请填写日期")
            }
            else {
              console.log(this.new_semester.split('-'));
              let start_date_year = parseInt(this.new_semester.split('-')[0]);
              let start_date_month = parseInt(this.new_semester.split('-')[1]);
              let start_date_day = parseInt(this.new_semester.split('-')[2]);

              let data = {
                "semester": {
                  "year": this.year,
                  "semester": this.semester,
                  "start_date_year": start_date_year,
                  "start_date_month": start_date_month,
                  "start_date_day": start_date_day
                },
                "user_name": this.$cookie.get('username'),
                "user_token": this.$cookie.get('user_token')
              }
              this.$http.post(this.Global_Api + '/entity/new_semester', data).then((res) => {
                alert(res.body.error_message)
                if(res.body.error_code===0){
                  // this.$router.push({name:"add_semester"})
                  location.reload()
                }
              })
            }
          }
        }
    }
</script>

<style scoped>
  div.v_select{
    display: block;
    margin: 0 auto;
    width: 300px;
  }
  div.container{
    margin: 0 auto;
    width: 330px;
  }
  button.btn {
    display: block;
    margin: 0 auto;
    width: 300px;
  }
</style>
