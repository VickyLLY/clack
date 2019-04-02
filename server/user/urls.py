from django.urls import path
from user import views

urlpatterns = [
    path(r'login', views.login, name="login"),
    path(r'logout', views.logout, name="logout"),
    path(r'signup', views.signup, name="signup"),
    path(r'test_status', views.test_status, name="test_status")
]
