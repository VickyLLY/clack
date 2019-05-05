from django.db import models
from entity.models import Student,Teacher, DissertationTopic
# Create your models here.

class Application(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)

    def to_dict(self):
        return {
            "student_id": self.student,
            "dissertation_id": self.dissertation,
        }


class Determination(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)

    def to_dict(self):
        return {
            "student_id": self.student,
            "dissertation_id": self.dissertation,
        }


class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation_grade = models.IntegerField(default=0)

    def to_dict(self):
        return {
            "student_id": self.student,
            "dissertation_grade": self.dissertation_grade,
        }


class File(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation_file = models.FileField()

    def to_dict(self):
        return {
            "student_id": self.student,
            "dissertation_file": self.dissertation_file,
        }


class Review(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    dissertation = models.ForeignKey(DissertationTopic,on_delete=models.CASCADE)
    review_content = models.TextField()

    def to_dict(self):
        return {
            "teacher_id": self.teacher,
            "student_id": self.student,
            "dissertation_id": self.dissertation,
            "review_content": self.review_content
        }