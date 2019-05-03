from django.urls import path
from scoremng import views

urlpatterns = [
    path('teacher_upload/<str:teacher_number>/', views.teacher_upload, name='teacher_upload'),
    path('student_check_scores/', views.student_check_scores, name='student_check_scores'),
    path('courses_comment/', views.courses_comment, name='courses_comment'),
    path('student_download_scores/', views.student_download_scores, name='student_download_scores'),
    path('teacher_check_scores/<str:teacher_number>/', views.teacher_check_scores, name='teacher_check_scores'),
    path('admin_check/<str:admin_number>/', views.admin_check, name='admin_check'),
]