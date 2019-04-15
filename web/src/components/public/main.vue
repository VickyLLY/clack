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
    }
  }
</script>

<style>

</style>
