from django.shortcuts import render
from django.http import JsonResponse
from server import error_code
import json
import entity.models
import dst.models
from server.decorators import admin_required,login_required


# Create your views here.
@admin_required
def view_detail(request):
    request_json = json.loads(request.body)
    result = entity.models.DissertationTopic.objects.filter(dissertation_id=request_json['dissertation_id'])
    dlist = [{
        'dissertation_id': result[0].id,
        'dissertation_title': result[0].dissertation_title,
        'dissertation_content': result[0].dissertation_content,
        'dissertation_requirement': result[0].dissertation_requirement,
        'dissertation_capacity': result[0].dissertation_capacity,
        'dissertation_pub_time': result[0].dissertation_pub_time,
        'dissertation_approval': result[0].dissertation_approval,
        'dissertation_tnum_id':result[0].dissertation_tnum_id
    }]
    return JsonResponse({'dlist': dlist})

@admin_required
def new_dst(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    tnum=user.user_teacher_id
    dst = entity.models.DissertationTopic(
        dissertation_title=request_json['dissertation']['dissertation_title'],
        dissertation_content=request_json['dissertation']['dissertation_content'],
        dissertation_requirement=request_json['dissertation']['dissertation_requirement'],
        dissertation_capacity=request_json['dissertation']['dissertation_capacity'],
        dissertation_tnum_id=tnum,
    )
    try:
        dst.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

@login_required
def stu_select(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    snum=user.user_student_id
    check_result = dst.models.Application.objects.filter(student_id=snum)
    if check_result.exists():
            return  JsonResponse({**error_code.CLACK_STUDENT_SELECT_DST_EXISTS})
    stu_select_dst = dst.models.Application(
        dissertation_id=request_json['dissertation_id'],
        student_id=snum,
    )
    try:
        stu_select_dst.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})