<template>
  <v-select max-height="80px"
            :options="department_name"
            placeholder="请选择学院"
            v-model="choose_name"
            :on-change="post"
            required="required">
  </v-select>
</template>

<script>
  export default {
    name: "department_list",
    data() {
      return {
        choose_id: undefined,
        choose_name: null,
        department_list: [],
        department_name: [],
        department_name_to_id: {},
      }
    },
    mounted() {
      let data = {}
      this.$http.post(this.Global_Api + '/entity/department_list', data).then((res) => {
        this.department_list = res.body.department_list
        for (let i = 0; i < this.department_list.length; i++) {
          this.department_name.push(this.department_list[i].department_name)
          this.department_name_to_id[this.department_list[i].department_name] = this.department_list[i].department_id
        }
      })
    },
    methods: {
      post: function () {
        this.choose_id = this.department_name_to_id[this.choose_name]
        if(this.choose_id===undefined)
          this.$emit('listenToChild', null);
        else
          this.$emit('listenToChild', this.choose_id);
      }
    }
  }
</script>

<style scoped>

</style>
