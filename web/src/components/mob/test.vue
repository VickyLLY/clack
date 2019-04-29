<template>
  <div class="hello">
    <span>上课时间：</span><input type="text" class="form-control" required="required" v-on:input ="my($event)" v-model=items[index].time>
        <br>
        <span>上课地点：</span><input type="text" class="form-control" required="required" v-on:input ="my($event)" v-model=items[index].place>
        <button @click="dele" class="btn5 btn-danger">删除</button>
        <button  class="btn btn-info" style="color: white">√</button>
  </div>
</template>

<script>

  import index from "../../router";

  export default {
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
        this.$emit('say',this.index);
      },
      my: function (node) {
        var thisDom = node.currentTarget
        thisDom.parentNode.lastChild.style.display = "inline-block"
      },
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
    vertical-align: 1px;
  }
  .btn5{
    width: 60px;
    border: 0;
    height: 35px;
    line-height: 35px;
    border-radius: 5px;
    font-size: 17px;
    margin: 25px;
    color: white;
  }
  a{
    text-decoration: none;
    outline: 0 none;
  }
  .hello{
    border-bottom: 1px solid #ddd;
    margin-bottom: 5px;
   }
  a:hover{color:black;}
  li{
    display: block;
    height: 50px;
    width: 313px;
    border-left: 0px solid black;
    border-bottom: 0px solid black;
    border-right: 0px solid black;
    line-height: 50px;
    padding: 0;
  }
  li::before{
    content: "";
    display: inline-block;
    width: 30px;
  }
  ul{
    margin-left: -55px;
  }
  li:hover{
    background: #f5f5f5;
  }
  ::-webkit-scrollbar {
    width: 0px;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
  }
  #cnmx{
    margin-left:15%;
    margin-top: 30px;
    height: 600px;
    width: 300px;
    float: left
  }
  #selecttype{
    padding: 0;
    margin: 10px;
  }
  #xianshi{
    border: 1px solid #ddd;
    position: absolute;
    width: 50%;
    height: 79.5%;
    margin-left: 40%;
    margin-top: 31px;
  }
  #change-block,#change-block2{
    border: 3px solid #f5f5f5;
    width: 90%;
    height: 75%;
    display: none;
    margin: 0 auto;
    margin-top: 15px;
    background-color: #f5f5f5;
    animation: donghua 1s;
  }
  #change-block span,
  #change-block2 span{
    font-weight: bold;
  }
  li{
    cursor: pointer;
  }
  .change-content{
    border-bottom: 1px solid #ddd;
    margin: 30px 10%;
    padding: 5px;
  }
  .btn3{
    display: inline-block;
    height: 30px;
    animation: donghua 2s;
    color: white;
  }
  #change-block v-select{
    width: 50px;
  }
  #title,#title2{
    animation: donghua 2s;
  }
  @keyframes donghua{
    0%{
      opacity: 0;
    }
    100%{
      opacity: 1;
    }
  }
  .form-control,.form-select{
    width:250px;
    display: inline-block;
  }
  #change-block{
    margin-bottom: 50px;
  }
  #change-block2{
    height: 400px;
  }
  #title,#title2{
    border-left:2px solid rgb(35,149,241);
    padding-left: 10px;
  }
  .btn2{
    width: 35px;
    border: 0;
    height: 35px;
    line-height: 35px;
    border-radius: 5px;
    font-size: 22px;
    margin: 25px;
  }
</style>
