<template>
    <div id="man_view_msg">
      <PC_bar></PC_bar>
      <div class="button">
        <button  type="button" class="btn btn-info"><router-link to ="/main/man_sel_course" >返回</router-link></button>
      </div>
    </div>
</template>

<script>
  import PC_bar from "../public/PC_bar";
  export default {
    name: "man_view_msg",
    components:{
      "PC_bar":PC_bar,
    },
    data () {
      return {
        msg: {}
      }
    }
  }
</script>

<style scoped>
#man_view_msg{
  margin: 0 auto;
  background: gainsboro;
  max-width: 960px;
}
.button{
  margin: 0 auto;
  position: relative;
  left: 93%;
}


</style>
