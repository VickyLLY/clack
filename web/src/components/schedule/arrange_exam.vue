<template>
    <div class="hello">
        <span>考试名称：</span>
        <input type="text"  class="form-control" v-model="exam_name" required="required">
        <span>考试开始时间：</span>
        <date-picker v-model="start_date_time" :config="config"></date-picker>
        <span>考试结束时间：</span>
        <date-picker v-model="end_date_time" :config="config"></date-picker>
        <span>考试地点：</span>
        <v-select class="select-pt"
                  max-height="80px"
                  v-model="classroom"
                  :options="classrooms"
                  required="required">
        </v-select>
      <button @click="dele" class="btn5 btn-danger" style="margin-left: 0;margin-right: 0">删除</button>
      <button class="btn btn-info ddd" style="color: white;margin-left: 20px;" @click="confirm_add">√</button>
    </div>
</template>

<script>
  import datePicker from 'vue-bootstrap-datetimepicker';

  // Import date picker css
  import 'eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css';
    export default {
      name: "arrange_exam",
      components:{
        datePicker
      },
      data(){
        return{
          config: {
            format: 'YYYY-MM-DD HH:mm',
            useCurrent: false,
          },
          start_date_time:null,
          end_date_time:null,
          exam_name:null,
          classrooms:[],
          classroom:null,
        }
      },
      props: {
        index: {
          type: Number,
          required: true
        },
        exam_items: {
          type: Array,
          default: Array
        },
        course: Object,
      },
      mounted() {
        console.log(this.course)
        console.log(this.exam_items)
        this.$http.post(this.Global_Api + '/schedule/classroom_list', {}).then((res) => {
          console.log(res.body.error_message)
          for (let i = 0; i < res.body.classroom_list.length; i++) {
            let dic={
              label:res.body.classroom_list[i].classroom_name,
              value:res.body.classroom_list[i].classroom_id,
            }
            this.classrooms.push(dic);
          }
        })
      },
      methods:{
        dele: function () {
          this.$emit('del',this.index);
        },
        confirm_add:function () {
          let data={
            user_name:this.$cookie.get('username'),
            user_token:this.$cookie.get('user_token'),
            exam_name:this.exam_name,
            start_date_time: this.start_date_time,
            end_date_time: this.end_date_time,
            exam_course_id: this.course.course_id,
            classroom_id: this.classroom.value,
          };
          this.$http.post(this.Global_Api + '/schedule/add_exam', data).then((res) => {
            alert(res.body.error_message)
            if(res.body.error_code===0)
              this.$emit('add_del',this.index);
          })
        }
      }
    }
</script>

<style scoped>
  *{
    list-style: none;
    text-decoration: none;
    color:black;
    outline: 0 none;
  }
  .btn-info{
    animation: donghua 1s;
    vertical-align: -1px;
    width: 35px;
    height: 30px;
  }
  .btn5{
    width: 60px;
    border: 0;
    height: 30px;
    line-height: 30px;
    border-radius: 5px;
    font-size: 17px;
    margin-left: 25px;
    margin-right: 25px;
    color: white;
  }
  .select-pt{
    white-space: nowrap;
    width: 150px;
    display: inline-block;
    margin-bottom: 25px;
    margin-right: 10px;
  }
  .hello{
    border-bottom: 1px solid #ddd;
    margin-bottom: 15px;
    padding-bottom: 15px;
  }
  ::-webkit-scrollbar {
    width: 0px;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
  }
  #change-block span,
  #change-block2 span{
    font-weight: bold;
  }
  @keyframes donghua{
    0%{
      opacity: 0;
    }
    100%{
      opacity: 1;
    }
  }
  .form-control,{
    width:250px;
    display: inline-block;
  }
</style>
