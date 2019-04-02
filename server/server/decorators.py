from django.http import JsonResponse
from server import error_code
from entity.models import User
import json


def login_required(func):
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


def post_required(func):
    def wrapped_func(request):
        if request.method != 'POST':
            return JsonResponse({**error_code.CLACK_POST_REQUIRED})
        return func(request)

    return wrapped_func
