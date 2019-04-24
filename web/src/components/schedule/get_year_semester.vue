<template>
  <div>
    <v-select max-height="80px"
              placeholder="请选择学年学期"
              :options="All"
              v-model="year_semester"
              :on-change="post"
              required="required">
    </v-select>
  </div>
</template>

<script>
  export default {
    name: "get_year_semester",
    data() {
      return {
        test:'',
        year_semester:null,
        All: [
          {
            label: '2018 - 1',
            value: {
              year: 2018,
              semester: 1,
            }
          },
          {
            label: '2018 - 2',
            value: {
              year: 2018,
              semester: 2,
            }
          },
          {
            label: '2018 - 3',
            value: {
              year: 2018,
              semester: 3,
            }
          },
          {
            label: '2019 - 1',
            value: {
              year: 2019,
              semester: 1,
            }
          },
          {
            label: '2019 - 2',
            value: {
              year: 2019,
              semester: 2,
            }
          },
          {
            label: '2019 - 3',
            value: {
              year: 2019,
              semester: 3,
            }
          }
        ]

      }
    },
    methods:{
      post:function () {
        if(this.year_semester!=null)
          this.$emit('listenToChild', this.year_semester.value)
        else
          this.$emit('listenToChild', null)
      },
    }
  }
</script>

<style scoped>

</style>
