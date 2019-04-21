from django.urls import path
from scoremng import views

urlpatterns = [
    path('teacher_upload/', views.teacher_upload, name='teacher_upload'),
    path('student_scores/<str:student_number>/', views.student_scores, name='student_scores'),
    path('courses_comment/<str:student_number>/', views.courses_comment, name='courses_comment'),
]