from django.shortcuts import render
from django.http import JsonResponse
from server import error_code
import json
import entity.models
from server.decorators import admin_required


# Create your views here.
@admin_required
def new_course(request):
    request_json = json.loads(request.body)
    course = entity.models.Course(course_name=request_json['course']['course_name'],
                                  course_credit=request_json['course']['course_credit'],
                                  course_type=request_json['course']['course_type'],
                                  course_year=request_json['course']['course_year'],
                                  course_semester=request_json['course']['course_semester'],
                                  course_department_id=request_json['course']['course_department_id'],
                                  course_capacity=request_json['course']['course_capacity'])
    try:
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


def course_list(request):
    # request_json = json.loads(request.body)
    courses = entity.models.Course.objects.all()
    result = [course.to_dict() for course in courses]
    return JsonResponse({**error_code.CLACK_SUCCESS, "course_list": result})
