<template>


  <div class="panel panel-default" style="width: 80%;margin: 0 auto"><!--首页新闻部分-->

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
        news_url:'',
        noticeList:[]
      }
    },

    activated(){
      this.judge(),
        this.getNotice()
    },
    methods:{
      flushCom:function(){
        this.$router.go(0);
      },
      judge(){
        // 这里因为登录是root，所以先将uers_type==0，实际上应该写==1
        if(this.user_type==1){
          console.log("这是老师")
          this.news_url=this.Global_Api+'/background/notice_list_teacher'
        }
        else if(this.user_type==2){
          // console.log("这是学生")
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
      }
    }
  }
</script>

<style scoped>

</style>
