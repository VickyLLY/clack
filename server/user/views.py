from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from server.decorators import login_required, post_required
from entity.models import User
import hashlib
from server import error_code
from uuid import uuid1


def encode_password(password: str):
    return hashlib.sha256(password.encode("utf8")).hexdigest()


@post_required
def login(request):
    request_json = json.loads(request.body)
    if 'user_name' not in request_json or 'user_password' not in request_json:
        return JsonResponse({**error_code.CLACK_REQUEST_JSON_ERROR})
    query_result = list(User.objects.filter(user_name=request_json['user_name']))
    if len(query_result) is 0:
        return JsonResponse({**error_code.CLACK_USER_LOGIN_FAILED})
    user = query_result[0]
    if user.user_password != encode_password(request_json['user_password']):
        return JsonResponse({**error_code.CLACK_USER_LOGIN_FAILED})
    user.user_token = uuid1()
    user.save()
    return JsonResponse({**error_code.CLACK_SUCCESS, 'user_type': user.user_type, 'user_token': user.user_token})


@login_required
def logout(request):
    return HttpResponse('unimplemented')


@post_required
def signup(request):
    request_json = json.loads(request.body)
    new_user = User()
    if 'user_name' not in request_json or 'user_password' not in request_json or 'user_type' not in request_json:
        return JsonResponse({**error_code.CLACK_REQUEST_JSON_ERROR})
    new_user.user_name = request_json['user_name']
    new_user.user_password = encode_password(request_json['user_password'])
    new_user.user_type = request_json['user_type']
    try:
        new_user.save()
    except Exception as e:
        if len(list(User.objects.filter(user_name=request_json['user_name']))) is not 0:
            return JsonResponse({**error_code.CLACK_USER_NAME_EXISTS})
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# 测试用户是否登录成功
@login_required
def test_status(request):
    return JsonResponse({**error_code.CLACK_SUCCESS})
