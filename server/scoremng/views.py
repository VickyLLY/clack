import json

import scoremng.models
from server import error_code, schema
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from server.decorators import check_json


def teacher_upload(request):
    request_json = json.loads(request.body)
    # 把新增的学生成绩添加到数据库中
    score = scoremng.models.Score(student_id=request_json['student_id'], course_id=request_json['course_id'],
                                  score=request_json['score'])
    try:
        score.save()
    except Exception:
        return JsonResponse({**error_code.CLACK_CREATE_NEW_MODELS_FAILED})
    return JsonResponse({**error_code.CLACK_SUCCESS})


def test(request):
    sdfghjk
    pass