<template>
  <div>
    <h3>添加课程</h3>
    <input type="text" class="form-control" placeholder="请输入课程名" v-model="course_name" required="required">
    <br>
    <input type="text" class="form-control" placeholder="请输入课程学分" v-model="course_credit" required="required">
    <br>
    <div class="v_select">
      <v-select max-height="80px" placeholder="请选择课程类型(0:必修；1:选修)" :options="type" v-model="course_type"></v-select>
      <br>
      <v-select max-height="80px" placeholder="请选择学年" :options="year" v-model="course_year"></v-select>
      <br>
      <v-select max-height="80px" placeholder="请选择学期" :options="semester" v-model="course_semester"></v-select>
      <br>
      <v-select max-height="80px" placeholder="请选择课程容量" :options="capacity" v-model="course_capacity"></v-select>
      <br>
      <department @listenToChild="get"></department>

    </div>
    <br>
    <button type="submit" class="btn btn-default" v-on:click="confirm">确认添加</button>
  </div>
</template>

<script>
  let type = ['0', '1'];
  let year = [];
  let semester = [1, 2, 3];
  let capacity = [50, 100, 150];
  for (let i = 2016; i <= 2030; i++)
    year.push(i);
  import department from './department_list'

  export default {
    name: "add_course_component",
    components: {
      department
    },
    data() {
      return {
        type: type,
        year: year,
        semester: semester,
        capacity: capacity,
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        course_name: '',
        course_credit: '',
        course_type: '',
        course_year: '',
        course_semester: '',
        course_capacity: '',
        course_department_id: ''
      }
    },

    methods: {
      get(val) {
        this.course_department_id = val
      },
      confirm: function () {
        //console.log(this.user_name)
        if (
          this.course_name === "" || this.course_credit === "" || this.course_type === "" || this.course_year === "" ||
          this.course_semester === "" || this.course_capacity === "" || this.course_department_id === ""
        )
          alert("信息未填写完全")
        else {
          let data = {
            "user_name": this.user_name,
            "user_token": this.user_token,
            "course": {
              "course_name": this.course_name,
              "course_credit": parseInt(this.course_credit),
              "course_type": parseInt(this.course_type),
              "course_year": parseInt(this.course_year),
              "course_semester": parseInt(this.course_semester),
              "course_capacity": parseInt(this.capacity),
              "course_department_id": parseInt(this.course_department_id)
            },
          }
          this.$http.post(this.Global_Api + '/schedule/new_course', data).then((res) => {
            if (res.body.error_code !== 0) {
              alert(res.body.error_message)
            } else {
              alert("添加成功")
              location.reload()
            }
          })
        }
      }
    }
  }
</script>

<style scoped>
  h3 {
    text-align: center;
  }

  div.choose {
    text-align: center;
    margin-top: 50px;
  }

  div.v_select {
    display: block;
    margin: 0 auto;
    width: 300px;
  }

  input.form-control {
    display: block;
    margin: 0 auto;
    width: 300px;
  }

  button.btn {
    display: block;
    margin: 0 auto;
    width: 300px;
  }
</style>
