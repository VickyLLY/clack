from django.contrib import admin
from django.urls import path, include
from schedule import views

urlpatterns = [
    path(r'new_course', views.new_course, name='new_course'),
    path(r'course_list', views.course_list, name='course_list'),
    path(r'classroom_list', views.classroom_list, name='classroom_list')
]
