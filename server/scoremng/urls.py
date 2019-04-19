from django.urls import path
from scoremng import views

urlpatterns = [
    path('teacher_upload', views.teacher_upload, name='teacher_upload'),
    path('student_scores/<int:student_number>', views.student_scores, name='student_scores'),
]