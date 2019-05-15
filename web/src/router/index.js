import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/public/login'  //登录
import Register from '@/components/public/register' //注册
import Main from '@/components/public/main' //PC端主页
import NewsDetail from '@/components/background/news_detail'//通知详情
import edit_classroom from '@/components/background/edit_classroom'
import edit_major from '@/components/background/edit_major'
import edit_student from '@/components/background/edit_student'
import edit_department from '@/components/background/edit_department'
import edit_class from '@/components/background/edit_class'
import edit_teacher from '@/components/background/edit_teacher'
import Add_course from '@/components/schedule/add_course'
import Arrange_course from '@/components/schedule/arrange_course'
import VueCookie from 'vue-cookie'
import test from '@/components/mob/test'
import bar_mob from '@/components/mob/bar_mob'
import stu_sel_course_mob from '@/components/mob/stu_sel_course_mob'
import tea_sel_course_mob from '@/components/mob/tea_sel_course_mob'
import main_mob from "@/components/mob/main_mob";
import schedule_mob from "@/components/mob/schedule_mob";
import schedule_mob_tea from "@/components/mob/schedule_mob_tea";
import man_sel_course from "@/components/select_course/man_sel_course";
import tea_sel_course from "@/components/select_course/tea_sel_course";
import stu_sel_course from "@/components/select_course/stu_sel_course";
import stu_timetable from "@/components/select_course/stu_timetable";
import course_table from "@/components/schedule/course_table";
import add_notice from "@/components/background/add_notice";
import teacher_course_table from "@/components/schedule/teacher_course_table";
import add_semester from "@/components/schedule/add_semester";

//成绩管理
import Stu_navigation from '@/components/scoremng/stu_scoremng/Stu_navigation'
import navigation from '@/components/scoremng/navigation'
import Stu_score from '@/components/scoremng/stu_scoremng/stu_score'
import Stu_evaluation from '@/components/scoremng/stu_scoremng/stu_evaluation'
import Tea_upload from '@/components/scoremng/tea_scoremng/teacher_upload'
import Tea_query from '@/components/scoremng/tea_scoremng/teacher_query'
import man_view_msg from "@/components/select_course/man_view_msg";
import attention from "@/components/select_course/attention";

Vue.use(VueCookie)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path: '/test',
      component: test,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/main_mob',
      name: 'main_mob',
      component: main_mob,
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/main/edit_classroom',
      name: 'edit_classroom',
      component: edit_classroom,
    },
    {
      path: '/main/edit_major',
      name: 'edit_major',
      component: edit_major,
    },
    {
      path: '/main/edit_teacher',
      name: 'edit_teacher',
      component: edit_teacher,
    },
    {
      path: '/main/edit_student',
      name: 'edit_student',
      component: edit_student,
    },
    {
      path: '/main/edit_class',
      name: 'edit_class',
      component: edit_class,
    },
    {
      path: '/main/edit_department',
      name: 'edit_department',
      component: edit_department,
    },
    {
      path: '/schedule_mob',
      component: schedule_mob,
    },
    {
      path: '/schedule_mob_tea',
      component: schedule_mob_tea,
    },
    {
      path: '/main/add_course',
      name: 'Add_course',
      component: Add_course,
    },
    {
      path: '/main/arrange_semester',
      name: 'Arrange_course',
      component: Arrange_course
    },
    {
      path: '/main/stu_course_table',
      name: 'course_table',
      component: course_table
    },
    {
      path: '/main/tea_course_table',
      name: 'tea_course_table',
      component: teacher_course_table
    },
    {
      path: '/main/stu_sel_course',
      name: 'stu_sel_course',
      component: stu_sel_course
    },
    {
      path: '/main/tea_sel_course',
      name: 'tea_sel_course',
      component: tea_sel_course
    },
    {
      path: '/main/man_sel_course',
      name: 'man_sel_course',
      component: man_sel_course
    },
    {
      path: '/main/man_sel_course/man_view_msg',
      name: 'man_view_msg',
      component: man_view_msg
    },
    {
      path: '/main/stu_sel_course/stu_timetable',
      name: 'stu_timetable',
      component: stu_timetable
    },
    {
      path: '/main_mob/stu_sel_course_mob',
      name: 'stu_sel_course_mob',
      component: stu_sel_course_mob
    },
    {
      path: '/main_mob/tea_sel_course_mob',
      name: 'tea_sel_course_mob',
      component: tea_sel_course_mob
    },
    //成绩管理
    {
      path:'/main/navigation',
      name:'navigation',
      component:navigation,
      children: [
        {
          path:'stu_score',
          name:'stu_score',
          component:Stu_score
        },
        {
          path:'stu_evaluation',
          name:'stu_evaluation',
          component:Stu_evaluation
        },
        {
          path:'tea_upload',
          name:'Tea_upload',
          component:Tea_upload
        },
        {
          path:'tea_query',
          name:'Tea_query',
          component:Tea_query
        }
      ]
    },
    {
      path:'/main/stu_sel_course/attention',
      name:'attention',
      component:attention
    },
    {
      path:'/main/background/add_notice',
      name:"add_notice",
      component:add_notice
    },
    {
      path:'/main/news_detail/:id',
      component:NewsDetail,
    },
    {
      path:'/main/add_semester',
      name:"add_semester",
      component:add_semester
    }
  ],
  mode: 'history' // 去除地址栏中的/#
})
