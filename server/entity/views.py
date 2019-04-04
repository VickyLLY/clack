from django.shortcuts import render
from django.http import JsonResponse
from server.decorators import post_required, admin_required, login_required, check_json
from server import error_code
import entity.models
import json
import jsonschema
from server import schema


@post_required
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
