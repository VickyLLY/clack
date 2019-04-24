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
        temp = result
        result = list()
        for classroom in temp:
            course_date.classroom_id = classroom.id
            if course_date.check_is_valid():
                result.append(classroom)
    # TODO 考试时间还没筛
    result = [classroom.to_dict() for classroom in classrooms]
    return {**error_code.CLACK_SUCCESS, 'classroom_list': result}


def course_add_dc(request):
    request_json = json.loads(request.body)
    try:
        course = entity.models
        pass
    except:
        pass


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
