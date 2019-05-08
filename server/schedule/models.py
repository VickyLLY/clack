from django.db import models
import entity.models


# Create your models here.
# TODO MockStudentCourse暂时用来测试课表功能, 选课功能完成后应该换到选课的数据
class MockStudentCourse(models.Model):
    student = models.ForeignKey(entity.models.Student, on_delete=models.CASCADE)
    course = models.ForeignKey(entity.models.Course, on_delete=models.CASCADE)
