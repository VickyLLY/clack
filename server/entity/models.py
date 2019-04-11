from django.db import models


# 学院
class Department(models.Model):
    department_name = models.TextField(default='', unique=True)


# 专业
class Major(models.Model):
    major_name = models.TextField(default='', unique=True)
    major_department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)


# 教室
class Classroom(models.Model):
    classroom_name = models.TextField(default='', unique=True)
    classroom_capacity = models.IntegerField(default=30)


# 班级
class Banji(models.Model):
    banji_name = models.TextField(default='', unique=True)
    banji_major = models.ForeignKey(Major, on_delete=models.CASCADE, null=False)
    # banji_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)


# 课程
class Course(models.Model):
    course_name = models.TextField(default="")
    course_start = models.IntegerField(default=1)
    course_end = models.IntegerField(default=3)
    course_credit = models.IntegerField(default=1)
    course_type = models.IntegerField(default=0)
    course_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=False)
    course_year = models.IntegerField(default=2018)
    course_semester = models.IntegerField(default=2)


# 考试
class Exam(models.Model):
    exam_name = models.TextField(default='')
    exam_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    exam_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=False)
    exam_start_time = models.DateTimeField()
    exam_end_time = models.DateTimeField()


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


# 教师
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


# 用户
class User(models.Model):
    user_name = models.TextField(default='', unique=True)
    user_password = models.TextField(default='')
    user_token = models.TextField(default='')
    user_type = models.IntegerField(default=2)
    user_student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    user_teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    user_permission = models.TextField(default='{}')
