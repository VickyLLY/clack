<template>
  <div>
    <PC_bar></PC_bar>
    <News></News>
  </div>
</template>

<script>
  import PC_bar from './PC_bar'
  import News from './news'

  export default {
    name: "main",
    components: {
      PC_bar,
      News
    },
    data(){
      return{

      }
    },
    mounted() {
      if (this.$cookie.get('username') == null)
        this.$router.push('/')
    },
    method: {
      select_course: function () {
        if (this.$cookie.get('user_type') === 1) {
          this.$router.push({
            path: '/main/stu_sel_course',
          });
        } else if (this.$cookie.get('user_type') === 2) {
          this.$router.push({
            path: '/main/tea_sel_course',
          });
          location.reload()
        }else{
          this.$router.push({
            path: '/main/man_sel_course',
          });
          location.reload();
        }
      }
    }
  }

</script>

<style>

</style>
