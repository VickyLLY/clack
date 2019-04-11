from django.shortcuts import render
from django.http import JsonResponse
from server.decorators import post_required, admin_required, login_required, check_json
from server import error_code
import entity.models
import json
import jsonschema
from server import schema
from django.db import transaction


@check_json(schema.entity_classroom_list)
def classroom_list(request):
    request_json = json.loads(request.body)
    classrooms = entity.models.Classroom.objects.all().order_by('classroom_capacity')
    if "capacity_range" in request_json:
        if "min_capacity" in request_json["capacity_range"]:
            classrooms = classrooms.filter(classroom_capacity__gte=request_json["capacity_range"]["min_capacity"])
        if "max_capacity" in request_json["capacity_range"]:
            classrooms = classrooms.filter(classroom_capacity__lte=request_json["capacity_range"]["max_capacity"])
    if "limit" in request_json:
        classrooms = classrooms[0:request_json["limit"]]
    result_list = [
        {
            "classroom_name": classroom.classroom_name,
            "classroom_id": classroom.id,
            "classroom_capacity": classroom.classroom_capacity
        } for classroom in list(classrooms)
    ]

    return JsonResponse(
        {
            "classroom_list": result_list
        }
    )


@check_json(schema.entity_new_classroom)
@admin_required
def new_classroom(request):
    request_json = json.loads(request.body)
    classroom = entity.models.Classroom(classroom_name=request_json["classroom_name"],
                                        classroom_capacity=request_json["classroom_capacity"])
    try:
        classroom.save()
    except Exception:
        return JsonResponse({**error_code.CLACK_CREATE_NEW_MODELS_FAILED})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.entity_new_course)
@admin_required
def new_course(request):
    request_json = json.loads(request.body)
    return JsonResponse({**error_code.CLACK_UNIMPLEMENTED_API})


@check_json(schema.entity_new_department)
@admin_required
def new_department(request):
    request_json = json.loads(request.body)
    department = entity.models.Department(department_name=request_json['department']['department_name'])
    try:
        with transaction.atomic():
            department.save()
    except Exception as e:
        print(str(e))
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


def department_list(request):
    departments = entity.models.Department.objects.all()
    result_list = [{
        'department_id': department.id,
        'department_name': department.department_name
    } for department in list(departments)]
    return JsonResponse({**error_code.CLACK_SUCCESS, "department_list": result_list})


@check_json(schema.entity_new_major)
@admin_required
def new_major(request):
    request_json = json.loads(request.body)
    major = entity.models.Major(major_name=request_json['major']['major_name'],
                                major_department_id=request_json['major']['major_department_id'])
    try:
        with transaction.atomic():
            major.save()
    except Exception as e:
        print(str(e))
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.entity_major_list)
def major_list(request):
    request_json = json.loads(request.body)
    majors = entity.models.Major.objects.all()
    if 'major' in request_json:
        majors = majors.filter(major_department_id=request_json['major']['major_department_id'])
    result_list = [{
        'major_id': major.id,
        'major_name': major.major_name,
        'major_department_id': major.major_department_id
    } for major in list(majors)]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'major_list': result_list})


@check_json(schema.entity_new_banji)
@admin_required
def new_banji(request):
    request_json = json.loads(request.body)
    banji = entity.models.Banji(banji_major_id=request_json['banji']['banji_major_id'],
                                banji_name=request_json['banji']['banji_name'])
    try:
        with transaction.atomic():
            banji.save()
    except Exception as e:
        print(str(e))
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.entity_banji_list)
def banji_list(request):
    request_json = json.loads(request.body)
    banjis = entity.models.Banji.objects.all()
    result_list = [{
        'banji_id': banji.id,
        'banji_name': banji.banji_name,
        'banji_major_id': banji.banji_major_id,
        'banji_department_id': banji.banji_major.major_department_id
    } for banji in banjis]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'banji_list': result_list})


# 返回查询学号的学生信息
@check_json(schema.entity_student)
@login_required
def student(request):
    request_json = json.loads(request.body)
    user = entity.models.User.objects.get(user_name=request_json['user_name'])
    if not (user.user_type == 0 or
            user.user_type == 1 or
            (user.user_type == 2 and user.user_student.student_number == request_json['student']['student_number'])):
        return JsonResponse({**error_code.CLACK_NO_PERMISSION})
    try:
        student_result = entity.models.Student.objects.get(student_number=request_json['student']['student_number'])
    except:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    return JsonResponse({
        "student": {
            "student_name": student_result.student_name,
            "student_number": student_result.student_number,
            "student_banji_id": student_result.student_banji_id,
            "student_email": student_result.student_email,
            "student_start_year": student_result.student_start_year,
            "student_end_year": student_result.student_end_year
        }
    })


# 返回查询教师工号的教师信息
@check_json(schema.entity_teacher)
@login_required
def teacher(request):
    request_json = json.loads(request.body)
    try:
        teacher_result = entity.models.Teacher.objects.get(teacher_number=request_json['teacher']['teacher_number'])
    except:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})
    return JsonResponse({
        "teacher": {
            "teacher_name": teacher_result.teacher_name,
            "teacher_number": teacher_result.teacher_number,
            "teacher_email": teacher_result.teacher_email,
            "teacher_department_id": teacher_result.teacher_department_id
        }
    })
