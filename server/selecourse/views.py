# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from server.decorators import login_required, post_required, check_json
from entity.models import Student, Course
import selecourse.models
import hashlib
from server import error_code
from uuid import uuid1
from server import schema
from django.db import transaction


# 登录后，进入选课界面,查看可以选择的课程
# 学号为student_number的学生查看可以选择的课程
def student_sele(request, student_number):
    # 学号为student_number的学生的可选择的课程信息
    course_list = []
    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    # 得到该学生的student_number的一条记录
    selection_student = Student.objects.get(student_number=student_number)
    # 由学生id过滤出该生所有的选课记录
    items_in_sele = selecourse.models.Selection.objects.filter(student_id=selection_student.id)
    for item in items_in_sele:
        # 由一条成绩记录找出记录中的course_id
        course_id = item.course_id
        # 由course_id在Course表中找到这门课程
        course = Course.objects.get(id=course_id)
        # 如果这门课程的年份和学期刚好对应学生查询时输入的课程和年份
        if year == course.course_year and semester == course.course_semester:
            result = {
                "course_name": course.course_name,
                "course_start": course.course_start,
                "course_end": course.course_end,
                "course_credit": course.course_credit,
                "course_type": course.course_type,
                "course_classroom": course.course_classroom,
                "course_year": course.course_year,
                "course_capacity": course.course_capacity,
                "course_teacher": course.course_teacher,
                "course_access": course.course_access,
                "course_department": course.course_department,
            }
            course_list.append(result)
        return JsonResponse({**error_code.CLACK_SUCCESS, 'course_list': course_list})


def student_inquiry(request):
    course_list = []
    request_json = json.loads(request.body)
    student_number = request_json["student_number"]
    selecourses = selecourse.models.selection.objects.filter(selection_student=student_number)
    for item in selecourses:
        course_id = item.id
        course = Course.objects.get(id=course_id)
        result = {
            "course_name": course.course_name,
            "course_start": course.course_start,
            "course_end": course.course_end,
            "course_credit": course.course_credit,
            "course_type": course.course_type,
            "course_classroom": course.course_classroom,
            "course_year": course.course_year,
            "course_capacity": course.course_capacity,
            "course_teacher": course.course_teacher,
            "course_access": course.course_access,
            "course_department": course.course_department,
        }
        course_and_message = {
            'course_info': result,
        }
        course_list.append(course_and_message)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'score_list': course_list})


def teacher_inquiry(request):
    request_json = json.loads(request.body)
    teacher_number = request_json["teacher_number"]
    courses = Course.objects.get(course_teacher=teacher_number)
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