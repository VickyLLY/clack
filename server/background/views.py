# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from server import error_code
import json
import jsonschema
from entity.models import Student, Classroom, Teacher, Major, Banji, Department, DissertationTopic,User
import background.models
import dst.models
from django.db.models import Max
from background.models import AssignGroup, TeacherGroup
from server.decorators import admin_required, login_required, check_json, post_required
from entity.views import major_list
from entity.views import department_list
from entity.views import banji_list
# from entity.views import classroom_list
from server import schema
from django.db import transaction
from entity.views import new_banji
from entity.views import new_department
from entity.views import new_classroom
import hashlib
import scoremng
from scoremng.models import Course


# 发布通知
@admin_required
def add_notice(request):
    request_json = json.loads(request.body)
    notice = background.models.Notice(notice_title=request_json['notice']['notice_title'],
                                      notice_author=request_json['notice']['notice_author'],
                                      notice_date=request_json['notice']['notice_date'],
                                      notice_content=request_json['notice']['notice_content'],
                                      notice_receiver=request_json['notice']['notice_receiver'],
                                      )
    try:
        notice.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 通知列表
def notice_list(request):
    request_json = json.loads(request.body)
    aim_id = request_json['notice_receiver']
    try:
        if aim_id > 3:
            notices = background.models.Notice.objects.all()
        else:
            notices = background.models.Notice.objects.filter(notice_receiver=aim_id)
        result = [notice.to_dict() for notice in notices]
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS, "notice_list": result})

# 学生通知
def notice_list_student(request):
    try:
        notices = background.models.Notice.objects.filter(notice_receiver__in=[2, 3])

        result = [notice.to_dict() for notice in notices]
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS, "notice_list": result})

# 教师通知
def notice_list_teacher(request):
    try:
        # notices = background.models.Notice.objects.filter(notice_receiver=1)
        notices = background.models.Notice.objects.filter(notice_receiver__in=[1, 3])
        result = [notice.to_dict() for notice in notices]
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS, "notice_list": result})

# 通知具体内容
def notice_content(request):
    request_json = json.loads(request.body)
    aim_id = request_json['notice_id']
    result = background.models.Notice.objects.filter(id=aim_id)
    if result.exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        content = [{
            'notice_title': notice.notice_title,
            'notice_date': notice.notice_date,
            'notice_concent': notice.notice_content
        } for notice in result]
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS, "notice_concent": content})


def encode_password(password: str):
    return hashlib.sha256(password.encode("utf8")).hexdigest()


# 添加学生
@admin_required
def add_student(request):
    request_json = json.loads(request.body)
    try:
        student = Student(student_name=request_json['student']['student_name'],
                          student_number=request_json['student']['student_number'],
                          student_banji_id=request_json['student']['student_banji_id'],
                          student_email=request_json['student']['student_email'],
                          student_start_year=request_json['student']['student_start_year'],
                          student_end_year=request_json['student']['student_end_year'],
                          )
        student.save()
        student_user = User(user_name=request_json['student']['student_number'],
                            user_password=encode_password(request_json['student']['student_number'],),
                            user_type=2,
                            user_student_id=student.id)
        student_user.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# 学生列表
def student_list(request):
    students = Student.objects.all()
    result = [student.to_dict() for student in students]
    return JsonResponse({**error_code.CLACK_SUCCESS, "student_list": result})


# 删除学生
@admin_required
def del_student(request):
    request_json = json.loads(request.body)
    aim_id = request_json['student_number']
    try:
        Student.objects.get(student_number=aim_id).delete()
        User.objects.get(user_name=aim_id).delete()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 修改学生
@admin_required
def edit_student(request):
    request_json = json.loads(request.body)

    new_name = request_json['student_name']
    new_banji_id = request_json['student_banji_id']
    new_email = request_json['student_email']
    new_start_year = request_json['student_start_year']
    new_end_year = request_json['student_end_year']
    aim_id = request_json['student_number']
    if Student.objects.filter(student_number=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Student.objects.filter(student_number=aim_id).update(student_name=new_name)
        Student.objects.filter(student_number=aim_id).update(student_banji_id=new_banji_id)
        Student.objects.filter(student_number=aim_id).update(student_email=new_email)
        Student.objects.filter(student_number=aim_id).update(student_start_year=new_start_year)
        Student.objects.filter(student_number=aim_id).update(student_end_year=new_end_year)
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 添加教师
@admin_required
def add_teacher(request):
    request_json = json.loads(request.body)
    try:
        teacher = Teacher(teacher_name=request_json['teacher']['teacher_name'],
                          teacher_number=request_json['teacher']['teacher_number'],
                          teacher_email=request_json['teacher']['teacher_email'],
                          teacher_department_id=request_json['teacher']['teacher_department_id'],
                          )
        teacher.save()
        teacher_user = User(user_name=request_json['teacher']['teacher_number'],
                            user_password=encode_password(request_json['teacher']['teacher_number'],),
                            user_type=1,
                            user_teacher_id=teacher.id)
        teacher_user.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# 教师列表
def teacher_list(request):
    teachers = Teacher.objects.all()
    result = [teacher.to_dict() for teacher in teachers]
    return JsonResponse({**error_code.CLACK_SUCCESS, "teacher_list": result})

# 删除教师
@admin_required
def del_teacher(request):
    request_json = json.loads(request.body)
    aim_id = request_json['teacher_number']
    try:
        Teacher.objects.get(teacher_number=aim_id).delete()
        User.objects.get(user_name=aim_id).delete()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 修改教师
@admin_required
def edit_teacher(request):
    request_json = json.loads(request.body)

    new_name = request_json['teacher_name']
    new_department_id = request_json['teacher_department_id']
    new_email = request_json['teacher_email']
    aim_id = request_json['teacher_number']
    if Teacher.objects.filter(teacher_number=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Teacher.objects.filter(teacher_number=aim_id).update(teacher_name=new_name)
        Teacher.objects.filter(teacher_number=aim_id).update(teacher_department_id=new_department_id)
        Teacher.objects.filter(teacher_number=aim_id).update(teacher_email=new_email)
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 添加专业
@admin_required
def add_major(request):
    request_json = json.loads(request.body)
    major = Major(major_name=request_json['major']['major_name'],
                  major_department_id=request_json['major']['major_department_id'],
                  )
    try:
        major.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# 删除专业
@admin_required
def del_major(request):
    request_json = json.loads(request.body)
    aim_id = request_json['major_id']
    try:
        Major.objects.get(id=aim_id).delete()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})
