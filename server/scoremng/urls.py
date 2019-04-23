from django.urls import path
from scoremng import views

urlpatterns = [
    path('teacher_upload/<str:teacher_number>/', views.teacher_upload, name='teacher_upload'),
    path('student_scores/<str:student_number>/', views.student_scores, name='student_scores'),
    path('courses_comment/<str:student_number>/', views.courses_comment, name='courses_comment'),
    path('student_download_scores/<str:student_number>/', views.student_download_scores, name='download_scores'),
    path('teacher_download_scores/<str:teacher_number>/', views.teacher_download_scores, name='teacher_download_scores'),
]