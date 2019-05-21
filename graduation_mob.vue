<template>
  <bar_mob>
  <div class="panel" style="height: 100%;width:100%;background-color: powderblue">
    <div class="panel-heading" style="background-color: powderblue">
      <legend>我的课题</legend>
    </div>
    <div class="panel-default"  style="background-color: #f7ecb5">
      <h4>课题编号：{{ktid}}{{nowtime}}</h4>
      <h4>课题标题：{{ktm}}</h4>
      <h4>课题内容：{{ktnr}}</h4>
      <h4>开题教师：{{ktjs}}</h4>
      <div align="center">
        <button @click="tuixuan" v-if="flag==2" class="btn-info">退选</button>
      </div>
    </div>
    <div class="panel-heading" style="background-color: powderblue">
      <legend>答辩信息</legend>
    </div>
    <div class="panel-default" style="background-color: #f7ecb5">
      <h4>答辩时间：{{time}}</h4>
      <h4>答辩地点：{{loc}}</h4>
      <h4 v-if="tea_name1==null">考察导师:暂未确认</h4>
      <h4 v-for="v in tea_name1">考察导师工号：{{v.teacher_number}}</h4>
    </div>
    <div class="panel-heading" style="background-color: powderblue">
      <legend>毕业设计最终评分</legend>
    </div>
    <div class="panel-default" style="background-color: #f7ecb5">
      <h4>成绩：{{score}}</h4>
      <h4>评语：{{comment}}</h4>
      <h4>评审教师：{{tea_name2}}</h4>
      <h6>如有异议，请联系教务处(电话：{{tet}},地址：{{adress}})</h6>
    </div>
  </div>
  </bar_mob>
</template>

<script>
  import bar_mob from './bar_mob'
  export default {
    name: "news",
    components: {
      bar_mob
    },
    data() {
      return{
        kt_list:null,
        ktid:"暂未选题",
        ktm:"暂未选题",
        ktnr:"暂未选题",
        ktjs:"暂未选题",
        flag:"0",
        time:"暂未确认",
        loc:"暂未确认",
        schedule:null,
        tea_name1:null,
        flag1:"0",
        grade_list:null,
        score:"暂未评出，请等待",
        comment:"暂未评出，请等待",
        tea_name2:"暂未评出，请等待",
        tet:"13579246800",
        adress:"图书馆某地",
        nowtime:""
      }
    },
    created(){
      this.getTime();
      this.getproject();
      this.getanpai();
      this.getscore();

    },
    methods:{
      tuixuan(){
        let data = {'user_name':this.$cookie.get('username'), 'user_token':this.$cookie.get('user_token')}
        this.$http.post(this.Global_Api+'/dst/del_select',data)
          .then(res=>{if(res.body.error_code==0)
          {alert("退选成功");
            this.ktid='暂未选题';
            this.ktm='暂未选题';
            this.ktnr='暂未选题';
            this.ktjs='暂未选题';}
          else alert("退选失败" + res.body.error_message);
          })
      },
      getTime(){
        //setInterval(()=>{
          //new Date() new一个data对象，当前日期和时间
          //toLocaleString() 方法可根据本地时间把 Date 对象转换为字符串，并返回结果。
        //  this.nowtime = new Date().getMonth();
       // },1000)
        let data = {'user_name':this.$cookie.get('username'), 'user_token':this.$cookie.get('user_token')}
        this.$http.post(this.Global_Api+'/dst/return_flag',data)
          .then((res)=>{
            this.flag=res.body.flag;
          })
      },
      getanpai(){
        let data = {'student_number':this.$cookie.get('user_student_number'),'user_name':this.$cookie.get('username'), 'user_token':this.$cookie.get('user_token')}
        this.$http.post(this.Global_Api+'/background/design',data)
          .then((res)=>{
            if (res.body.error_code == 0)
            {this.schedule=res.body.result_list;
            this.time=res.body.result_list[0].assign_date;
            this.loc=res.body.result_list[0].assign_classroom_id;}
          }),
          this.$http.post(this.Global_Api + '/background/design_tea', data).then((res) => {
            if (res.body.error_code == 0)
            {
              this.tea_name1=res.body.result_list2;
              // alert("查询结果")
            }
          })
      },
      getproject()
      {
        let data = {'user_name':this.$cookie.get('username'), 'user_token':this.$cookie.get('user_token')}
        this.$http.post(this.Global_Api+'/dst/stu_dst_list',data)
          .then((res)=>{
            if(res.body.error_code==0)
            {this.kt_list=res.body.stu_dst_list;
            this.ktid=this.kt_list[0].dissertation_id;
            this.ktm=this.kt_list[0].dissertation_title;
            this.ktnr=this.kt_list[0].dissertation_content;
            this.ktjs=this.kt_list[0].dissertation_teacher;}
          })
      },
      getscore(){
        let data = {'user_name':this.$cookie.get('username'), 'user_token':this.$cookie.get('user_token')}
        this.$http.post(this.Global_Api+'/dst/stu_view_grade',data)
          .then((res)=>{
            if(res.body.error_code==0)
            { this.grade_list=res.body.stu_view_grade;
              this.score=this.grade_list[0].grade;
              this.comment=this.grade_list[0].comment;
              this.tea_name2=this.ktjs;}
          })
      },
    }
  }
</script>

<style>

</style>
