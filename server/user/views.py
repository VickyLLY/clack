from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from server.decorators import login_required, post_required, check_json
import entity.models
import hashlib
from server import error_code
from uuid import uuid1
from server import schema
from django.db import transaction


def encode_password(password: str):
    return hashlib.sha256(password.encode("utf8")).hexdigest()


@check_json(schema.user_login)
def login(request):
    request_json = json.loads(request.body)
    query_result = list(entity.models.User.objects.filter(user_name=request_json['user_name']))
    if len(query_result) is 0:
        return JsonResponse({**error_code.CLACK_USER_LOGIN_FAILED})
    user = query_result[0]
    if user.user_password != encode_password(request_json['user_password']):
        return JsonResponse({**error_code.CLACK_USER_LOGIN_FAILED})
    user.user_token = uuid1()
    user.save()
    return JsonResponse({**error_code.CLACK_SUCCESS, 'user_type': user.user_type, 'user_token': user.user_token})


@check_json(schema.user_logout)
@login_required
def logout(request):
    request_json = json.loads(request.body)
    user = entity.models.User.objects.get(request_json['user']['user_name'])
    user.user_token = uuid1()
    user.save()
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.user_signup_student)
def signup_student(request):
    request_json = json.loads(request.body)
    try:
        with transaction.atomic():
            student = entity.models.Student(student_name=request_json['student']['student_name'],
                                            student_number=request_json['student']['student_number'],
                                            student_banji_id=request_json['student']['student_banji_id'],
                                            student_email=request_json['student']['student_email'],
                                            student_start_year=request_json['student']['student_start_year'],
                                            student_end_year=request_json['student']['student_end_year'],
                                            )
            student.save()
            student_user = entity.models.User(user_name=request_json['user']['user_name'],
                                              user_password=encode_password(request_json['user']['user_password']),
                                              user_type=2,
                                              user_student_id=student.id)
            student_user.save()
    except Exception as e:
        print(request_json)
        print(str(e))
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.user_signup_teacher)
def signup_teacher(request):
    request_json = json.loads(request.body)
    try:
        with transaction.atomic():
            teacher = entity.models.Teacher(teacher_name=request_json['teacher']['teacher_name'],
                                            teacher_number=request_json['teacher']['teacher_number'],
                                            teacher_email=request_json['teacher']['teacher_email'],
                                            teacher_department_id=request_json['teacher']['teacher_department_id'])
            teacher.save()
            teacher_user = entity.models.User(user_name=request_json['user']['user_name'],
                                              user_password=encode_password(request_json['user']['user_password']),
                                              user_type=2,
                                              user_teacher_id=teacher.id)
            teacher_user.save()
    except Exception as e:
        print(request_json)
        print(str(e))
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.user_signup_admin)
def signup_admin(request):
    request_json = json.loads(request.body)
    admin_user = entity.models.User(user_name=request_json['user']['user_name'],
                                    user_password=encode_password(request_json['user']['user_password']),
                                    user_type=0)
    try:
        admin_user.save()
    except Exception as e:
        if len(list(entity.models.User.objects.filter(user_name=request_json['user']['user_name']))) is not 0:
            return JsonResponse({**error_code.CLACK_USER_NAME_EXISTS})
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@check_json(schema.user_login_status)
# 测试用户是否登录成功
@login_required
def login_status(request):
    return JsonResponse({**error_code.CLACK_SUCCESS})
