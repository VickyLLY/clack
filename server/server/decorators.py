from django.http import JsonResponse
from server import error_code
from entity.models import User
import json
import jsonschema

# 开启debug模式后login_required,admin_required都会失效
debug_mode = False


def login_required(func):
    if debug_mode:
        return func

    @post_required
    def wrapped_func(request):
        request_json = json.loads(request.body)
        if "user_name" not in request_json or "user_token" not in request_json:
            return JsonResponse({**error_code.CLACK_REQUEST_JSON_ERROR})
        query_result = list(
            User.objects.filter(user_name=request_json['user_name'], user_token=request_json['user_token']))
        if len(query_result) is 0:
            return JsonResponse({**error_code.CLACK_LOGIN_REQUIRED})
        return func(request)

    return wrapped_func


def admin_required(func):
    if debug_mode:
        return func

    @login_required
    def wrapped_func(request):
        request_json = json.loads(request.body)
        query_result = list(
            User.objects.filter(user_name=request_json['user_name']))
        user = query_result[0]
        if user.user_type is not 0:
            return JsonResponse({**error_code.CLACK_ADMIN_REQUIRED})
        return func(request)

    return wrapped_func


def post_required(func):
    def wrapped_func(request):
        if request.method != 'POST':
            return JsonResponse({**error_code.CLACK_POST_REQUIRED})
        return func(request)

    return wrapped_func


def check_json(json_schema: dict):
    def decorator_func(func):
        @post_required
        def wrapped_func(request):
            request_json = json.loads(request.body)
            try:
                jsonschema.validate(instance=request_json, schema=json_schema)
            except jsonschema.exceptions.ValidationError as e:
                print(e.message)
                return JsonResponse({**error_code.CLACK_REQUEST_JSON_ERROR, "error_message": e.message})
            return func(request)

        return wrapped_func

    return decorator_func
