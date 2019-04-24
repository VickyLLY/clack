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
            <el-table :data="classroom_list" tooltip-effect="dark" style="width:100%" :default-sort="{prop:'create_time',order:'descending'}" @selection-change="selectionButton">
              <el-table-column type="selection" width="55">
              </el-table-column>
              <el-table-column type="selection" width="55"></el-table-column>
              <el-table-column prop="username" width="100" label="用户名"></el-table-column>
              <el-table-column prop="password" width="100" label="密码"></el-table-column>
              <el-table-column prop="stu_name" width="80" label="姓名" sortable></el-table-column>
              <el-table-column prop="stu_number" label="学号"></el-table-column>
              <el-table-column prop="stu_email" label="邮箱"></el-table-column>
              <el-table-column prop="stu_start_year" label="入学年份" sortable></el-table-column>
              <el-table-column prop="stu_end_year" label="毕业年份" sortable></el-table-column>
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
    <el-dialog title="添加学生" :visible.sync="add_dialog" @close="reset_form('add_form')">
      <el-form :model="add_form" :rules="addRules" ref="add_form" label-width="100px">
        <el-form-item label="姓名" prop="student_name">
          <el-input type="text" v-model="add_form.student_name" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="学号" prop="student_number">
          <el-input type="text" v-model="add_form.student_number" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="班级" prop="student_banji_id">
          <el-input type="text" v-model="add_form.student_banji_id" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="student_email">
          <el-input type="email" v-model="add_form.student_email" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="入学年份" prop="student_start_year">
          <el-input type="text" v-model="add_form.student_start_year" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="毕业年份" prop="student_end_year">
          <el-input type="text" v-model="add_form.student_end_year" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('add_form')">提交</el-button>
          <el-button @click="reset_form('add_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-dialog title="修改学生" :visible.sync="edit_dialog" @close="reset_form('edit_form')">
      <el-form :model="edit_form" :rules="addRules" ref="edit_form" label-width="100px">
        <el-form-item label="姓名" prop="stu_name">
          <el-input type="text" v-model="edit_form.student_name"></el-input>
        </el-form-item>
        <el-form-item label="学号" prop="stu_number">
          <el-input type="text" v-model.number="edit_form.stu_number"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="stu_email">
          <el-input type="email" v-model="edit_form.student_email"></el-input>
        </el-form-item>
        <el-form-item label="入学年份" prop="stu_start_year">
          <el-input type="text" v-model="edit_form.stu_start_year"></el-input>
        </el-form-item>
        <el-form-item label="毕业年份" prop="stu_end_year">
          <el-input type="text" v-model="edit_form.stu_end_year"></el-input>
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
        add_form: {
          student_name: '',
          student_number: '',
          student_banji_id: '',
          student_email: '',
          student_start_year: '',
          student_end_year: '',
        },
        //用于修改用户的对象
        edit_form: {
          student_name: '', //学生姓名
          stu_number: '',//学生学号
          student_email: '', //学生邮箱
          stu_start_year: '', //学生入学年份
          stu_end_year: '', //学生毕业年份
        },
        add_dialog:false,  // 添加的对话框
        edit_dialog:false,  // 编辑的对话框
        classroom_list:[],
        data_rules:{
          student_name: [
            { required: true, message: '请输入姓名', tigger: 'blur' }
          ],
          student_email: [
            { type: 'email', required: true, message: '必须是合法邮箱格式', tigger: 'blur' }
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
              "student": {
                "student_name": this.add_form.student_name,
                "student_number": this.add_form.student_number,
                "student_banji_id": parseInt(this.add_form.student_banji_id),
                "student_email": this.add_form.student_email,
                "student_start_year": parseInt(this.add_form.student_start_year,),
                "student_end_year": parseInt(this.add_form.student_end_year),
              },
            };
            this.$http.post(this.Global_Api + '/background/add_student',data).then(response=>{
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
            this.classroom_list = res.classroom_list;
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
