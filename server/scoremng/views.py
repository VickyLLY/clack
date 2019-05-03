import json
import os

import xlwt
from io import StringIO
import scoremng.models
from server import error_code, schema
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from server.decorators import check_json
from entity.models import Student, Course, Teacher, Banji


# 老师上传成绩
# 由老师所带的所有课程，以一门课为例，找到选这门课的学生
# 需要讨论一下做成下拉框的形式 一个老师选择了一门课后 下一个框就是他到的所有学生
# 或者开始时把这个老师带的所有学生都显示出来，然后要求老师去选择那门课，这个信息由前端传过来
# 然后后端由这个老师和这门课给前端传所有学生的信息，让这个老师去填写
# 目前状态：未完成
def teacher_upload(request, teacher_number):

    # 老师选择学年，学期，学生号，课程名称，分数，提交到后端

    request_json = json.loads(request.body)

    # 从json中获得学生的学号，课程的课号，课程分数
    year = request_json['year']
    semester = request_json['semester']
    student_number = request_json['student_number']
    course_name = request_json['course_name']
    score = request_json['score']
    print(teacher_number, year, semester, student_number, course_name, score)

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
# 如果返回信息中不包含任课老师的信息，就不需要用其他组的表
# 目前状态：已完成
def student_check_scores(request):
    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    student_number = request_json['student_number']
    print(student_number, semester, type(year), type(semester))

    # 学号为student_number的学生的所有成绩
    score_list = []

    # 得到该学生的student_id
    try:
        student = Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

    # print(student.id, student.student_name)
    # 由学生id过滤出该生所有的成绩记录
    try:
        items_in_score = scoremng.models.Score.objects.filter(student_id=student.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_SCORE_NOT_EXISTS})
    # print(len(items_in_score))

    for item in items_in_score:
        # 由一条成绩记录找出记录中的course_id
        course_id = item.course_id

        # 由course_id在Course表中找到这门课程
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

        # print(year, type(year), course.course_year, type(course.course_year))

        # 如果这门课程的年份和学期刚好对应学生查询时输入的课程和年份
        if year == str(course.course_year) and semester == str(course.course_semester):
            course_and_score = {
                'course_name': course.course_name,
                'course_credit': course.course_credit,
                'course_year': course.course_year,
                'course_semester': course.course_semester,
                'course_type': course.course_type,
                'score': item.score,
            }
            score_list.append(course_and_score)
    # print(len(score_list))  # 添加这句看一下打印出来的是不是和预想的课程数量是一致的
    return JsonResponse({**error_code.CLACK_SUCCESS, 'score_list': score_list})


