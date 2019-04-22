import json

import scoremng.models
from server import error_code, schema
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from server.decorators import check_json
from entity.models import Student, Course, Teacher


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
        if year == str(course.course_year) and semester == str(course.course_semester):
            course_info = {
                'course_name': course.course_name,
                'course_credit': course.course_credit,
                'course_year': course.course_credit,
                'course_semester': course.course_semester,
                'course_type': course.course_type,
            }

            # 课程信息和分数的打包
            course_and_score = {
                'course_info': course_info,
                'score': item.score,
            }
            score_list.append(course_and_score)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'score_list': score_list})


# 学生课程评价
# 应该是老师填写完成绩后，才能填写课程评价，才能看成绩
def courses_comment(request, student_number):
    if request.method == "GET":
        # 这名学生所选的全部课程的列表
        course_list_list = []

        # 在选课表中查找这名学生所选的全部课程，填写course_name -> 需要scoremng_SelectCourse
        # 用这门课程在课程中查询这门课程的type，如0,填写course_type -> 已有entity_Course
        # 用这门课程在教师排课表中查询这门课程的任课教师，填写course_teacher -> 需要scoremng_ScheduleTeacher
        student_id = Student.objects.get(student_number=student_number).id

        # 由这名学生的id找到他所选的所有课程
        items_in_score = scoremng.models.Score.objects.filter(student_id=student_id)
        for item in items_in_score:
            # 这一门课的id, type和name
            course_id = item.course_id
            course_type = Course.objects.get(id=course_id).course_type
            course_name = Course.objects.get(id=course_id).course_name

            # 在给老师的排课表中由这门课程找到代课老师的id
            teacher_id = scoremng.models.TeacherSchedule.objects.get(course_id=course_id).teacher_id

            # 有代课老师的id找到代课老师的name
            teacher_name = Teacher.objects.get(id=teacher_id).teacher_name

            # 把这些信息打包成一个json
            course = {
                "status": "未提交",
                "course_name": course_name,
                "course_teacher": teacher_name,
                "course_type": course_type,
            }
            course_list.append(course)
        return JsonResponse({**error_code.CLACK_SUCCESS, 'course_list': course_list})
    elif request.method == "POST":
        request_json = json.loads(request.body)
        course_name = request_json['course_name']
        course_teacher = request_json['course_teacher']
        course_comment = request_json['course_comment']

        # 因为一门名字一样的课可能由多名老师来带，但是一名老师不能带多门同名的课
        # 所以由老师的名字找到这个老师带的所有课，然后在所有课中找到课名为course_name的，得到他的course_id
        teacher_id = Teacher.objects.get(teacher_name=course_teacher).id

        # 这名老师带的所有课
        teacher_courses = scoremng.models.TeacherSchedule.objects.filter(teacher_id=teacher_id)

        for teacher_course in teacher_courses:
            # 老师带的一门课的课程id
            temp_course_id = teacher_course.course_id
            course = Course.objects.get(id=temp_course_id)
            # 如果这门课的名字就是要找的course_name，就选中这门课
            if course.course_name == course_name:
                course_id = course.id
                break

        student_id = Student.objects.get(student_number=student_number).id
        print(student_id, course_id)
        # 找到这条成绩记录
        score = scoremng.models.Score.objects.get(student_id=student_id, course_id=course_id)

        # 给成绩记录添加课程评论
        score.comment = course_comment

        # 存储到数据库中
        try:
            score.save()
        except Exception:
            return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
        return JsonResponse({**error_code.CLACK_SUCCESS})

