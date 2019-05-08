<template>
  <div>
    <v-select max-height="80px"
              placeholder="请选择课程类型"
              :options="All"
              v-model="course_type"
              :on-change="post"
              required="required">
    </v-select>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        test:'',
        course_type:null,
        All: [
          {
            label: '必修',
            value: {
              coursetype: 0,
            }
          },
          {
            label: '选修',
            value: {
              coursetype: 1,
            }
          },
        ]
      }
    },
    methods:{
      post:function () {
        if(this.course_type!=null)
          this.$emit('listenToChild', this.course_type.value)
        else
          this.$emit('listenToChild', null)
      },
    }
  }
</script>

<style scoped>

</style>
