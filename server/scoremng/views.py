import json

import scoremng.models
from server import error_code, schema
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from server.decorators import check_json
from entity.models import Student, Course


# 老师上传成绩
def teacher_upload(request):
    request_json = json.loads(request.body)

    # 从json中获得学生的学号，课程的课号，课程分数
    student_number = request_json['student_number']
    course_name = request_json['course_name']
    score = request_json['score']
    print(student_number, course_name, score)

    # 由student_number找到student_id
    student = Student.objects.get(student_number=student_number)

    # 由course_number找到course_id
    course = Course.objects.get(course_name=course_name)

    # 把新增的学生成绩添加到数据库中
    score = scoremng.models.Score(student_id=student.id, course_id=course.id,
                                  score=score)
    try:
        score.save()
    except Exception:
        return JsonResponse({**error_code.CLACK_CREATE_NEW_MODELS_FAILED})
    return JsonResponse({**error_code.CLACK_SUCCESS})


# 登录后，进入成绩查看界面,选择查看成绩
# 学号为student_number的学生查看自己的成绩
def student_scores(request, student_number):
    year = request.GET.get("year")
    semester = request.GET.get("semester")

    # 学号为student_number的学生的所有成绩
    score_list = []

    # 得到该学生的student_id
    student = Student.objects.get(student_number=student_number)

    # 由学生id过滤出该生所有的成绩记录
    items_in_score = scoremng.models.Score.objects.filter(student_id=student.id)

    for item in items_in_score:
        # 由一条成绩记录找出记录中的course_id
        course_id = item.course_id

        # 由course_id在Course表中找到这门课程
        course = Course.objects.get(id=course_id)

        # 如果这门课程的年份和学期刚好对应学生查询时输入的课程和年份
        # if year == str(course.course_year) and semester == str(course.course_semester):
        #     course_info = {
        #         'course_name': course.course_name,
        #         'course_credit': course.course_credit,
        #         'course_year': course.course_credit,
        #         'course_semester': course.course_semester,
        #         'course_type': course.course_type,
        #     }
        #
        #     # 课程信息和分数的打包
        #     course_and_score = {
        #         'course_info': course_info,
        #         'score': item.score,
        #     }
        #     score_list.append(course_and_score)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'score_list': score_list})

