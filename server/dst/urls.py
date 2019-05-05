from django.urls import path
from dst import views

urlpatterns = [
    path(r'view_detail', views.view_detail, name="view_detail"),
    path(r'new_dst', views.new_dst, name="new_dst"),
    path(r'stu_select',views.stu_select,name='stu_select'),

]
