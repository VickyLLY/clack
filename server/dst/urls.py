from django.urls import path
from dst import views

urlpatterns = [
    path(r'new_dst', views.new_dst, name="new_dst"),
    path(r'stu_select',views.stu_select,name='stu_select'),
    path(r'dst_list', views.dst_list, name='dst_list'),
    path(r'dst_list_approval', views.dst_list_approval, name='dst_list_approval'),
    path(r'teacher_dst_list', views.teacher_dst_list, name='teacher_dst_list'),
    path(r'stu_dst_list', views.stu_dst_list, name='stu_dst_list'),
    path(r'stu_view_dst', views.stu_view_dst, name='stu_view_dst'),
    path(r'view_published_dissertation', views.view_published_dissertation, name='view_published_dissertation'),
    path(r'view_detail', views.view_detail, name='view_detail'),
    path(r'change_dst', views.change_dst, name='change_dst'),
    path(r'view_selected', views.view_selected, name='view_selected'),
    path(r'view_student', views.view_student, name='view_student'),
    path(r'upload_score', views.upload_score, name='upload_score'),
    path(r'download', views.download, name='download'),
    path(r'define_stu', views.define_stu, name='define_stu'),
    path(r'everyyear_dst', views.everyyear_dst, name='everyyear_dst'),
    path(r'select_dst_teacher_name', views.select_dst_teacher_name, name="select_dst_teacher_name"),
    path(r'select_dst_dst_title', views.select_dst_dst_title, name="select_dst_dst_title"),
    path(r'upload_file', views.upload_file, name="upload_file"),
    path(r'dst_approval', views.dst_approval, name="dst_approval"),
    path(r'stu_view_grade', views.stu_view_grade, name="stu_view_grade"),

]
