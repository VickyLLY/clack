<template>
  <div>
    <PC_bar></PC_bar>
    <!--主界面-->
    <el-container>
      <el-header>
        <h1>编辑学生信息</h1>
      </el-header>
      <el-main>
        <!--添加删除按钮-->
        <el-row>
          <el-col :span="20" :offset="1">
            <div class="fr margin40">
              <el-button size="mini" type="primary" icon="el-icon-plus" @click="add_dialog = true">添加</el-button>
              <el-button size="mini" type="danger" icon="el-icon-delete" @click="delete_multiple_data">删除</el-button>
            </div>
          </el-col>
        </el-row>
        <!--数据展示列表-->
        <el-row>
          <el-col :span="24">
            <el-table :data="data_list" tooltip-effect="dark" style="width:100%" :default-sort="{prop:'create_time',order:'descending'}" @selection-change="get_multiple_selection">
              <el-table-column type="selection" width="55">
              </el-table-column>
              <el-table-column prop="student_number" label="学生学号" sortable>
              </el-table-column>
              <el-table-column prop="student_name" label="学生姓名" sortable>
              </el-table-column>
              <el-table-column prop="student_banji_id" label="所属班级ID" sortable>
              </el-table-column>
              <el-table-column prop="student_email" label="学生邮箱" sortable>
              </el-table-column>
              <el-table-column prop="student_start_year" label="入学年份" sortable>
              </el-table-column>
              <el-table-column prop="student_end_year" label="毕业年份" sortable>
              </el-table-column>
              <el-table-column label="操作">
                <template slot-scope="scope">
                  <el-button type="success" size="small" @click="set_data(scope.row)">
                    编辑
                  </el-button>
                  <el-button type="danger" size="small" @click="delete_single_data(scope.row)">删除
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
              <el-pagination
                @size-change="change_page_size"
                @current-change="change_page"
                :current-page="current_page"
                :page-sizes="[10, 30, 50]"
                :page-size="page_size"
                layout="total, sizes, prev, pager, next, jumper"
                :total="total"
                background
                :pager-count="11">
              </el-pagination>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
    <!--添加信息窗口-->
    <el-dialog title="添加" :visible.sync="add_dialog" @close="reset_form('add_form')">
      <el-form :model="add_form" :rules="data_rules" ref="add_form" label-width="100px">
        <el-form-item label="学生用户名" prop="student_user_name">
          <el-input type="text" v-model="add_form.student_user_name" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="学生密码" prop="student_user_password">
          <el-input type="password" v-model="add_form.student_user_password" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="student_user_password_again">
          <el-input type="password" v-model="add_form.student_user_password_again" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="学生学号" prop="student_number">
          <el-input type="text" v-model="add_form.student_number" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="学生姓名" prop="student_name">
          <el-input type="text" v-model="add_form.student_name" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="所属班级ID" prop="student_banji_id">
          <el-input type="text" v-model="add_form.student_banji_id" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="学生邮箱" prop="student_email">
          <el-input type="text" v-model="add_form.student_email" auto-complete="off">
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
          <el-button type="primary" @click="add_submit">提交</el-button>
          <el-button @click="reset_form('add_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!--修改信息窗口-->
    <el-dialog title="编辑" :visible.sync="edit_dialog" @close="reset_form('edit_form')">
      <el-form :model="edit_form" :rules="data_rules" ref="edit_form" label-width="100px">
        <el-form-item label="学生姓名" prop="student_name">
          <el-input type="text" v-model="edit_form.student_name"></el-input>
        </el-form-item>
        <el-form-item label="所属班级ID" prop="student_banji_id">
          <el-input type="text" v-model="edit_form.student_banji_id"></el-input>
        </el-form-item>
        <el-form-item label="学生邮箱" prop="student_email">
          <el-input type="text" v-model="edit_form.student_email"></el-input>
        </el-form-item>
        <el-form-item label="入学年份" prop="student_start_year">
          <el-input type="text" v-model="edit_form.student_start_year"></el-input>
        </el-form-item>
        <el-form-item label="毕业年份" prop="student_end_year">
          <el-input type="text" v-model="edit_form.student_end_year"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="edit_submit">修改</el-button>
          <el-button @click="reset_form('edit_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>


