<template>
  <div>
    <PC_bar></PC_bar>
    <!--主界面-->
    <el-container>
      <el-header>
        <h1>编辑学院信息</h1>
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
              <el-table-column prop="department_id" label="学院ID" sortable>
              </el-table-column>
              <el-table-column prop="department_name" label="学院名称" sortable>
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
        <el-form-item label="学院名称" prop="department_name">
          <el-input type="text" v-model="add_form.department_name" auto-complete="off">
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
        <el-form-item label="学院名称" prop="department_name">
          <el-input type="text" v-model="edit_form.department_name"></el-input>
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
    name: 'edit_department',
    components: {
      PC_bar
    },
    // 组件渲染完成后，获取数据
    mounted: function() {
      this.get_data();
    },
    data() {
      return {
        // 用户数据
        user_name: this.$cookie.get('username'),
        user_token: this.$cookie.get('user_token'),
        // 窗口显示标志
        add_dialog: false,
        edit_dialog: false,
        // 添加窗口数据
        add_form: {
          department_name: ''
        },
        // 编辑窗口数据
        edit_form: {
          department_id: '',
          department_name: ''
        },
        // 数据输入规则
        data_rules: {
          department_name: [
            { required: true, message: '请输入教室名称', tigger: 'blur' },
            { min: 3, max: 15, message: '长度在3到15个字符', tigger: 'blur' }
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
        this.$refs['add_form'].validate((valid) => {
          if(valid) {
            this.$http.post(this.Global_Api + '/background/add_department', {
              user_name: this.user_name,
              user_token: this.user_token,
              department: {
                department_name: this.add_form.department_name
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
            }).catch(err => {
              console.log(err);
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
        this.$http.post(this.Global_Api + '/background/department_list', {}).then(response => {
          let start = (this.current_page - 1)*this.page_size;
          let end  = start + this.page_size;
          if(end > response.data.department_list.length) {
            end = response.data.department_list.length;
          }
          this.data_list = response.data.department_list.slice(start, end);
          this.total = response.data.department_list.length;
        }).catch(error => {
          console.log(error);
        })
      },
      // 设置编辑窗口数据
      set_data: function(row) {
        this.edit_dialog = true;
        this.edit_form.department_id = row.department_id;
        this.edit_form.department_name = row.department_name;
      },
      // 提交编辑窗口数据
      edit_submit: function() {
        this.$refs['edit_form'].validate((valid) => {
          if(valid) {
            this.$http.post(this.Global_Api + '/background/edit_department', {
              user_name: this.user_name,
              user_token: this.user_token,
              department_id: parseInt(this.edit_form.department_id),
              department_name: this.edit_form.department_name
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
          this.$http.post(this.Global_Api + '/background/del_department', {
            user_name: this.user_name,
            user_token: this.user_token,
            department_id: row.department_id
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
      get_multiple_selection: function (rows) {
        this.multiple_selection = rows;
      },
      // 删除多项数据
      delete_multiple_data: function() {
        this.$confirm('删除后不可恢复，是否继续？', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          console.info(this.multiple_selection);
          let is_error = false;
          for(let i = 0; i < this.multiple_selection.length; ++i) {
            this.$http.post(this.Global_Api + '/background/del_department', {
              user_name: this.user_name,
              user_token: this.user_token,
              department_id: this.multiple_selection[i].department_id
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
