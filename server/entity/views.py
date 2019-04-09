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
