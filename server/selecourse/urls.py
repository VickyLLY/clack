from django.urls import path
from selecourse import views

urlpatterns = [
    path(r'student_sele', views.student_sele, name="student_sele"),
    path(r'student_inquiry', views.student_inquiry, name="student_inquiry"),
    path(r'teacher_inquiry', views.teacher_inquiry, name="teacher_inquiry"),
]
