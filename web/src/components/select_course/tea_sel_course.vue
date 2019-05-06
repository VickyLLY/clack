<template>
  <div>
    <PC_bar></PC_bar>
    <table class="table table-hover">

      <caption class="table-bar">查看课程信息</caption>
      <thead>
      <tr>
        <th class="table-bar">学年</th>
        <th class="table-bar">学期</th>
        <th class="table-bar">课程代码</th>
        <th class="table-bar">课程名称</th>
        <th class="table-bar">课程性质</th>
        <th class="table-bar">学分</th>
        <th class="table-bar">任课老师</th>
        <th class="table-bar">课程容量</th>
        <th class="table-bar">已选人数</th>
        <th class="table-bar">开课学院</th>
      </tr>
      </thead>
      <tbody class="table-bar">
      <tr>
        <td>2018-2019</td>
        <td>1</td>
        <td>A00001</td>
        <td>计算机组成原理</td>
        <td>专业必修课</td>
        <td>3.5</td>
        <td>吴越</td>
        <td>200</td>
        <td>188</td>
        <td>信息科学与技术学院</td>
      </tr>
      <tr>
        <td>2018-2019</td>
        <td>1</td>
        <td>A00002</td>
        <td>计算机网络</td>
        <td>专业必修课</td>
        <td>3.5</td>
        <td>何川</td>
        <td>200</td>
        <td>188</td>
        <td>信息科学与技术学院</td>
      </tr>
      <tr>
        <td>2018-2019</td>
        <td>1</td>
        <td>A00002</td>
        <td>计算机网络</td>
        <td>专业必修课</td>
        <td>3.5</td>
        <td>何川</td>
        <td>200</td>
        <td>188</td>
        <td>信息科学与技术学院</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
    import PC_bar from "../public/PC_bar";
    export default {
        name: "tea_sel_course",
      components: {PC_bar}
    }
</script>

<style scoped>
.table-bar {
  text-align: center;
}
</style>
