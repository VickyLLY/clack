from django.urls import path
from scoremng import views

urlpatterns = [
    path(r'teacher/upload',views.teacher_upload, name='teacher_upload'),
]