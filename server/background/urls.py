from django.urls import path
from background import views

urlpatterns = [
    path(r'add_notice', views.add_notice, name='add_notice'),
    path(r'notice_list', views.notice_list, name='notice_list'),
    path(r'add_student', views.add_student, name='add_student'),
    path(r'student_list', views.student_list, name='student_list'),
    path(r'add_teacher', views.add_teacher, name='add_teacher'),
    path(r'teacher_list', views.teacher_list, name='teacher_list'),
    path(r'add_major', views.add_major, name='add_major'),
    path(r'major_list', views.major_list, name='major_list'),
    path(r'del_student', views.del_student, name='del_student'),
    path(r'del_teacher', views.del_teacher, name='del_teacher'),
    path(r'del_major', views.del_major, name='del_major'),
    path(r'add_department', views.add_department, name='add_department'),
    path(r'add_banji', views.add_banji, name='add_banji'),
    path(r'department_list', views.department_list, name='department_list'),
    path(r'banji_list', views.banji_list, name='banji_list'),
    path(r'classroom_list', views.classroom_list, name='classroom_list'),
    path(r'add_classroom', views.add_classroom, name='add_classroom'),
    path(r'del_classroom', views.del_classroom, name='del_classroom'),
    path(r'edit_classroom', views.edit_classroom, name='edit_classroom'),
    path(r'edit_student', views.edit_student, name='edit_student'),
    path(r'edit_teacher', views.edit_teacher, name='edit_teacher'),
    path(r'edit_major', views.edit_major, name='edit_major'),

]
