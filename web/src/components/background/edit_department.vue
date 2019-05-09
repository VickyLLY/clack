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
              <el-button size="mini" type="danger" icon="el-icon-delete" @click="delete_multiple_data()">删除</el-button>
            </div>
          </el-col>
        </el-row>
        <!--数据展示列表-->
        <el-row>
          <el-col :span="24">
            <el-table :data="data_list" tooltip-effect="dark" style="width:100%" :default-sort="{prop:'create_time',order:'descending'}" @selection-change="get_multiple_selection()">
              <el-table-column type="selection" width="55">
              </el-table-column>
              <el-table-column prop="classroom_id" label="学院ID" sortable>
              </el-table-column>
              <el-table-column prop="classroom_name" label="学院名称" sortable>
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
              <el-pagination layout="prev,pager,next" :total="total" :page-size="5" @current-change="get_data">
              </el-pagination>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
    <!--添加信息窗口-->
    <el-dialog title="添加信息" :visible.sync="add_dialog" @close="reset_form('add_form')">
      <el-form :model="add_form" :rules="data_rules" ref="add_form" label-width="100px">
        <el-form-item label="学院名称" prop="classroom_name">
          <el-input type="text" v-model="add_form.classroom_name" auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="add_submit()">提交</el-button>
          <el-button @click="reset_form('add_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!--修改信息窗口-->
    <el-dialog title="修改" :visible.sync="edit_dialog" @close="reset_form('edit_form')">
      <el-form :model="edit_form" :rules="data_rules" ref="edit_form" label-width="100px">
        <el-form-item label="学院名称" prop="classroom_name">
          <el-input type="text" v-model="edit_form.classroom_name"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="edit_submit()">修改</el-button>
          <el-button @click="reset_form('edit_form')">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>


<script>
  import PC_bar from '../public/PC_bar';
  import axios from 'axios';

  export default {
    name: 'edit_classroom',
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
          classroom_name: ''
        },
        edit_form: {
          classroom_id: '',
          classroom_name: ''
        },
        add_dialog: false,
        edit_dialog: false,
        data_list: [],
        data_rules: {
          // 待修改
          classroom_name: [
            { required: true, message: '请输入教室名称', tigger: 'blur' },
            { min: 3, max: 15, message: '长度在3到15个字符', tigger: 'blur' }
          ],
          classroom_capacity: [
            { required: true, message: '请输入教室容量', tigger: 'blur' }
          ]
        },
        total: 0,
        multiple_selection: []
      }
    },
    methods: {
      // 提交添加窗口数据
      add_submit: function() {
        this.$refs['add_form'].validate((valid) => {
          if(valid) {
            this.$http.post(this.Global_Api + '/background/add_department', {
              'user_name': this.user_name,
              'user_token': this.user_token,
              'classroom': {
                'classroom_name': this.add_form.classroom_name,
                'classroom_capacity': parseInt(this.add_form.classroom_capacity)
              }
            }).then(response => {
              if(response.body.error_code === 0) {
                this.$message.success('添加成功');
                this.reset_form('add_form');
                this.get_data();
              }
              else {
                this.$message.error('错误：' + response.body.error_message);
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
      get_data: function(page) {
        // 待修改
        axios.post(this.Global_Api + '/background/classroom_list', {
          params: {
            page: page || 1,
            pageSize: 5
          }
        }).then(response => {
          this.data_list = response.data.classroom_list;
          this.total = response.data.classroom_list.count;
        }).catch(err => {
          console.log(err);
        })
      },
      // 设置编辑窗口数据
      set_data: function(row) {
        this.edit_dialog = true;
        this.edit_form.classroom_name = row.classroom_name;
        this.edit_form.classroom_capacity = row.classroom_capacity;
      },
      // 提交编辑窗口数据
      edit_submit: function() {
        // 待修改
        this.$refs['edit_form'].validate((valid) => {
          if(valid) {
            this.$http.post(this.Global_Api + '/background/edit_classroom', {
              'user_name': this.user_name,
              'user_token': this.user_token,
              'classroom': {
                'classroom_name': this.edit_form.classroom_name,
                'classroom_capacity': parseInt(this.edit_form.classroom_capacity)
              }
            }).then(response => {
              if(response.body.error_code === 0) {
                this.$message.success('添加成功');
                this.reset_form('edit_form');
                this.get_data();
              }
              else {
                this.$message.error('错误：' + response.body.error_message);
              }
            }).catch(err => {
              console.log(err);
            });
          }
        })
      },
      // 删除单项数据
      delete_single_data: function(row) {
        // 待修改
        this.$confirm('此操作将永久删除该项，是否继续?', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.post('/background/del_classroom', row).then(response => {
            if(response.body.error_code === 0) {
              this.$message.success('删除成功');
              this.get_data();
            }
            else {
              this.$message.error('错误：' + response.body.error_message);
            }
          })
        }).catch(() => {
          this.$message.info('操作已取消');
        });
      },
      // 获取多选项
      get_multiple_selection: function (rows) {
        this.multiple_selection = rows;
      },
      // 删除多项数据
      delete_multiple_data: function() {
        // 待修改
        this.$confirm('此操作将永久删除这些项，是否继续？', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.post('/background/del_classroom', this.multiple_selection).then(response => {
            if(response.body.error_code === 0) {
              this.$message.success('删除成功');
              this.get_data();
            }
            else {
              this.$message.error('错误：' + response.body.error_message);
            }
          })
        }).catch(() => {
          this.$message.info('操作已取消');
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
