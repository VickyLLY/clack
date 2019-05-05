from django.db import models
from entity.models import Student, Course
# Create your models here.


# 选课表
class Selection(models.Model):
    selection_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    selection_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)