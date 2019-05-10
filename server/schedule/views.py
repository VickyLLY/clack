from django.shortcuts import render
from django.http import JsonResponse
from server import error_code
import json
import entity.models
from server.decorators import admin_required, login_required
import schedule.models


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
    request_json = json.loads(request.body)
    courses = entity.models.Course.objects.all()
    if 'course_type' in request_json:
        courses = courses.filter(course_type=request_json['course_type'])
    if 'course_year' in request_json:
        courses = courses.filter(course_year=request_json['course_year']);
    if 'course_semester' in request_json:
        courses = courses.filter(course_semester=request_json['course_semester'])
    if 'course_department_id' in request_json:
        courses = courses.filter(course_department_id=request_json['course_department_id'])
    result = [course.to_dict() for course in courses]
    return JsonResponse({**error_code.CLACK_SUCCESS, "course_list": result})


def classroom_list(request):
    request_json = json.loads(request.body)
    classrooms = entity.models.Classroom.objects.all()
    if 'capacity_range' in request_json:
        if 'min_capacity' in request_json['capacity_range']:
            classrooms = classrooms.filter(classroom_capacity__gte=request_json['capacity_range']['min_capacity'])
        if 'max_capacity' in request_json['capacity_range']:
            classrooms = classrooms.filter(classroom_capacity__lte=request_json['capacity_range']['max_capacity'])
    result = [classroom for classroom in classrooms]
    if 'course_date' in request_json:
        course_date = entity.models.DateAndClassroom(type=0,
                                                     year=request_json['course_date']['year'],
                                                     semester=request_json['course_date']['semester'],
                                                     start_week=request_json['course_date']['start_week'],
                                                     end_week=request_json['course_date']['end_week'],
                                                     day_of_week=request_json['course_date']['day_of_week'],
                                                     start=request_json['course_date']['start'],
                                                     end=request_json['course_date']['end'])
        if 'id' in request_json['course_date']:
            course_date.id = request_json['course_date']['id']
        temp = result
        result = list()
        for classroom in course_date.get_free_classroom():
            if classroom in temp:
                result.append(classroom)
    # TODO 考试时间还没筛
    result = [classroom.to_dict() for classroom in result]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'classroom_list': result})


def course_add_dc(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        DC = entity.models.DateAndClassroom(type=0)
        if 'id' in request_json:
            DC = entity.models.DateAndClassroom.objects.get(id=request_json['id'])
        DC.classroom_id = request_json['classroom_id']
        DC.course_id = request_json['course_id']
        DC.year = course.course_year
        DC.semester = course.course_semester
        DC.start_week = request_json['date']['start_week']
        DC.end_week = request_json['date']['end_week']
        DC.day_of_week = request_json['date']['day_of_week']
        DC.start = request_json['date']['start']
        DC.end = request_json['date']['end']
        # TODO 检查时间与任课教师的其他课程是否冲突
        DC.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# TODO 修改课程信息的这坨接口非常恶心,感觉是米婆婆喝多了, 如果有时间可以考虑改一下, 大概是不会改了
@admin_required
def change_course_name(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        course.course_name = request_json['course_name']
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@admin_required
def change_course_credit(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        course.course_credit = request_json['course_credit']
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@admin_required
def change_course_type(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        course.course_type = request_json['course_type']
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@admin_required
def change_course_semester(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        course.course_year = request_json['course_year']
        course.course_semester = request_json['course_semester']
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@admin_required
def change_course_capacity(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        course.course_capacity = request_json['course_capacity']
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@admin_required
def change_course_department(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        course.course_department_id = request_json['course_department_id']
        course.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


def mock_xuanke(request):
    request_json = json.loads(request.body)
    try:
        student_id = entity.models.Student.objects.get(student_number=request_json['student_number']).id
        mock = schedule.models.MockStudentCourse(student_id=student_id, course_id=request_json['course_id'])
        mock.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


def student_course_list(request):
    # TODO 替换mock,权限
    request_json = json.loads(request.body)
    try:
        mocks = schedule.models.MockStudentCourse.objects.filter(student__student_number=request_json['student_number'])
        result = [mock.course.to_dict() for mock in mocks]
        return JsonResponse({**error_code.CLACK_SUCCESS, "course_list": result})
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})


def del_dc(request):
    request_json = json.loads(request.body)
    try:
        dc = entity.models.DateAndClassroom.objects.get(id=request_json['id'])
        dc.classroom = None
        dc.course = None
        dc.exam = None
        dc.type = -1
        dc.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@login_required
def course_info(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models.Course.objects.get(id=request_json['course_id'])
        return JsonResponse({**error_code.CLACK_SUCCESS, "course": course.to_dict()})
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "error_message": str(e)})

@admin_required
def teacher_list(request):
    request_json = json.loads(request.body)
    teachers = entity.models.Teacher.objects.all()
    result = [teacher.to_dict() for teacher in teachers]
    return JsonResponse({**error_code.CLACK_SUCCESS,"teacher_list":result})