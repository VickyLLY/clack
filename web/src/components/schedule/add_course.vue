<template>
  <div>
    <PC_bar></PC_bar>
    <add_course_component></add_course_component>
  </div>
</template>

<script>
  import PC_bar from '../public/PC_bar'
  import add_course_component from '../public/add_course_component'

  export default {
    name: "add_course",
    components: {
      PC_bar,
      add_course_component
    },
    mounted() {
      if(this.$cookie.get('username')==null)
        this.$router.push('/')
    }
  }
</script>

<style scoped>

</style>
