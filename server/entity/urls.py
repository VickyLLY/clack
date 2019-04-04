from django.urls import path
from entity import views

urlpatterns = [
    path(r'classroom_list', views.classroom_list, name="classroom_list"),
    path(r'new_classroom', views.new_classroom, name="new_classroom"),
    path(r'new_course', views.new_course, name="new_course")

]
