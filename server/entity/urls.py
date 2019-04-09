from django.urls import path
from entity import views

urlpatterns = [
    path(r'classroom_list', views.classroom_list, name="classroom_list"),
    path(r'new_classroom', views.new_classroom, name="new_classroom"),
    path(r'new_course', views.new_course, name="new_course"),
    path(r'new_department', views.new_department, name="new_department"),
    path(r'department_list', views.department_list, name="department_list"),
    path(r'new_major', views.new_major, name="new_major"),
    path(r'major_list', views.major_list, name="major_list"),
    path(r'new_banji', views.new_banji, name="new_banji"),
    path(r'banji_list', views.banji_list, name="banji_list")
]
