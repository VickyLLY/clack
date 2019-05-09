<template>
  <div>
    <!--主界面-->
    <el-container>
      <el-header>
        <h1>学生信息</h1>
      </el-header>
      <el-main>
        <!--添加删除按钮-->
        <el-row>
          <el-col :span="20" :offset="1">
            <div class="fr margin40">
              <el-button size="mini" type="primary" icon="el-icon-plus" @click="add_dialog = true">添加</el-button>
              <el-button size="mini" type="danger" icon="el-icon-delete" @click="delete_button">删除</el-button>
            </div>
          </el-col>
        </el-row>
        <!--数据展示列表-->
        <el-row>
          <el-col :span="24">
            <el-table :data="data_list" tooltip-effect="dark" style="width:100%" :default-sort="{prop:'create_time',order:'descending'}" @selection-change="selectionButton">
              <el-table-column type="selection" width="55">
              </el-table-column>
              <el-table-column prop="student_name" label="学生姓名" sortable>
              </el-table-column>
              <el-table-column prop="student_number" label="学生学号" sortable>
              </el-table-column>
              <el-table-column prop="student_banji_id" label="学生班级" sortable>
              </el-table-column>
              <el-table-column prop="student_email" label="学生邮箱" sortable>
              </el-table-column>
              <el-table-column prop="student_start_year" label="入学年份" sortable>
              </el-table-column>
              <el-table-column prop="student_end_year" label="毕业年份" sortable>
              </el-table-column>
              <el-table-column label="操作" width="250">
                <template slot-scope="scope">
                  <el-button type="success" size="small" @click="set_data(scope.row)">
                    编辑
                  </el-button>
                  <el-button type="danger" size="small" @click="delete_data(scope.row)">删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <!--下一页按钮-->
        <el-row>
          <el-col :span="24">
            <div class="block">
              <el-pagination layout="prev,pager,next" :total="total" :page-size="5" @current-change="page_change">
              </el-pagination>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
    <!--添加信息窗口-->
    <el-dialog title="添加教室信息" :visible.sync="add_dialog" @close="reset_form('add_form')">
      <el-form :model="add_form" :rules="data_rules" ref="add_form" label-width="100px">
        <el-form-item label="教室名称" prop="classroom_name">
          <el-input type="text" v-model="add_form.classroom_name" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="教室容量" prop="classroom_capacity">
          <el-input type="text" v-model="add_form.classroom_capacity" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit_form('add_form')">提交</el-button>
          <el-button @click="reset_form('add_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!--修改信息窗口-->
    <el-dialog title="修改用户" :visible.sync="edit_dialog" @close="reset_form('edit_form')">
      <el-form :model="edit_form" :rules="data_rules" ref="edit_form" label-width="100px">
        <el-form-item label="教室名称" prop="classroom_name">
          <el-input type="text" v-model="edit_form.classroom_name"></el-input>
        </el-form-item>
        <el-form-item label="教室容量" prop="classroom_capacity">
          <el-input type="text" v-model="edit_form.classroom_capacity"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="updateUser">修改</el-button>
          <el-button @click="reset_form('edit_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>


<script>
  import axios from 'axios'

  export default{
    name:"edit_classroom",
    // 组件渲染完毕后调用get_data, 来获取所有数据
    mounted:function(){
      this.get_data();
    },
    data(){
      return {
        user_name:this.$cookie.get('username'),
        user_token:this.$cookie.get('user_token'),
        add_form:{
          classroom_name:'',
          classroom_capacity:''
        },
        edit_form:{
          "classroom_name":'',
          "classroom_capacity":''
        },
        add_dialog:false,  // 添加的对话框
        edit_dialog:false,  // 编辑的对话框
        data_list:[],
        data_rules:{
          classroom_name:[
            {required:true,message:'请输入教室名称',tigger:'blur'},
            {min:3,max:16,message:'请输入合法的教室名称',tigger:'blur'}
          ],
          classroom_capacity:[
            {required:true,message:'请输入姓名',tigger:'blur'}
          ]
        },
        total:0,
        multiple_selection:[]
      }
    },
    methods:{
      //表单提交
      submit_form:function(form_name){
        this.$refs[form_name].validate((valid)=>{
          if(valid){
            let data = {
              "user_name": this.user_name,
              "user_token": this.user_token,
              "classroom": {
                "classroom_name": this.add_form.classroom_name,
                "classroom_capacity": parseInt(this.add_form.classroom_capacity)
              }
            };
            this.$http.post(this.Global_Api + '/entity/new_classroom',data).then(response=>{
              let res = response.body;
              if(res.error_code === 0){
                this.$message.success('添加成功');
                this.reset_form('add_form');
                this.get_data();  // 重新获取最新数据
              }else{
                this.$message.error("错误："+res.error_message);
              }
            }).catch(err=>{
              console.log(err);
            })
          }else{
            return false;
          }
        })
      },
      reset_form:function(form_name){
        if(form_name === 'add_form'){
          //将新增的弹出框关闭
          this.add_dialog = false;
        }else if(form_name === 'edit_form'){
          //编辑的弹出框关掉
          this.edit_dialog = false;
        }
        //将弹出框里面的内容清空
        this.$refs[form_name].resetFields();
      },
      get_data:function(page){
        axios.get('/users/get_data',{
          params:{
            page:page || 1,
            pageSize:5
          }
        })
          .then(response=>{
            var res = response.data;
            this.data_list = res.data_list;
            this.total = res.count;
          }).catch(err=>{
          console.log(err);
        })
      },
      page_change:function(value){
        this.get_data(value);
      },
      set_data:function(row){
        //编辑的弹出框开启
        this.edit_dialog = true;
        //可以使用row里面的数据，将整行的用户信息输出
        this.edit_form.classroom_name = row.classroom_name;
        this.edit_form.classroom_capacity = row.classroom_capacity;
      },
      updateUser:function(){
        axios.post('/users/updateUser',this.edit_form)
          .then(response=>{
            var res = response.data;
            if(res.status === '0'){
              this.reset_form('edit_form');
              this.$message.success('修改成功');
              this.get_data();
            }
          }).catch(err=>{
          console.log(err);
        })
      },
      delete_data:function(row){
        this.$confirm('此操作将永久删除该项'+ row.classroom_name +', 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center:true
        }).then(() => {
          axios.post('/users/remove',row).then(data=>{
            this.$message.success('删除成功!')
            this.get_data();
          })
        }).catch(() => {
          this.$message.info('已取消删除');
        });
      },
      selectionButton:function (val) {
        this.multiple_selection= val
      },
      delete_button:function(){
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          axios.post('/users/deletes', this.multiple_selection).then(data=>{
            if (data.data.status === '0') {
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              this.get_data()
            }
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        })
      }
    }
  }
</script>

<style>
  h1 {
    text-align:center;
  }
  .clearfix {
    clear:both;
  }
  .fr {
    float:right;
  }
  .fl {
    float:left;
  }
  .margin40 {
    margin-top:40px;
  }
  .block {
    margin-top:20px;
    float:right;
  }
</style>
