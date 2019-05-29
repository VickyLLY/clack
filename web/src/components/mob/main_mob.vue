<template>
    <bar_mob>
      <div class="panel panel-default" style="width: 100%;margin: 0 auto;" ><!--首页新闻部分-->

        <div class="panel-body">

          <div class="panel panel-default" style="width: 100%;margin: auto;"><!--每一个块的新闻部分-->
            <div class="panel-heading">
            </div>
            <div class="panel-body" style="white-space: pre-wrap">
            </div>
          </div>


        </div>

      </div><!--首页新闻部分-->
    </bar_mob>
</template>

<script>
    import bar_mob from './bar_mob'

    export default {
      data(){
        return{
          user_type: this.$cookie.get('user_type'),
        }
      },
      components: {
        bar_mob
      }
    }
</script>

<style scoped>

</style>
