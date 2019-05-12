# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from server import error_code
import json
import jsonschema
from entity.models import Student, Classroom, Teacher, Major, Banji, Department
import background.models
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
        notices = background.models.Notice.objects.filter(notice_receiver=aim_id)
        all_notice = background.models.Notice.objects.filter(notice_receiver=3)
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

# 添加学生
@admin_required
def add_student(request):
    request_json = json.loads(request.body)
    student = Student(student_name=request_json['student']['student_name'],
                                    student_number=request_json['student']['student_number'],
                                    student_banji_id=request_json['student']['student_banji_id'],
                                    student_email=request_json['student']['student_email'],
                                    student_start_year=request_json['student']['student_start_year'],
                                    student_end_year=request_json['student']['student_end_year'],
                                    )
    try:
        student.save()
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
    teacher = Teacher(teacher_name=request_json['teacher']['teacher_name'],
                      teacher_number=request_json['teacher']['teacher_number'],
                      teacher_email=request_json['teacher']['teacher_email'],
                      teacher_department_id=request_json['teacher']['teacher_department_id'],
                      )
    try:
        teacher.save()
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
        Major.objects.get(major_name=aim_id).delete()
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
    # new_department_id = request_json['banji_department_id']
    # new_major_id = request_json['banji_major_id']
    aim_id = request_json['department_id']

    if Department.objects.filter(id=aim_id).exists() == False:
        return JsonResponse({**error_code.CLACK_NOT_EXISTS})
    try:
        Department.objects.filter(id=aim_id).update(department_name=new_name)
        # Banji.objects.filter(id=aim_id).update(banji_major_department_id=new_department_id)
        # Banji.objects.filter(id=aim_id).update(banji_major_id=new_major_id)

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