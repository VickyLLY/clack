from django.db import models
import datetime
from django.utils.timezone import make_aware

# 放飞自我
每节课开始时间 = {
    1: (datetime.timedelta(hours=8, minutes=0), datetime.timedelta(hours=8, minutes=45)),
    2: (datetime.timedelta(hours=8, minutes=50), datetime.timedelta(hours=9, minutes=35)),
    3: (datetime.timedelta(hours=9, minutes=50), datetime.timedelta(hours=10, minutes=35)),
    4: (datetime.timedelta(hours=10, minutes=45), datetime.timedelta(hours=11, minutes=30)),
    5: (datetime.timedelta(hours=11, minutes=35), datetime.timedelta(hours=12, minutes=20)),
    6: (datetime.timedelta(hours=13, minutes=0), datetime.timedelta(hours=13, minutes=45)),
    7: (datetime.timedelta(hours=13, minutes=50), datetime.timedelta(hours=14, minutes=35)),
    8: (datetime.timedelta(hours=14, minutes=45), datetime.timedelta(hours=15, minutes=30)),
    9: (datetime.timedelta(hours=15, minutes=40), datetime.timedelta(hours=16, minutes=25)),
    10: (datetime.timedelta(hours=16, minutes=30), datetime.timedelta(hours=17, minutes=15)),
    11: (datetime.timedelta(hours=18, minutes=0), datetime.timedelta(hours=18, minutes=45)),
    12: (datetime.timedelta(hours=18, minutes=50), datetime.timedelta(hours=19, minutes=35)),
    13: (datetime.timedelta(hours=19, minutes=40), datetime.timedelta(hours=20, minutes=25))
}


# 学院
class Department(models.Model):
    department_name = models.TextField(default='', unique=True)

    def to_dict(self):
        return {
            "department_id": self.id,
            "department_name": self.department_name
        }


# 专业
class Major(models.Model):
    major_name = models.TextField(default='', unique=True)
    major_department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)


# 教室
class Classroom(models.Model):
    classroom_name = models.TextField(default='', unique=True)
    classroom_capacity = models.IntegerField(default=30)

    def __str__(self):
        return "%s,%d" % (self.classroom_name, self.classroom_capacity)

    def to_dict(self):
        return {
            'classroom_id': self.id,
            'classroom_name': self.classroom_name,
            'classroom_capacity': self.classroom_capacity
        }


# 班级
class Banji(models.Model):
    banji_name = models.TextField(default='', unique=True)
    banji_major = models.ForeignKey(Major, on_delete=models.CASCADE, null=False)
    # banji_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)

class Teacher(models.Model):
    teacher_name = models.TextField(default="")
    teacher_number = models.TextField(default="", unique=True)
    teacher_email = models.EmailField(default="test@test.com")
    teacher_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)

    def to_dict(self):
        return {
            "teacher_name": self.teacher_name,
            "teacher_number": self.teacher_number,
            "teacher_email": self.teacher_email,
            "teacher_department_id": self.teacher_department_id
        }

# 课程
class Course(models.Model):
    course_name = models.TextField(default="")
    # 课程学分
    course_credit = models.IntegerField(default=1)
    # 课程类型
    course_type = models.IntegerField(default=0)

    # 课程所在学年开始年份
    course_year = models.IntegerField(default=2018)
    # 课程学期
    course_semester = models.IntegerField(default=2)
    # 课程容量
    course_capacity = models.IntegerField(default=150)
    # 任课老师
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    # 选课权限
    course_access = models.TextField(default="无")
    # 开课学院
    course_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # 课程余量
    course_allowance = models.IntegerField(default=150)

    def __str__(self):
        return self.course_name + "," + str(self.course_year) + "," + str(self.course_semester)

    def to_dict(self):
        return {
            "course_id": self.id,
            "course_name": self.course_name,
            "course_credit": self.course_credit,
            "course_type": self.course_type,
            "course_year": self.course_year,
            "course_semester": self.course_semester,
            "course_capacity": self.course_capacity,
            # "course_department_id": self.course_department_id
            "course_department": self.course_department.to_dict(),
            "date_and_classroom": [dc.to_dict() for dc in self.dateandclassroom_set.all()]
        }

# 考试
class Exam(models.Model):
    exam_name = models.TextField(default='')
    exam_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)


# 学生
class Student(models.Model):
    student_number = models.TextField(default='', unique=True)
    student_name = models.TextField(default='')
    student_banji = models.ForeignKey(Banji, null=False, on_delete=models.CASCADE)
    student_email = models.EmailField(default="test@test.com")
    # student_department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    # student_major = models.ForeignKey(Major, null=False, on_delete=models.CASCADE)
    student_start_year = models.IntegerField(default=2016)
    student_end_year = models.IntegerField(default=2020)

    def to_dict(self):
        return {
            "student_number": self.student_number,
            "student_name": self.student_name,
            "student_banji_id": self.student_banji_id,
            "student_email": self.student_email,
            # student_department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
            # student_major = models.ForeignKey(Major, null=False, on_delete=models.CASCADE)
            "student_start_year": self.student_start_year,
            "student_end_year": self.student_end_year
        }

