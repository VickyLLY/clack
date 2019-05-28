from django.db import models
from entity.models import Student,Teacher, DissertationTopic
# Create your models here.

class Application(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)


class Determination(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)


# 学生成绩及评语
class Grade(models.Model):
    grade_dissertation = models.ForeignKey(DissertationTopic, on_delete=models.CASCADE,default="")
    grade_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade_grade = models.IntegerField(default=0)
    grade_comment = models.TextField(default="")

class DissertationFile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    dissertation_file_path = models.FileField(upload_to=None)

class Flag(models.Model):
    flag = models.IntegerField(default=-1)

