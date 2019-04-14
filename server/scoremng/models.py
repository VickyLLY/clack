from django.db import models
from entity.models import Student
from entity.models import Course


# 成绩
class Score(models.Model):
    student_number = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    course_number = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    score = models.IntegerField(default=0, null=False)