#学生课程关系
class Student_course(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    # 选课权限
    course_access = models.TextField(default="无")

# 用户
class User(models.Model):
    user_name = models.TextField(default='', unique=True)
    user_password = models.TextField(default='')
    user_token = models.TextField(default='')
    user_type = models.IntegerField(default=2)
    user_student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    user_teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    user_permission = models.TextField(default='{}')


class Semester(models.Model):
    # 学年开始的年份
    year = models.IntegerField()
    # 第几学期
    semester = models.IntegerField()
    # 开学日期
    start_date = models.DateField()

    def __str__(self):
        return str(self.year) + "," + str(self.semester) + "," + str(self.start_date)


class DateAndClassroom(models.Model):
    # 时间地点的类型
    # type 0 代表课程的时间地点
    # type 1 代表考试的时间地点
    # type -1 代表被删除
    type = models.IntegerField(default=0)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)
    # type 0 开始 -----------------------
    # 对应课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    # 学年开始年份
    year = models.IntegerField(blank=True)
    # 所在学期 1 2 3
    semester = models.IntegerField(blank=True)
    # 开始周数
    start_week = models.IntegerField(blank=True)
    # 结束周数
    end_week = models.IntegerField(blank=True)
    # 星期几 1, 2, ... 6, 7
    day_of_week = models.IntegerField(blank=True)
    # 第几节开始 1,2 ...
    start = models.IntegerField(blank=True)
    # 第几节结束 1,2 ...
    end = models.IntegerField(blank=True)
    # type 0 结束 -----------------------

    # type 1 开始 -----------------------
    # 对应考试
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
    # 开始日期时间
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)

    # type 1 结束 -----------------------

    def to_date_time_list(self) -> list:
        result = list()
        if self.type == 0:
            try:
                var = Semester.objects.get(year=self.year, semester=self.semester)
            except:
                pass
            semester_start_date_time = datetime.datetime.strptime(var.start_date.strftime('%Y%m%d'), '%Y%m%d')
            for i in range(self.start_week, self.end_week + 1):
                delta_day = (i - 1) * 7 + self.day_of_week - 1
                start_date_time = semester_start_date_time + datetime.timedelta(days=delta_day) + 每节课开始时间[self.start][0]
                end_date_time = semester_start_date_time + datetime.timedelta(days=delta_day) + 每节课开始时间[self.end][1]
                result.append((start_date_time, end_date_time))
                # date_time =
        else:
            result.append((self.start_date_time.replace(tzinfo=None), self.end_date_time.replace(tzinfo=None)))
        print(result)
        return result

    def conflict(self, date_and_classroom) -> bool:
        # 如果时间有冲突将会返回True
        assert isinstance(date_and_classroom, DateAndClassroom)
        for i in self.to_date_time_list():
            for j in date_and_classroom.to_date_time_list():
                if not (i[0] >= j[1] or i[1] <= j[0]):
                    return True
        return False

    def save(self, *args, **kwargs):
        if self.type == -1:
            # 被删除
            super(DateAndClassroom, self).save(*args, **kwargs)
            return
        # TODO 判断节次不能大于13
        Semester.objects.get(year=self.year, semester=self.semester)
        if self.type == 0:
            if self.start_week > self.end_week:
                raise Exception("开始周大于结束周")
            if self.start > self.end:
                raise Exception("开始节次大于结束节次")
            if self.start < 1 or self.end > 13:
                raise Exception("开始结束应在1到13范围内")
            if self.course.course_capacity > self.classroom.classroom_capacity:
                raise Exception("教室容量小于课程容量")
            if self.day_of_week < 1 or self.day_of_week > 7:
                raise Exception("day_of_week wrong")
        elif self.type == 1:
            self.start_date_time = make_aware(self.start_date_time)
            self.end_date_time = make_aware(self.end_date_time)
            if self.start_date_time > self.end_date_time:
                raise Exception("开始时间大于结束时间")
            if self.classroom.classroom_capacity < self.exam.exam_course.course_capacity:
                pass
                # TODO 一个课程多个考试教室
                # raise Exception("教室容量小于考试对应课程容量")
        # 存储时判断同一教室是否存在时间冲突
        for DAC in DateAndClassroom.objects.filter(classroom_id=self.classroom_id):
            if DAC.id != self.id and self.conflict(DAC):
                raise Exception('当前时间教室内存在其它事件')

        super(DateAndClassroom, self).save(*args, **kwargs)

    def check_is_valid(self):
        for DAC in DateAndClassroom.objects.filter(classroom_id=self.classroom_id):
            if self.conflict(DAC):
                return False
        return True

    def get_free_classroom(self):
        result = list()
        for classroom in Classroom.objects.all():
            flag = True
            for DC in classroom.dateandclassroom_set.all():
                if DC.id != self.id and self.conflict(DC):
                    flag = False
                    break
            if flag:
                result.append(classroom)
        return result

    def to_dict(self):
        if self.type == 0:
            return {
                "id": self.id,
                "classroom": self.classroom.to_dict(),
                "year": self.year,
                "semester": self.semester,
                "start_week": self.start_week,
                "end_week": self.end_week,
                "day_of_week": self.day_of_week,
                "start": self.start,
                "end": self.end
            }
