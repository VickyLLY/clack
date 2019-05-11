from django.db import models
from entity.models import Student,Teacher, DissertationTopic
# Create your models here.

class Application(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)


class Determination(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)


class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation_grade = models.IntegerField(default=0)

class File(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation_file = models.FileField()

class Review(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)
    review_content = models.TextField()