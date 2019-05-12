<template>
  <div class="hello">
        <span>开始周数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model="start_week"
                                    :options="weeknum"
                                    :on-change="myf"
                                    required="required">
                        </v-select>
        <span>结束周数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model="end_week"
                                    :options="weeknum"
                                    :on-change="myf"
                                    required="required">
                        </v-select>
    <br>
        <span>开始节数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model="start"
                                    :options="jienum"
                                    :on-change="myf"
                                    required="required">
                              </v-select>
        <span>结束节数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model="end"
                                    :options="jienum"
                                    :on-change="myf"
                                    required="required">
                              </v-select>
    <br>
    <span style="white-space: pre-wrap">   星  期   ：</span><v-select class="select-pt"
                                                             max-height="80px"
                                                             v-model="day_of_week"
                                                             :options="week"
                                                             :on-change="myf"
                                                             required="required">
  </v-select>
        <span style="white-space: pre-wrap">  教 室   ：</span><v-select class="select-pt"
                                max-height="80px"
                                v-model="classroom"
                                :options="classrooms"
                                :on-change="myf"
                                required="required">
                          </v-select>
        <button @click="dele" class="btn5 btn-danger" style="margin-left: 0;margin-right: 0">删除</button>
        <button class="btn btn-info ddd" style="color: white;margin-left: 20px;" @click="confirm_add">√</button>
  </div>
</template>

<script>

  import index from "../../router";

  export default {
    data(){
      return{
        week:[1,2,3,4,5,6,7],
        weeknum:[1,2,3,4,5,6,7,8,9,10,11,12,13],
        jienum:[1,2,3,4,5,6,7,8,9,10,11,12,13],
        start_week:null,
        end_week:null,
        day_of_week:null,
        start:null,
        end:null,
        classrooms:[],
        classroom:null,
        list:[],
      }
    },
    props: {
      index: {
        type: Number,
        required: true
      },
      items: {
        type: Array,
        default: Array
      },
      course: Object,
    },
    mounted(){
      let data={
        capacity_range:{
          min_capacity:this.course.course_capacity
        },
        course_data:{
          year:this.course.course_year,
          semester:this.course.course_semester
        }
      };
      this.$http.post(this.Global_Api + '/schedule/classroom_list', data).then((res) => {
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
      // my: function (node) {
      //   var thisDom = node.currentTarget
      //   thisDom.parentNode.lastChild.style.display = "inline-block"
      // },
      myf:function () {
        let data={
          capacity_range:{
            min_capacity:this.course.course_capacity
          },
          course_data:{
            year:this.course.course_year,
            semester:this.course.course_semester
          }
        };
        if(this.start_week!==null)
          data['course_data'].start_week=this.start_week;
        if(this.end_week!==null)
          data['course_data'].end_week=this.end_week;
        if(this.day_of_week!==null)
          data['course_data'].day_of_week=this.day_of_week;
        if(this.start!==null)
          data['course_data'].start=this.start;
        if(this.end!==null)
          data['course_data'].end=this.end;
        this.$http.post(this.Global_Api + '/schedule/classroom_list', data).then((res) => {
          if (res.body.error_code !== 0)
            alert(res.body.error_message)
          else {
            let arr = [];
            for (let j = 0; j < res.body.classroom_list.length; j++) {
              arr.push(
                {
                  label: res.body.classroom_list[j].classroom_name,
                  value: res.body.classroom_list[j].classroom_id,
                  capacity: res.body.classroom_list[j].classroom_capacity
                }
              );
            }
            this.classrooms.push(arr);
            //console.log(this.classrooms[i])
          }
        })
      },
      confirm_add:function () {
        //console.log(this.course.course_name)
        //this.$emit('add_del',this.index);

        let data = {
          "user_name": this.$cookie.get('username'),
          "user_token": this.$cookie.get('user_token'),
          "course_id": this.course.course_id,
          "classroom_id": this.classroom.value,
          "date": {
            "end": this.end,
            "start": this.start,
            "day_of_week": this.day_of_week,
            "end_week": this.end_week,
            "start_week": this.start_week
          }
        };
        this.$http.post(this.Global_Api + '/schedule/course_add_dc', data).then((res) => {
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
