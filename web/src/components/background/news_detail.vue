<template>
  <div class="body-bg">
    <div class="main">
      <PCbar></PCbar>
      <div class="content" >

        <h3 >{{notice.notice_title}}</h3>
        <p class="subtitle">
          <span>发布人：{{notice.notice_author}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <span>发布时间:{{notice.notice_date }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <!-- <span>浏览人数:457</span> -->
        </p>

        <hr>

        <div class="notice-body">
          {{notice.notice_content}}
        </div>

      </div>
    </div>
  </div>
</template>
<script>
  import PCbar from '../public/Pc_bar'
  export default {
    data(){
      return {
        user_type:this.$cookie.get('user_type'),
        id:this.$route.params.id,
        notice_list:[],
        notice:{}
      }
    },
    // created(){
    //   this.reload()
    // },
    activated(){
      this.judge(),
        this.getNotice(),
        this.reload()
    },
    methods:{

      judge(){
        // 这里因为登录是root，所以先将uers_type==0，实际上应该写==1
        if(this.user_type==1){
          // console.log("这是老师")
          this.news_url=this.Global_Api+'/background/notice_list_teacher'
        }
        else if(this.user_type==2){
          // console.log("这是学生")
          this.news_url=this.Global_Api+'/background/notice_list_student'
        }
      },
      // 获取通知列表1
      getNotice(){
        this.$http.get(this.news_url).then(res=>{
          if(res.body.error_code !== 0)
          {
            alert(res.body.error_message)
          }else{
            this.notice_list=res.body.notice_list
            for(let i=0;i<this.notice_list.length;i++){
              if(this.notice_list[i].notice_id==this.id){
                this.notice=this.notice_list[i];break;
              }
            }
          }
        })
      }

    },
    // watch:{
    //   '$route'(to,from){
    //     this.isRouterAlive=false;
    //     this.key=Math.random()*1000;
    //     this.$nextTick(()=>(this.isRouterAlive=true))
    //   }
    // },
    components:{
      PCbar
    },
  }
</script>
<style scoped>
  .body-bg{
    position: absolute;
    width: 100%;
    height: 100%;
    top:0;
    left: 0;
    overflow: auto;
    background-color: #f0f0f0;
    padding-top: 50px;
  }
  .main{
    background-color: #fff;
    margin: 20px 100px 30px;
    height: 100%;
    padding: 0 50px;
  }
  .nav{
    position: absolute;
    top:0;
    left: 0;
    width: 100%;
    background-color: #337ab7;
    color: white;
    font-size: 20px;
    line-height: 50px;
    height: 50px;
    padding-left: 80px;
  }
  h3{
    text-align-last: center;
    padding: 20px 0 0;
  }
  .subtitle{
    text-align: center;
  }
  .notice-body{
    padding:0 5px;
  }
</style>
