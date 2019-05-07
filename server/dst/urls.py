from django.urls import path
from dst import views

urlpatterns = [
    path(r'view_detail', views.view_detail, name="view_detail"),
    path(r'new_dst', views.new_dst, name="new_dst"),
    path(r'stu_select',views.stu_select,name='stu_select'),
    path(r'dst_list', views.dst_list, name='dst_list'),
    path(r'dst_list_approval', views.dst_list_approval, name='dst_list_approval'),
    path(r'teacher_dst_list', views.teacher_dst_list, name='teacher_dst_list'),
    path(r'stu_dst_list', views.stu_dst_list, name='stu_dst_list'),
]
