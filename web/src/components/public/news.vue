<template>

  

  <div class="panel panel-default" style="width: 80%;margin: 0 auto"><!--首页新闻部分-->
    <!-- 学位警告，使用v-if -->
    <div class="alert alert-danger" role="alert" v-if="warn">
      <h3>学分尚未达到要求，给予学位警告</h3>
      <ul >
        <li>必修毕业要求总学分:{{required_course_credit_aim}}</li>
        <li>必修所获总学分:{{required_course_credit_gained_sum}}</li>
        <li>选修毕业要求总学分:{{optional_course_credit_aim}}</li>
        <li>选修所获总学分:{{optional_course_credit_gained_sum}}</li>
        <li>辅修毕业要求总学分:{{minor_course_credit_aim}}</li>
        <li>辅修所获总学分:{{minor_course_credit_gained_sum}}</li>
      </ul>
    </div>

    <div class="panel-body">

      <div class="panel panel-default" style="width: 49%;margin: auto;float: left"  v-for="item in noticeList" :key='item.id' ><!--每一个块的新闻部分-->
        <div class="panel-heading">
          <router-link :to="'/main/news_detail/'+item.notice_id" tag="h3"  @click.native="flushCom"> {{item.notice_title}}</router-link>
        </div>
        <div class="panel-body" style="white-space: pre-wrap">{{item.notice_content}}</div>
      </div>
    </div>

  </div><!--首页新闻部分-->


</template>

<script>
  export default {
    name: "news",
    data(){
      return {
        user_type:this.$cookie.get('user_type'),
        user_id:this.$cookie.get('user_student_number'),
        news_url:'',
        noticeList:[],
        warning_list:[],
        stu:null,
        warn:false,
        required_course_credit_gained_sum:0,
        required_course_credit_aim:0,
        optional_course_credit_gained_sum:0,
        optional_course_credit_aim:0,
        optional_course_credit_gained_sum:0,
        optional_course_credit_aim:0,
        minor_course_credit_gained_sum:0,
        minor_course_credit_aim:0,
      }
    },

    activated(){
      this.judge(),
      this.getNotice()
      this.getWarning()
    },
    methods:{
      flushCom:function(){
        this.$router.go(0);
      },
      judge(){
        console.log(this.user_id)
        // 这里因为登录是root，所以先将uers_type==0，实际上应该写==1
        if(this.user_type==1){
          console.log("这是老师")
          this.news_url=this.Global_Api+'/background/notice_list_teacher'
        }
        else if(this.user_type==2){
          console.log("这是学生")
          this.news_url=this.Global_Api+'/background/notice_list_student'
        }
      },
      getNotice(){
        this.$http.get(this.news_url).then(res=>{
          if(res.body.error_code !== 0)
          {
            alert(res.body.error_message)
          }else{
            // console.log(res.body)
            this.noticeList=res.body.notice_list
          }
        })
      },
      getWarning(){
        if(this.user_type==2){
          this.$http.get(this.Global_Api+'/background/degree_warning').then(res=>{
          if(res.body.error_code !== 0)
          {
            alert(res.body.error_message)
          }else{
            this.warning_list=res.body.students_list
            // console.log(this.warning_list)
            for(let i=0;i<this.warning_list.length;i++){
              if(this.warning_list[i].student_number==this.user_id){
                    this.stu=this.warning_list[i]
                    this.warn=true
              }
            }
            this.required_course_credit_gained_sum=this.stu.required_course_credit_gained_sum
            this.required_course_credit_aim=this.stu.required_course_credit_aim
            this.optional_course_credit_gained_sum=this.stu.optional_course_credit_gained_sum
            this.optional_course_credit_aim=this.stu.optional_course_credit_aim
            this.minor_course_credit_gained_sum=this.stu.minor_course_credit_gained_sum
            this.minor_course_credit_aim=this.stu.minor_course_credit_aim
          }
        })
        }
      }
    }
  }
</script>

<style scoped>

</style>
