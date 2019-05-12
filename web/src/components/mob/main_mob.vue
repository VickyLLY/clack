<template>
    <bar_mob>
      <div class="panel panel-default" style="width: 100%;margin: 0 auto;" ><!--首页新闻部分-->

        <div class="panel-body">

          <div class="panel panel-default" style="width: 100%;margin: auto;"><!--每一个块的新闻部分-->
            <div class="panel-heading">
              <h3>张东东喜提奔驰</h3>
            </div>
            <div class="panel-body" style="white-space: pre-wrap">
              原标题：<strong>曾被马来西亚叫停的中资项目东岸铁路，即将复工了</strong>

              　　4月6日，马来西亚《星洲日报》引述可靠消息源称，中马两国将在马来西亚总理马哈蒂尔访华前，签署有关此前一度暂停的东海岸铁路（ECRL）的新协议，这意味着自去年5月9日马来西亚第十四届大选后马哈蒂尔上台以来命途多舛、一度遭遇“暂停”或“取消”的东海岸铁路将正式复工。

              　　报道指出，负责与中方进行谈判的马来西亚精英顾问团主席达因将在近期前往北京，代表马来西亚政府签署新协议。同时，马来西亚总理马哈蒂尔将于本月24日至28日应中国国家主席习近平邀请，赴华出席第二届“一带一路”国际合作高峰论坛。

              　　根据报道公布的消息，新协议下的东海岸铁路造价从之前的660亿马币降低至500亿马币甚至更低。新版东海岸铁路在路线规划上亦有所调整，据称考虑到环境保护因素，路线将绕过被列为联合国遗产区的“石英区”，即绕过原定的文冬站转而经过位于马来半岛西海岸的森美兰州。
            </div>
          </div>

          <div class="panel panel-default" style="width: 100%;margin: auto;margin-top:20px;">
            <div class="panel-heading">
              <h3>张东东喜提奔驰</h3>
            </div>
            <div class="panel-body" style="white-space: pre-wrap">
              原标题：<strong>曾被马来西亚叫停的中资项目东岸铁路，即将复工了</strong>

              　　4月6日，马来西亚《星洲日报》引述可靠消息源称，中马两国将在马来西亚总理马哈蒂尔访华前，签署有关此前一度暂停的东海岸铁路（ECRL）的新协议，这意味着自去年5月9日马来西亚第十四届大选后马哈蒂尔上台以来命途多舛、一度遭遇“暂停”或“取消”的东海岸铁路将正式复工。

              　　报道指出，负责与中方进行谈判的马来西亚精英顾问团主席达因将在近期前往北京，代表马来西亚政府签署新协议。同时，马来西亚总理马哈蒂尔将于本月24日至28日应中国国家主席习近平邀请，赴华出席第二届“一带一路”国际合作高峰论坛。

              　　根据报道公布的消息，新协议下的东海岸铁路造价从之前的660亿马币降低至500亿马币甚至更低。新版东海岸铁路在路线规划上亦有所调整，据称考虑到环境保护因素，路线将绕过被列为联合国遗产区的“石英区”，即绕过原定的文冬站转而经过位于马来半岛西海岸的森美兰州。
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
