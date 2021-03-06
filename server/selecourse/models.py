from django.db import models
from entity.models import Student, Course
# Create your models here.

#选课表
class Selection(models.Model):
    #在数据库中分别对应为selection_student_id和selection_course_id,由Django自动生成
    selection_student=models.ForeignKey(Student,on_delete=models.CASCADE, null=False)
    selection_course=models.ForeignKey(Course,on_delete=models.CASCADE, null=False)

#表中永远只有一条记录
class Year_semester(models.Model):
    year=models.IntegerField(default=2016)
    semester=models.IntegerField(default=1)