from django.db import models
from entity.models import Department, Student, Teacher, Classroom, DissertationTopic



# 通告
class Notice(models.Model):
    notice_title = models.TextField(default='', unique=True)
    notice_author = models.IntegerField(default='')
    notice_date = models.DateTimeField(default='')
    notice_receiver = models.IntegerField(default='')
    notice_content = models.TextField(default='')

    def to_dict(self):
        return {
            "notice_title": self.notice_title,
            "notice_author": self.notice_author,
            "notice_date": self.notice_date,
            "notice_id": self.id,
            "notice_content": self.notice_content,
            'notice_receiver':self.notice_receiver,
        }


# 教师分组
class TeacherGroup(models.Model):
    group_teacher = models.TextField(default='',unique=True)
    group_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    group_number = models.IntegerField(default=0)


# 组内时间地点安排
class AssignGroup(models.Model):
    assign_number = models.IntegerField(default=0,unique=True)
    assign_year = models.IntegerField(default=2016)
    assign_month = models.IntegerField(default=12)
    assign_day = models.IntegerField(default=12)
    assign_time = models.TimeField(default='')
    # assign_date = models.DateTimeField(default='')
    assign_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return {
            "assign_date": str(self.assign_year)+"-"+str(self.assign_month)+"-"+str(self.assign_day)
                           +" "+str(self.assign_time),
            "assign_classroom_id": self.assign_classroom_id
        }