# 修改专业
@admin_required
def edit_major(request):
    request_json = json.loads(request.body)
    aim_id = request_json['major_id']
    new_name = request_json['major_name']
    new_department_id = request_json['major_department_id']

    if Major.objects.filter(id=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Major.objects.filter(id=aim_id).update(major_name=new_name)
        Major.objects.filter(id=aim_id).update(major_department_id=new_department_id)
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})
# 添加学院
@admin_required
def add_department(request):
    return new_department(request)


# 添加班级
@admin_required
def add_banji(request):
    return new_banji(request)

# 添加教室
@admin_required
def add_classroom(request):
    return new_classroom(request)


# 教室列表
def classroom_list(request):
    classrooms = Classroom.objects.all()
    result_list = [{
        'classroom_id': classroom.id,
        'classroom_name': classroom.classroom_name,
        'classroom_capacity': classroom.classroom_capacity
    } for classroom in list(classrooms)]
    return JsonResponse({**error_code.CLACK_SUCCESS, "classroom_list": result_list})

# 删除教室
@admin_required
def del_classroom(request):
    request_json = json.loads(request.body)
    aim_id = request_json['classroom_id']
    try:
        Classroom.objects.get(id=aim_id).delete()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 修改教室
@admin_required
def edit_classroom(request):
    request_json = json.loads(request.body)

    new_name = request_json['classroom_name']
    new_capacity = request_json['classroom_capacity']
    aim_id = request_json['classroom_id']

    if Classroom.objects.filter(id=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Classroom.objects.filter(id=aim_id).update(classroom_name=new_name)
        Classroom.objects.filter(id=aim_id).update(classroom_capacity=new_capacity)
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 修改班级
@admin_required
def edit_banji(request):
    request_json = json.loads(request.body)

    new_name = request_json['banji_name']
    # new_department_id = request_json['banji_department_id']
    new_major_id = request_json['banji_major_id']
    aim_id = request_json['banji_id']

    if Banji.objects.filter(id=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Banji.objects.filter(id=aim_id).update(banji_name=new_name)
        # Banji.objects.filter(id=aim_id).update(banji_major_department_id=new_department_id)
        Banji.objects.filter(id=aim_id).update(banji_major_id=new_major_id)

    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 删除班级
@admin_required
def del_banji(request):
    request_json = json.loads(request.body)
    aim_id = request_json['banji_id']
    try:
        Banji.objects.get(id=aim_id).delete()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 添加学院
@admin_required
def edit_department(request):
    request_json = json.loads(request.body)

    new_name = request_json['department_name']
    aim_id = request_json['department_id']

    if Department.objects.filter(id=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Department.objects.filter(id=aim_id).update(department_name=new_name)

    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 删除学院
@admin_required
def del_department(request):
    request_json = json.loads(request.body)
    aim_id = request_json['department_id']
    try:
        Department.objects.get(id=aim_id).delete()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 学生查询答辩安排
@login_required
def design(request):
    request_json = json.loads(request.body)
    aim_id = request_json['student_number']

    try:
        teach = dst.models.Determination.objects.filter(student__student_number=aim_id)
        teacher_num = teach[0].dissertation.dissertation_tnum.teacher_number
        teacher_depart_id = teach[0].dissertation.dissertation_tnum.teacher_department_id

        group = TeacherGroup.objects.filter(group_teacher=teacher_num)
        group_num = group[0].group_number

        teachers = TeacherGroup.objects.filter(group_number=group_num,group_department_id=teacher_depart_id )
        tea_list = [{
            'teacher_number':t.group_teacher
        }for t in list(teachers)]

        result = AssignGroup.objects.filter(assign_number=group_num)
        schedule = [result[0].__str__()]

    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS,"result_list":schedule+tea_list})

#  老师按专业分组
def group_teacher(request):
    try:
        TeacherGroup.objects.all().delete()
        dis_list = DissertationTopic.objects.all()
        tea_list = [i.dissertation_tnum.teacher_number for i in list(dis_list)]
        note = {}
        count= {}
        for t_num in list(tea_list):
            teacher = Teacher.objects.filter(teacher_number=t_num)
            depart_id = teacher[0].teacher_department_id
            if depart_id not in note:
                note.update({depart_id: 0})
                count.update({depart_id: 0})
            else:
                count[depart_id] = count[depart_id] + 1
                note[depart_id] = count[depart_id] / 3

            if TeacherGroup.objects.filter(group_teacher=t_num).exists() == False:
                TeacherGroup.objects.create(group_teacher=t_num,
                                            group_department_id=depart_id,
                                            group_number=note[depart_id])

    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

#  规定每组时间地点
#  假设答辩期间所有课程已结束
def time_place(request):
    request_json = json.loads(request.body)
    aim_id = request_json['year']
    AssignGroup.objects.all().delete()
    try:
        group = TeacherGroup.objects.latest('group_number')
        group_num = group.group_number + 1
        class_num = Classroom.objects.count()
        year = aim_id
        for i in range(0, group_num):
            month = 6
            day = i/4+1
            s1 = "08:00"
            s2 = "10:00"
            s3 = "14:00"
            s4 = "16:00"
            if i % 4 == 1:
                AssignGroup.objects.create(assign_number=i,
                                           assign_time=s1,
                                           assign_year=year,
                                           assign_month=month,
                                           assign_day=day,
                                           assign_classroom_id=i % class_num+1)
            elif i % 4 == 2:
                AssignGroup.objects.create(assign_number=i,
                                           assign_time=s2,
                                           assign_year=year,
                                           assign_month=month,
                                           assign_day=day,
                                           assign_classroom_id=i % class_num+1)
            elif i % 4 == 3:
                AssignGroup.objects.create(assign_number=i,
                                           assign_time=s3,
                                           assign_year=year,
                                           assign_month=month,
                                           assign_day=day,
                                           assign_classroom_id=i % class_num+1)
            elif i % 4 == 0:
                AssignGroup.objects.create(assign_number=i,
                                           assign_time=s4,
                                           assign_year=year,
                                           assign_month=month,
                                           assign_day=day,
                                           assign_classroom_id=i % class_num+1)
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# 学位警告
def degree_warning(request):
    students = Student.objects.all()
    snum_list = [i.student_number for i in list(students)]
    students_list = []
    for i in snum_list:
        student_number = i
        try:
            student = Student.objects.get(student_number=student_number)
        except Exception:
            return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

        score_list = scoremng.models.Score.objects.filter(student_id=student.id)

        # 必修课需要获得的学分和已经获得了的学分 课程代码是0
        required_course_credit_gained_sum = 0
        required_course_credit_aim = 100

        # 选修课需要获得的学分和已经获得了的学分 课程代码是1
        optional_course_credit_gained_sum = 0
        optional_course_credit_aim = 50

        # 辅修课需要获得的学分和已经获得了的学分 课程代码是2
        minor_course_credit_gained_sum = 0
        minor_course_credit_aim = 20

        for score_item in score_list:
            course_id = score_item.course_id
            try:
                course = Course.objects.get(id=course_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
            if course.course_type == 0:  # 这门课是必修
                required_course_credit_gained_sum += course.course_credit
            elif course.course_type == 1:  # 这门课是选修
                optional_course_credit_gained_sum += course.course_credit
            elif course.course_type == 2:  # 这门课是辅修
                minor_course_credit_gained_sum += course.course_credit

        # 必修课
        required_course = {
                    'credit_type': 0,
                    'credit_gained_sum': required_course_credit_gained_sum,
                    'credit_aim': required_course_credit_aim,
        }
        # 选修课
        optional_course = {
                    'credit_type': 1,
                    'credit_gained_sum': optional_course_credit_gained_sum,
                    'credit_aim': optional_course_credit_aim,
                }
        # 辅修课
        minor_course = {
                    'credit_type': 2,
                    'credit_gained_sum': minor_course_credit_gained_sum,
                    'credit_aim': minor_course_credit_aim,
                }
        if required_course_credit_gained_sum<required_course_credit_aim or optional_course_credit_gained_sum<optional_course_credit_aim or minor_course_credit_gained_sum<minor_course_credit_aim:
            credits_list = {'student_number':student_number,
                        'required_course_credit_gained_sum': required_course_credit_gained_sum,
                        'required_course_credit_aim': required_course_credit_aim,
                       'optional_course_credit_gained_sum': optional_course_credit_gained_sum,
                       'optional_course_credit_aim': optional_course_credit_aim,
                       'minor_course_credit_gained_sum': minor_course_credit_gained_sum,
                       'minor_course_credit_aim': minor_course_credit_aim,
                       }
        # credits_list = [student, required_course, optional_course, minor_course]
        students_list.append(credits_list)
    return JsonResponse({**error_code.CLACK_SUCCESS, "students_list":students_list})
