import json
from server import error_code
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def teacher_upload(request):
    request_json = json.loads(request.body)
    # print(request_json)
    # 把新增的学生成绩添加到数据库中

    return JsonResponse({**error_code.CLACK_SUCCESS})
