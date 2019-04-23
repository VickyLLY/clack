import json
import os

import xlwt
from io import StringIO
import scoremng.models
from server import error_code, schema
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from server.decorators import check_json
from entity.models import Student, Course, Teacher


# 老师上传成绩
def teacher_upload(request, teacher_number):
    if request.method == "GET":
        return JsonResponse({
            'year_list': [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010],
            'semester_list': [1, 2, 3],
        })
    elif request.method == "POST":
        request_json = json.loads(request.body)

        # 从json中获得学生的学号，课程的课号，课程分数
        student_number = request_json['student_number']
        course_name = request_json['course_name']
        score = request_json['score']

        # 由student_number找到student_id
        try:
            student = Student.objects.get(student_number=student_number)
        except Exception:
            return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

        # 由course_number找到course_id
        try:
            course = Course.objects.get(course_name=course_name)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

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
    try:
        student = Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

    # 由学生id过滤出该生所有的成绩记录
    try:
        items_in_score = scoremng.models.Score.objects.filter(student_id=student.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_SCORE_NOT_EXISTS})

    for item in items_in_score:
        # 由一条成绩记录找出记录中的course_id
        course_id = item.course_id

        # 由course_id在Course表中找到这门课程
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

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
        course_list = []

        # 在选课表中查找这名学生所选的全部课程，填写course_name -> 需要scoremng_SelectCourse
        # 用这门课程在课程中查询这门课程的type，如0,填写course_type -> 已有entity_Course
        # 用这门课程在教师排课表中查询这门课程的任课教师，填写course_teacher -> 需要scoremng_ScheduleTeacher
        try:
            student_id = Student.objects.get(student_number=student_number).id
        except Exception:
            return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

        # 由这名学生的id找到他所选的所有课程
        try:
            items_in_score = scoremng.models.Score.objects.filter(student_id=student_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_SCORE_NOT_EXISTS})

        for item in items_in_score:
            # 这一门课的id, type和name
            course_id = item.course_id

            try:
                course_type = Course.objects.get(id=course_id).course_type
                course_name = Course.objects.get(id=course_id).course_name
            except Exception:
                return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

            # 在给老师的排课表中由这门课程找到代课老师的id
            teacher_id = scoremng.models.TeacherSchedule.objects.get(course_id=course_id).teacher_id

            # 有代课老师的id找到代课老师的name
            try:
                teacher_name = Teacher.objects.get(id=teacher_id).teacher_name
            except Exception:
                return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

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
        try:
            teacher_id = Teacher.objects.get(teacher_name=course_teacher).id
        except Exception:
            return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

        # 这名老师带的所有课
        teacher_courses = scoremng.models.TeacherSchedule.objects.filter(teacher_id=teacher_id)

        course_exists = False
        for teacher_course in teacher_courses:
            # 老师带的一门课的课程id
            temp_course_id = teacher_course.course_id

            try:
               course = Course.objects.get(id=temp_course_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

            # 如果这门课的名字就是要找的course_name，就选中这门课
            if course.course_name == course_name:
                course_id = course.id
                course_exists = True
                break

        if not course_exists:
            return JsonResponse({**error_code.CLACK_TEACH_NOT_EXISTS})

        try:
            student_id = Student.objects.get(student_number=student_number).id
        except Exception:
            return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

        # 找到这条成绩记录
        try:
            score = scoremng.models.Score.objects.get(student_id=student_id, course_id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_SCORE_NOT_EXISTS})

        # 给成绩记录添加课程评论
        score.comment = course_comment

        # 存储到数据库中
        try:
            score.save()
        except Exception:
            return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})
        return JsonResponse({**error_code.CLACK_SUCCESS})


# 学生下载自己的成绩
def download_scores(request, student_number):
    wb = xlwt.Workbook(encoding='utf-8')
    w = wb.add_sheet(u'学生成绩', cell_overwrite_ok=True)
    w.write(0, 0, u'课程名称')
    w.write(0, 1, u'课程学分')
    w.write(0, 2, u'课程学年')
    w.write(0, 3, u'课程学期')
    w.write(0, 4, u'课程种类')
    w.write(0, 5, u'成绩')
    excel_row = 1

    # 使用student_scores函数
    # 学号为student_number的学生查看自己的成绩
    year = request.GET.get("year")
    semester = request.GET.get("semester")
    print(year, semester)

    # 学号为student_number的学生的所有成绩
    score_list = []

    # 得到该学生的student_id
    try:
        student = Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

    # 由学生id过滤出该生所有的成绩记录
    try:
        items_in_score = scoremng.models.Score.objects.filter(student_id=student.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_SCORE_NOT_EXISTS})

    for item in items_in_score:
        # 由一条成绩记录找出记录中的course_id
        course_id = item.course_id

        # 由course_id在Course表中找到这门课程
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

        # 如果这门课程的年份和学期刚好对应学生查询时输入的课程和年份
        if year == str(course.course_year) and semester == str(course.course_semester):
            course_info = {
                'course_name': course.course_name,
                'course_credit': course.course_credit,
                'course_year': course.course_year,
                'course_semester': course.course_semester,
                'course_type': course.course_type,
            }

            # 课程信息和分数的打包
            course_and_score = {
                'course_info': course_info,
                'score': item.score,
            }

            # 把这些成绩存放到excel表格中
            w.write(excel_row, 0, course.course_name)
            w.write(excel_row, 1, course.course_credit)
            w.write(excel_row, 2, course.course_year)
            w.write(excel_row, 3, course.course_semester)
            w.write(excel_row, 4, course.course_type)
            w.write(excel_row, 5, item.score)
            excel_row += 1

            # 把成绩放入成绩单列表中
            score_list.append(course_and_score)

    exist_file = os.path.exists(student.student_name + '的成绩单.xls')
    if exist_file:
        os.remove(student.student_name + '的成绩单.xls')
    wb.save(student.student_name + '的成绩单.xls')
    return JsonResponse({**error_code.CLACK_SUCCESS, 'score_list': score_list})
