from django.contrib import admin
from django.urls import path, include
from schedule import views

urlpatterns = [
    path(r'new_course', views.new_course, name='new_course'),
    path(r'course_list', views.course_list, name='course_list'),
    path(r'classroom_list', views.classroom_list, name='classroom_list'),
    path(r'change_course_name', views.change_course_name, name='change_course_name'),
    path(r'change_course_credit', views.change_course_credit, name='change_course_credit'),
    path(r'change_course_type', views.change_course_type, name='change_course_type'),
    path(r'change_course_semester', views.change_course_semester, name='change_course_semester'),
    path(r'change_course_capacity', views.change_course_capacity, name='change_course_capacity'),
    path(r'change_course_department', views.change_course_department, name='change_course_department'),
    path(r'course_add_dc', views.course_add_dc, name='course_add_dc'),
    path(r'mock_xuanke', views.mock_xuanke, name='mock_xuanke'),
    path(r'student_course_list', views.student_course_list, name='student_course_list'),
    path(r'del_dc', views.del_dc, name='del_dc'),
    path(r'course_info', views.course_info, name='course_info'),
    path(r'teacher_list', views.teacher_list, name='teacher_list'),
    path(r'course_add_teacher', views.course_add_teacher, name='course_add_teacher')
]