<script>
  import PC_bar from '../public/PC_bar';

  export default {
    name: 'edit_student',
    components: {
      PC_bar
    },
    // 组件渲染完成后，获取数据
    mounted: function() {
      this.get_data();
    },
    data() {
      return {
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        add_form: {
          student_user_name: '',
          student_user_password: '',
          student_user_password_again: '',
          student_name: '',
          student_number: '',
          student_banji_id: '',
          student_email: '',
          student_start_year: '',
          student_end_year: ''
        },
        edit_form: {
          student_id: '',
          student_name: '',
          student_number: '',
          student_banji_id: '',
          student_email: '',
          student_start_year: '',
          student_end_year: ''
        },
        add_dialog: false,
        edit_dialog: false,
        data_rules: {
          student_user_name: [
            { required: true, message: '请输入学生用户名', tigger: 'blur' }
          ],
          student_user_password: [
            { required: true, message: '请输入学生密码', tigger: 'blur' }
          ],
          student_user_password_again:[
            { required: true, message: '请再次输入学生密码', tigger: 'blur' },
            {
              validator: (rule, value, callback) => {
                if(value === '') {
                  callback(new Error('请再次输入学生密码'));
                }
                else if(value !== this.add_form.student_user_password) {
                  callback(new Error('两次输入密码必须一致'));
                }
                else {
                  callback();
                }
              },
              trigger: 'blur'
            }
          ],
          student_number:[
            { required: true, message: '请输入学生学号', tigger: 'blur'},
            { min: 9, max: 12, message: '长度为9~12个字符', tigger: 'blur'}
          ],
          student_name: [
            { required: true, message: '请输入姓名', tigger: 'blur' }
          ],
          student_banji_id:[
            { required: true, message: '请输入所属班级ID', tigger: 'blur' }
          ],
          student_email: [
            { type: 'email', required: true, message: '必须是合法邮箱格式', tigger: 'blur' }
          ],
          student_start_year: [
            { required: true, message: '请输入年份', tigger: 'blur' },
            { min: 4, max: 4, message: '请输入合法的年份', tigger: 'blur'}
          ],
          student_end_year: [
            { required: true, message: '请输入年份', tigger: 'blur' },
            { min: 4, max: 4, message: '请输入合法的年份', tigger: 'blur' }
          ]
        },
        // 数据显示列表
        data_list: [],
        // 多选列表
        multiple_selection: [],
        // 分页相关数据
        current_page: 1,
        page_size: 10,
        total: 0
      }
    },
    methods: {
      // 提交添加窗口数据
      add_submit: function() {
        console.info(this.add_form.student_user_name);
        this.$refs['add_form'].validate((valid) => {
          if(valid) {
            this.$http.post(this.Global_Api + '/user/signup_student', {
              user: {
                user_name: this.add_form.student_user_name,
                user_password: this.add_form.student_user_password
              },
              student: {
                student_name: this.add_form.student_name,
                student_number: this.add_form.student_number,
                student_email: this.add_form.student_email,
                student_start_year: parseInt(this.add_form.student_start_year),
                student_end_year: parseInt(this.add_form.student_end_year),
                student_banji_id: parseInt(this.add_form.student_banji_id)
              }
            }).then(response => {
              if(response.body.error_code === 0) {
                this.$message.success('添加成功！');
                this.reset_form('add_form');
                this.get_data();
              }
              else {
                this.$message.error('错误' + response.body.error_code + '：'
                  + response.body.error_message + '（' + response.body.exception + '）');
              }
            }).catch(error => {
              console.log(error);
            });
          }
        })
      },
      // 重置当前窗口
      reset_form: function(form_name) {
        if(form_name === 'add_form') {
          this.add_dialog = false;
        }
        else if(form_name === 'edit_form') {
          this.edit_dialog = false;
        }
        // 清空窗口数据
        this.$refs[form_name].resetFields();
      },
      // 获取主界面数据
      get_data: function() {
        this.$http.post(this.Global_Api + '/background/student_list').then(response => {
          let start = (this.current_page - 1)*this.page_size;
          let end  = start + this.page_size;
          if(end > response.data.student_list.length) {
            end = response.data.student_list.length;
          }
          this.data_list = response.data.student_list.slice(start, end);
          this.total = response.data.student_list.length;
        }).catch(error => {
          console.log(error);
        })
      },
      // 设置编辑窗口数据
      set_data: function(row) {
        this.edit_dialog = true;
        this.edit_form.student_id = row.student_id;
        this.edit_form.student_name = row.student_name;
        this.edit_form.student_number = row.student_number;
        this.edit_form.student_banji_id = row.student_banji_id;
        this.edit_form.student_email = row.student_email;
        this.edit_form.student_start_year = row.student_start_year;
        this.edit_form.student_end_year = row.student_end_year;
      },
      // 提交编辑窗口数据
      edit_submit: function() {
        this.$refs['edit_form'].validate((valid) => {
          if(valid) {
            this.$http.post(this.Global_Api + '/background/edit_student', {
              user_name: this.user_name,
              user_token: this.user_token,
              student_id: this.edit_form.student_id,
              student_name: this.edit_form.student_name,
              student_number: this.edit_form.student_number,
              student_banji_id: parseInt(this.edit_form.student_banji_id),
              student_email: this.edit_form.student_email,
              student_start_year: parseInt(this.edit_form.student_start_year),
              student_end_year: parseInt(this.edit_form.student_end_year)
            }).then(response => {
              if(response.body.error_code === 0) {
                this.$message.success('编辑成功！');
                this.reset_form('edit_form');
                this.get_data();
              }
              else {
                this.$message.error('错误' + response.body.error_code + '：'
                  + response.body.error_message + '（' + response.body.exception + '）');
              }
            }).catch(error => {
              console.log(error);
            });
          }
        })
      },
      // 删除单项数据
      delete_single_data: function(row) {
        this.$confirm('删除后不可恢复，是否继续？', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.post(this.Global_Api + '/background/del_student', {
            user_name: this.user_name,
            user_token: this.user_token,
            student_number: row.student_number
          }).then(response => {
            if(response.body.error_code === 0) {
              this.$message.success('删除成功！');
              this.get_data();
            }
            else {
              this.$message.error('错误' + response.body.error_code + '：'
                + response.body.error_message + '（' + response.body.exception + '）');
            }
          }).catch(error => {
            console.log(error);
          });
        }).catch(() => {
          this.$message.info('操作已取消！');
        });
      },
      // 获取多选项
      get_multiple_selection: function(rows) {
        this.multiple_selection = rows;
      },
      // 删除多项数据
      delete_multiple_data: function() {
        this.$confirm('删除后不可恢复，是否继续？', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          let is_error = false;
          for(let i = 0; i < this.multiple_selection.length; ++i) {
            this.$http.post(this.Global_Api + '/background/del_student', {
              user_name: this.user_name,
              user_token: this.user_token,
              student_number: this.multiple_selection[i].student_number
            }).then(response => {
              if(response.body.error_code !== 0) {
                is_error = true;
              }
              if(i === this.multiple_selection.length - 1) {
                if(is_error) {
                  this.$message.error('删除时出现错误！');
                }
                else {
                  this.$message.success('删除成功！');
                  this.get_data();
                }
              }
            }).catch(error => {
              console.log(error);
            });
          }
        }).catch(() => {
          this.$message.info('操作已取消！');
        });
      },
      // 改变页面大小
      change_page_size(size) {
        this.page_size = size;
        this.get_data();
      },
      // 换页
      change_page(page) {
        this.current_page = page;
        this.get_data();
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
