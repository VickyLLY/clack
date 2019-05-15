from django.db import models
from entity.models import Student
from entity.models import Course
from entity.models import Teacher


# 成绩
class Score(models.Model):
    # 在数据库中体现为 student_id, 学生的id是Django自动生成的，并不是学生的学号
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    # 在数据库中体现为 course_id, 课程的id是Django自动生成的，并不是课程号
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    score = models.IntegerField(default=0, null=False)
    comment = models.TextField(default='', null=True)

    class Meta:
        unique_together = ('student', 'course')

