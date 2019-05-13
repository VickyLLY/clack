from django.urls import path
from selecourse import views

urlpatterns = [
    path(r'student_inquiry',views.student_inquiry,name="student_inquiry"),
    path(r'teacher_inquiry',views.teacher_inquiry,name="teacher_inquiry"),
    path(r'sele_button',views.sele_button,name="sele_button"),
    path(r'dele_button',views.dele_button,name="dele_button"),
    path(r'teacher_download',views.teacher_download,name="teacher_download"),
    path(r'admin_reports',views.admin_reports,name="admin_reports"),
    path(r'course_inquiry',views.course_inquiry,name="course_inquiry"),
    path(r'set_year_semester',views.set_year_semester,name="set_year_semester"),
    path(r'inquiry_year_semester',views.inquiry_year_semester,name="inquiry_year_semester"),
]