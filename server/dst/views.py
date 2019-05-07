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

@login_required
def dst_list(request):
    request_json = json.loads(request.body)
    dsts = entity.models.DissertationTopic.objects.all()
    result_list = []
    for dst in dsts:
        tname=list(entity.models.Teacher.objects.filter(id=dst.dissertation_tnum_id))
        tt=tname[0]
        result_list_te = [{
            'dissertation_id': dst.id,
            'dissertation_title': dst.dissertation_title,
            'dissertation_content': dst.dissertation_content,
            'dissertation_requirement': dst.dissertation_requirement,
            'dissertation_capacity': dst.dissertation_capacity,
            'dissertation_approval': dst.dissertation_approval,
            'dissertation_pub_time': dst.dissertation_pub_time,
            'dissertation_teacher': tt.teacher_name,
        } ]
        result_list = result_list + result_list_te

    return JsonResponse({**error_code.CLACK_SUCCESS, 'dst_list': result_list})

@login_required
def dst_list_approval(request):
    request_json = json.loads(request.body)
    dsts = entity.models.DissertationTopic.objects.filter(dissertation_approval=True)
    result_list=[]
    for dst in dsts:
        tname=list(entity.models.Teacher.objects.filter(id=dst.dissertation_tnum_id))
        tt=tname[0]
        result_list_te = [{
            'dissertation_id': dst.id,
            'dissertation_title': dst.dissertation_title,
            'dissertation_content': dst.dissertation_content,
            'dissertation_requirement': dst.dissertation_requirement,
            'dissertation_capacity': dst.dissertation_capacity,
            'dissertation_pub_time': dst.dissertation_pub_time,
            'dissertation_teacher': tt.teacher_name,
        } ]
        result_list = result_list + result_list_te

    return JsonResponse({**error_code.CLACK_SUCCESS, 'dst_list': result_list})

@login_required
def teacher_dst_list(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    tnum = user.user_teacher_id
    dsts = entity.models.DissertationTopic.objects.filter(dissertation_tnum_id=tnum)
    result_list = [{
        'dissertation_id': dst.id,
        'dissertation_title': dst.dissertation_title,
        'dissertation_content': dst.dissertation_content,
        'dissertation_requirement': dst.dissertation_requirement,
        'dissertation_capacity': dst.dissertation_capacity,
        'dissertation_approval':dst.dissertation_approval,
        'dissertation_pub_time':dst.dissertation_pub_time,
    } for dst in dsts]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'teacher_dst_list': result_list})

@login_required
def stu_dst_list(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    snum = user.user_student_id
    dd=dst.models.Application.objects.filter(student_id=snum)
    tnum=dd[0].dissertation_id
    dsts = entity.models.DissertationTopic.objects.filter(id=tnum)
    tname = list(entity.models.Teacher.objects.filter(id=dsts[0].dissertation_tnum_id))
    tt = tname[0]
    result_list = [{
        'dissertation_id': dsta.id,
        'dissertation_title': dsta.dissertation_title,
        'dissertation_content': dsta.dissertation_content,
        'dissertation_requirement': dsta.dissertation_requirement,
        'dissertation_capacity': dsta.dissertation_capacity,
        'dissertation_pub_time': dsta.dissertation_pub_time,
        'dissertation_teacher': tt.teacher_name,
    } for dsta in dsts]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'stu_dst_list': result_list})
