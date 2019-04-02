from django.db import models


class User(models.Model):
    user_name = models.TextField(default='', unique=True)
    user_password = models.TextField(default='')
    user_token = models.TextField(default='')
    user_type = models.IntegerField(default=2)
    # user_student
    # user_teacher
    user_permission = models.TextField(default='{}')