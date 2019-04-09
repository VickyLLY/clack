from django.urls import path
from user import views

urlpatterns = [
    path(r'login', views.login, name="login"),
    path(r'logout', views.logout, name="logout"),
    path(r'signup_student', views.signup_student, name="signup_student"),
    path(r'signup_teacher', views.signup_teacher, name="signup_teacher"),
    path(r'signup_admin', views.signup_admin, name="signup_admin"),

    path(r'login_status', views.login_status, name="login_status")
]