# 学生课程评价
# 应该是老师填写完成绩后，才能填写课程评价，才能看成绩
# 目前状态：已完成
def courses_comment(request):
    request_json = json.loads(request.body)
    student_number = request_json['student_number']
    course_name = request_json['course_name']
    course_credit = request_json['course_credit']
    course_year = request_json['course_year']
    course_semester = request_json['course_semester']
    score = request_json['score']
    course_comment = request_json['course_comment']
    print(student_number)

    try:
        student_id = Student.objects.get(student_number=student_number).id
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

    try:
        course_id = Course.objects.get(course_name=course_name,
                                       course_year=int(course_year),
                                       course_semester=int(course_semester)).id
        print(type(course_year), type(course_semester))  # 仍然是str，后续可以放心使用
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

    # 拿着学生的学号，课程的课号，和评论往数据库中填
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
# 如果不需要返回任课教师的信息，就不需要用其他组的表
# 目前状态：已完成
def student_download_scores(request):
    request_json = json.loads(request.body)
    student_number = request_json['student_number']
    year = request_json['year']
    semester = request_json['semester']
    print(student_number, year, semester)

    # 下载成绩到excel表格中
    wb = xlwt.Workbook(encoding='utf-8')
    w = wb.add_sheet(u'学生成绩', cell_overwrite_ok=True)
    w.write(0, 0, u'课程名称')
    w.write(0, 1, u'课程学分')
    w.write(0, 2, u'课程学年')
    w.write(0, 3, u'课程学期')
    w.write(0, 4, u'课程种类')
    w.write(0, 5, u'成绩')
    excel_row = 1

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
            course_and_score = {
                'course_name': course.course_name,
                'course_credit': course.course_credit,
                'course_year': course.course_year,
                'course_semester': course.course_semester,
                'course_type': course.course_type,
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

    # print(len(score_list))
    exist_file = os.path.exists(student.student_name + ' ' + year + '年 第' + semester + '学期的成绩单.xls')
    if exist_file:
        os.remove(student.student_name + ' ' + year + '年 第' + semester + '学期的成绩单.xls')
    wb.save(student.student_name + ' ' + year + '年 第' + semester + '学期的成绩单.xls')
    return JsonResponse({**error_code.CLACK_SUCCESS, 'score_list': score_list})


# 老师选择特定的学年和学期，查看学生的成绩
# 因为用到了排课组的排课表，所以还未完成
# 目前状态：未完成
def teacher_check_scores(request, teacher_number):
    """
    在排课表中查找这名老师带的全部课程的id,
    在选课表中由课程id，查找到选这门课的学生的id
    因为先阶段不知道排课表和选课表中的字段设置，所以先给前端返回假数据
    """
    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    print(teacher_number, year, semester)  # 成功获得post的数据

    try:
        teacher = Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    wb = xlwt.Workbook(encoding='utf-8')
    w = wb.add_sheet(u'学生成绩', cell_overwrite_ok=True)
    w.write(0, 0, u'学生学号')
    w.write(0, 1, u'学生姓名')
    w.write(0, 2, u'学生班级')
    w.write(0, 3, u'课程名称')
    w.write(0, 4, u'课程种类')
    w.write(0, 5, u'课程学年')
    w.write(0, 6, u'课程学期')
    w.write(0, 7, u'课程学分')
    w.write(0, 8, u'课程成绩')
    excel_row = 1

    student_score_list = []

    student_score_list1 = {
        'student_number': '2015014069',
        'student_name': '尹毓康',
        'student_banji_name': '计科1602班',
        'course_name': '编译原理',
        'course_type': 0,
        'course_year': 2018,
        'course_semester': 1,
        'course_credit': 3,
        'course_score': 90,
    }

    student_score_list2 = {
        'student_number': '2016014069',
        'student_name': '蔡锐',
        'student_banji_name': '计科1605班',
        'course_name': '数据结构',
        'course_type': 0,
        'course_year': 2019,
        'course_semester': 1,
        'course_credit': 3,
        'course_score': 100,
    }

    student_score_list.append(student_score_list1)
    student_score_list.append(student_score_list2)
    print("---")

    # 在后端判断，如果老师点击的按钮名是"check",就把学生的成绩单返回给后端
    if "check" in request.POST:
        print('前端点击了check')
        return JsonResponse({**error_code.CLACK_SUCCESS, 'student_score_list': student_score_list})

    # 如果老师点击的按钮名是"download"，就把学生的成绩单以excel的形式保存下来
    if "download" in request.POST:
        print('前端点击了download')
        for student_score in student_score_list:
            w.write(excel_row, 0, student_score['student_number'])
            w.write(excel_row, 1, student_score['student_name'])
            w.write(excel_row, 2, student_score['student_banji_name'])
            w.write(excel_row, 3, student_score['course_name'])
            w.write(excel_row, 4, student_score['course_type'])
            w.write(excel_row, 5, student_score['course_year'])
            w.write(excel_row, 6, student_score['course_semester'])
            w.write(excel_row, 7, student_score['course_credit'])
            w.write(excel_row, 8, student_score['course_score'])
            excel_row += 1

        exist_file = os.path.exists(teacher.teacher_name + '所带学生的成绩单.xls')
        if exist_file:
            os.remove(teacher.teacher_name + '所带学生的成绩单.xls')
        wb.save(teacher.teacher_name + '所带学生的成绩单.xls')
        return JsonResponse({**error_code.CLACK_SUCCESS})

    # # 把成绩单里的学生成绩信息放入excel表中
    # for student_score in student_score_list:
    #     w.write(excel_row, 0, student_score['student_number'])
    #     w.write(excel_row, 1, student_score['student_name'])
    #     w.write(excel_row, 2, student_score['student_banji_name'])
    #     w.write(excel_row, 3, student_score['course_name'])
    #     w.write(excel_row, 4, student_score['course_type'])
    #     w.write(excel_row, 5, student_score['course_year'])
    #     w.write(excel_row, 6, student_score['course_semester'])
    #     w.write(excel_row, 7, student_score['course_credit'])
    #     w.write(excel_row, 8, student_score['course_score'])
    #     excel_row += 1
    #
    # exist_file = os.path.exists(teacher.teacher_name + '所带学生的成绩单.xls')
    # if exist_file:
    #     os.remove(teacher.teacher_name + '所带学生的成绩单.xls')
    # wb.save(teacher.teacher_name + '所带学生的成绩单.xls')
    # return JsonResponse({**error_code.CLACK_SUCCESS, 'student_score_list': student_score_list})


def admin_check(request, admin_number):
    print(admin_number)
    # 管理员进入页面后可以选择需要查看的学年和学期
    if request.method == "GET":
        # 返回所有可选择的班级
        banji_list = Banji.objects.all()
        banji_name_list = []
        for banji in banji_list:
            banji_name_list.append(banji.banji_name)
            print(banji.banji_name)

        return JsonResponse({**error_code.CLACK_SUCCESS,
                             'banji_name_list': banji_name_list,
                             'year_list': [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010],
                             'semester_list': [1, 2, 3], })

    elif request.method == 'POST':
        # 从前端获得管理员需要查询的学年，学期和班级名称
        request_json = json.loads(request.body)
        year = request_json['year']
        semester = request_json['semester']
        banji_name = request_json['banji_name']

        # 找到这个班级的banji_id
        try:
            banji_id = Banji.objects.all().get(banji_name=banji_name).id
        except Exception:
            return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})

        # 查询这个班的学生
        student_list = Student.objects.all().filter(student_banji=banji_id)
        for student in student_list:
            print(student.id)

        return HttpResponse("hello world.")
