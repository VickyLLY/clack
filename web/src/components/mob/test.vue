<template>
  <div class="hello">
        <span>开始周数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model=items[index].start_week
                                    :options="weeknum"
                                    :on-change="myf"
                                    required="required">
                        </v-select>
        <span>结束周数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model=items[index].end_week
                                    :options="weeknum"
                                    :on-change="myf"
                                    required="required">
                        </v-select>
        <span style="white-space: pre-wrap">星 期：</span><v-select class="select-pt"
                                                                       max-height="80px"
                                                                       v-model=items[index].day_of_week
                                                                       :options="week"
                                                                        :on-change="myf"
                                                                       required="required">
                                                                </v-select>
    <br>
        <span>开始节数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model=items[index].start
                                    :options="jienum"
                                    :on-change="myf"
                                    required="required">
                              </v-select>
        <span>结束节数：</span><v-select class="select-pt"
                                    max-height="80px"
                                    v-model=items[index].end
                                    :options="jienum"
                                    :on-change="myf"
                                    required="required">
                              </v-select>
        <button @click="dele" class="btn5 btn-danger">删除</button>
        <button class="btn btn-info ddd" style="color: white">√</button>
  </div>
</template>

<script>

  import index from "../../router";

  export default {
    data(){
      return{
        week:[1,2,3,4,5,6,7],
        weeknum:[1,2,3,4,5,6,7,8,9,10,11,12,13],
        jienum:[1,2,3,4,5,6,7,8,9,10,11,12,13]
      }
    },
    props: {
      index: {
        type: Number,
        required: true
      },
      items: {
        type: Array,
        default: Array
      }
    },
    methods:{
      dele: function () {
        this.$emit('del',this.index);
      },
      // my: function (node) {
      //   var thisDom = node.currentTarget
      //   thisDom.parentNode.lastChild.style.display = "inline-block"
      // },
      myf:function () {
        document.getElementsByClassName("ddd")[this.index].style.display = "inline-block"
      }
    }
  }
</script>

<style scoped>
  *{
    list-style: none;
    text-decoration: none;
    color:black;
    outline: 0 none;
  }
  .btn-info{
    animation: donghua 1s;
    vertical-align: -1px;
    width: 35px;
    height: 30px;
  }
  .btn5{
    width: 60px;
    border: 0;
    height: 30px;
    line-height: 30px;
    border-radius: 5px;
    font-size: 17px;
    margin-left: 25px;
    margin-right: 25px;
    color: white;
  }
  .select-pt{
    width: 95px;
    display: inline-block;
    margin-bottom: 25px;
    margin-right: 15px;
  }
  .hello{
    border-bottom: 1px solid #ddd;
    margin-bottom: 15px;
    padding-bottom: 15px;
   }
  ::-webkit-scrollbar {
    width: 0px;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
  }
  #change-block span,
  #change-block2 span{
    font-weight: bold;
  }
  @keyframes donghua{
    0%{
      opacity: 0;
    }
    100%{
      opacity: 1;
    }
  }
  .form-control,{
    width:250px;
    display: inline-block;
  }
</style>
