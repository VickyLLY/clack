# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from server.decorators import login_required, post_required, check_json
import entity.models
import selecourse.models
import hashlib
from server import error_code
from uuid import uuid1
from server import schema
from django.db import transaction


def student_sele(request):
    pass
    pass


def student_inquiry(request):
    request_json=json.loads(request.body)
    student_number=request_json["student_number"]
    selecourses=selecourse.models.selection.objects.get(selection_student=student_number)
    course_all=entity.models.Course.objects.all()
    result=[
        {
            "course_name": cou.course_name,
            "course_start": cou.course_start,
            "course_end": cou.course_end,
            "course_credit": cou.course_credit,
            "course_type": cou.course_type,
            "course_classroom": cou.course_classroom,
            "course_year": cou.course_year,
            "course_capacity": cou.course_capacity,
            "course_teacher":cou.course_teacher,
            "course_department":cou.course_department,
        }for cou in list(course_all)
             for any in list(selecourses)
                 if any == cou.id
    ]

    return JsonResponse(
        {
            "courses_information": result
        }
    )

def teacher_inquiry(request):
    request_json=json.loads(request.body)
    teacher_number=request_json["teacher_number"]
    courses=entity.models.Course.objects.get(course_teacher=teacher_number)
    result = [
        {
            "course_name":course.course_name,
            "course_start": course.course_start,
            "course_end": course.course_end,
            "course_credit": course.course_credit,
            "course_type": course.course_type,
            "course_classroom": course.course_classroom,
            "course_year": course.course_year,
            "course_capacity": course.course_capacity,
            "course_department": course.course_department,

        } for course in list(courses)
    ]
    return JsonResponse(
        {
            "courses_information": result
        }
    )