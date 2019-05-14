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
from selecourse.models import Selection


# 管理员查看成绩
# 目前状态：未完成
def admin_check_scores(request):
    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    admin_number = request_json['admin_number']
    print(year, semester, admin_number)

    avg_score_list = []
    # 在year年 semester学期的所有课程

    course_list = Course.objects.filter(course_year=year,
                                        course_semester=semester)
    for certain_course in course_list:
        course_score = {
            'course_name': certain_course.course_name,
            'course_type': certain_course.course_type,
            'course_year': certain_course.course_year,
            'course_semester': certain_course.course_semester,
            'course_credit': certain_course.course_credit,
            'course_avg_score': 0,
        }

        # 选修这门课的学生人数
        student_amount = 0

        # 选修这门课的学生成绩的总分
        score_amount = 0

        # 在选课表中查看选了这门课的学生
        student_course_list = Selection.objects.filter(selection_course_id=certain_course.id)
        for student_course in student_course_list:
            # 查看这一门课这个学生的分数，如果在成绩表查找不到这个学生的这条记录，说明老师还没有登分，则暂定成绩为0
            try:
                student = Student.objects.get(id=student_course.selection_student_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

            # 锁定这名学生后学生人数+1
            student_amount += 1

            try:
                # 进入到try中说明有这名学生的成绩
                score = scoremng.models.Score.objects.get(student_id=student.id, course_id=certain_course.id)
                score_amount += score.score
            except Exception:
                # 进入到Exception中说明老师还没有登录这名学生的成绩
                score_amount += 0

        # 统计完选修这门课的所有学生后，计算平均分
        if student_amount == 0:
            avg_score = 0
        else:
            avg_score = score_amount / student_amount
        print('选修',certain_course.course_name, '的有', student_amount, '人，这们课的总分是', score_amount, '均分是', avg_score)
        course_score['course_avg_score'] = avg_score
        avg_score_list.append(course_score)
    return  JsonResponse({**error_code.CLACK_SUCCESS, 'avg_score_list': avg_score_list})


# 管理员下载成绩
# 目前状态：未完成
def admin_download_scores(request):
    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    admin_number = request_json['admin_number']
    print(year, semester, admin_number)
    return HttpResponse('Hello')


# 登录后，进入成绩查看界面,选择查看成绩
# 学号为student_number的学生查看自己的成绩
# 如果返回信息中不包含任课老师的信息，就不需要用其他组的表
# 目前状态：已完成
# 修改完数据库：对这个函数没有影响
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
# 修改数据库后：对这个函数没有影响
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
        student = Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    # print('student_id', student.id)

    try:
        course = Course.objects.get(course_name=course_name,
                                       course_year=int(course_year),
                                       course_semester=int(course_semester))
        # print(type(course_year), type(course_semester))  # 仍然是str，后续可以放心使用
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

    # print('course_id', course.id)
    print('student_id', student.id, 'course_id', course.id)
    # print(type(student.id), type(course.id))
    # 拿着学生的学号，课程的课号，和评论往数据库中填
    # 找到这条成绩记录
    try:
        score = scoremng.models.Score.objects.get(student_id=student.id, course_id=course.id)
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
# 修改完数据库：已完成
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


# 老师查看他带的某门课还没有提交成绩的学生
# 更改数据库后状态：以完成
def teacher_check_uncommitted_score(request):
    request_json = json.loads(request.body)
    teacher_number = request_json['teacher_number']
    year = request_json['year']
    semester = request_json['semester']
    print(teacher_number, year, semester)  # 成功获得post的数据
    # print(type(year), type(semester))


    try:
        teacher = Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    # 存储老师没有提交成绩的学生
    uncommitted_student_score_list = []

    # 在课表中查看这名老师带的所有的课程
    teacher_course_list = Course.objects.filter(course_year=int(year),
                                                course_semester=int(semester),
                                                course_teacher=teacher.id)

    # 对于这名老师在year学年semester学期带的每一门课
    for teacher_course in teacher_course_list:
        course_id = teacher_course.id
        # print(teacher_course.id)
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

        # 选这门课的学生的列表
        student_course_list = Selection.objects.filter(selection_course_id=course_id)

        for student_course in student_course_list:
            # print(student_course.selection_student_id)
            student_id = student_course.selection_student_id
            # print(student_id)
            # 由学生的名字找到学生的这条记录
            try:
                student = Student.objects.get(id=student_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

            # 由学生的记录找到学生的班级
            banji_id = student.student_banji_id
            try:
                banji = Banji.objects.get(id=banji_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})

            # 尝试用学生的id和课程的id在统计成绩的表格中寻找这条记录，如果没有找到, 说明老师没有提交，需要返回前端
            try:
                score = scoremng.models.Score.objects.get(student_id=student_id,
                                                          course_id=course_id)
            except Exception:
                # 如果进入到except中说明老师没有提交这名学生的记录
                # print(student.id) # 打印出老师没有提交成绩的学生的id
                student_score = {
                                'student_number': student.student_number,
                                'student_name': student.student_name,
                                'student_banji_name': banji.banji_name,
                                'course_name': course.course_name,
                                'course_type': course.course_type,
                                'course_year': course.course_year,
                                'course_semester': course.course_semester,
                                'course_credit': course.course_credit,
                                'course_score': 0,
                            }
                uncommitted_student_score_list.append(student_score)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'uncommitted_student_score_list': uncommitted_student_score_list})


# 老师选择特定的学年和学期，查看学生的成绩
# 目前状态：已完成
# 修改数据库后：已完成
def teacher_check_scores(request):
    request_json = json.loads(request.body)
    teacher_number = request_json['teacher_number']
    year = request_json['year']
    semester = request_json['semester']
    print(teacher_number, year, semester)  # 成功获得post的数据
    # print(type(year), type(semester))

    try:
        teacher = Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    # 这名老师教的所有学生的列表
    student_score_list = []

    # 在课表中查看这名老师带的所有的课程
    teacher_course_list = Course.objects.filter(course_year=int(year),
                                                course_semester=int(semester),
                                                course_teacher=teacher.id)

    # 对于这名老师在year学年semester学期带的每一门课
    for teacher_course in teacher_course_list:
        course_id = teacher_course.id
        # print(teacher_course.id)
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

        # 选这门课的学生的列表
        student_course_list = Selection.objects.filter(selection_course_id=course_id)

        for student_course in student_course_list:
            # print(student_course.selection_student_id)
            student_id = student_course.selection_student_id
            # print(student_id)
            # 由学生的名字找到学生的这条记录
            try:
                student = Student.objects.get(id=student_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

            # 由学生的记录找到学生的班级
            banji_id = student.student_banji_id
            try:
                banji = Banji.objects.get(id=banji_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})

            # 尝试用学生的id和课程的id在统计成绩的表格中寻找这条记录，如果没有找到, 说明老师没有提交，需要返回前端
            try:
                # 如果进入到try语句中表明老师已经提交过这个学生的成绩
                score = scoremng.models.Score.objects.get(student_id=student_id,
                                                          course_id=course_id)
                print('提交过的学生的id', student.id)
                student_score = {
                    'student_number': student.student_number,
                    'student_name': student.student_name,
                    'student_banji_name': banji.banji_name,
                    'course_name': course.course_name,
                    'course_type': course.course_type,
                    'course_year': course.course_year,
                    'course_semester': course.course_semester,
                    'course_credit': course.course_credit,
                    'course_score': score.score,
                }
                student_score_list.append(student_score)
            except Exception:
                # 如果进入到except中说明老师没有提交这名学生的记录
                # print(student.id) # 打印出老师没有提交成绩的学生的id
                print('没有提交过的学生的id', student.id)
                student_score = {
                    'student_number': student.student_number,
                    'student_name': student.student_name,
                    'student_banji_name': banji.banji_name,
                    'course_name': course.course_name,
                    'course_type': course.course_type,
                    'course_year': course.course_year,
                    'course_semester': course.course_semester,
                    'course_credit': course.course_credit,
                    'course_score': 0,
                }
                student_score_list.append(student_score)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'student_score_list': student_score_list})


# 老师下载学生成绩到excel表格中
# 目前状态：已实现
# 修改完数据库：已实现
def teacher_download_scores(request):
    request_json = json.loads(request.body)
    teacher_number = request_json['teacher_number']
    year = request_json['year']
    semester = request_json['semester']
    print(teacher_number, year, semester)  # 成功获得post的数据
    # print(type(year), type(semester))

    # 下载成绩到excel表格中
    wb = xlwt.Workbook(encoding='utf-8')
    w = wb.add_sheet(u'学生成绩', cell_overwrite_ok=True)
    w.write(0, 0, u'学生学号')
    w.write(0, 1, u'学生姓名')
    w.write(0, 2, u'学生所在班级')
    w.write(0, 3, u'课程名称')
    w.write(0, 4, u'课程种类')
    w.write(0, 5, u'课程学年')
    w.write(0, 6, u'课程学期')
    w.write(0, 7, u'课程学分')
    w.write(0, 8, u'课程成绩')
    excel_row = 1

    try:
        teacher = Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    # 在课表中查看这名老师带的所有的课程
    teacher_course_list = Course.objects.filter(course_year=int(year),
                                                course_semester=int(semester),
                                                course_teacher=teacher.id)

    student_score_list = []

    # 对于这名老师在year学年semester学期带的每一门课
    for teacher_course in teacher_course_list:
        course_id = teacher_course.id
        # print(teacher_course.id)
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

        # 选这门课的学生的列表
        student_course_list = Selection.objects.filter(selection_course_id=course_id)

        for student_course in student_course_list:
            # print(student_course.selection_student_id)
            student_id = student_course.selection_student_id
            # print(student_id)
            # 由学生的名字找到学生的这条记录
            try:
                student = Student.objects.get(id=student_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

            # 由学生的记录找到学生的班级
            banji_id = student.student_banji_id
            try:
                banji = Banji.objects.get(id=banji_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})

            # 把这些成绩存放到excel表格中
            w.write(excel_row, 0, student.student_number)
            w.write(excel_row, 1, student.student_name)
            w.write(excel_row, 2, banji.banji_name)
            w.write(excel_row, 3, course.course_name)
            w.write(excel_row, 4, course.course_type)
            w.write(excel_row, 5, course.course_year)
            w.write(excel_row, 6, course.course_semester)
            w.write(excel_row, 7, course.course_credit)

            # 尝试用学生的id和课程的id在统计成绩的表格中寻找这条记录，如果没有找到, 说明老师没有提交，需要返回前端
            try:
                # 如果进入到try语句中表明老师已经提交过这个学生的成绩
                score = scoremng.models.Score.objects.get(student_id=student_id,
                                                          course_id=course_id)
                print('提交过的学生的id', student.id)
                student_score = {
                    'student_number': student.student_number,
                    'student_name': student.student_name,
                    'student_banji_name': banji.banji_name,
                    'course_name': course.course_name,
                    'course_type': course.course_type,
                    'course_year': course.course_year,
                    'course_semester': course.course_semester,
                    'course_credit': course.course_credit,
                    'course_score': score.score,
                }
                w.write(excel_row, 8, score.score)
                student_score_list.append(student_score)
            except Exception:
                # 如果进入到except中说明老师没有提交这名学生的记录
                # print(student.id) # 打印出老师没有提交成绩的学生的id
                print('没有提交过的学生的id', student.id)
                student_score = {
                    'student_number': student.student_number,
                    'student_name': student.student_name,
                    'student_banji_name': banji.banji_name,
                    'course_name': course.course_name,
                    'course_type': course.course_type,
                    'course_year': course.course_year,
                    'course_semester': course.course_semester,
                    'course_credit': course.course_credit,
                    'course_score': 0,
                }
                w.write(excel_row, 8, 0)
                student_score_list.append(student_score)
            excel_row += 1
    exist_file = os.path.exists(teacher.teacher_name + ' ' + year + '年 第' + semester + '学期所带学生的成绩单.xls')
    if exist_file:
        os.remove(teacher.teacher_name + ' ' + year + '年 第' + semester + '学期所带学生的成绩单.xls')
    wb.save(teacher.teacher_name + ' ' + year + '年 第' + semester + '学期所带学生的成绩单.xls')
    return JsonResponse({**error_code.CLACK_SUCCESS, 'student_score_list': student_score_list})


# 老师上传成绩
# 目前状态：已完成
# 修改数据库后：已完成
def teacher_upload(request):
    request_json = json.loads(request.body)
    teacher_number = request_json['teacher_number']
    course_name = request_json['course_name']
    course_credit = request_json['course_credit']
    course_type = request_json['course_type']
    course_year = request_json['course_year']
    course_semester = request_json['course_semester']
    student_number = request_json['student_number']
    student_name = request_json['student_name']
    student_banji_name = request_json['student_banji_name']
    course_score = request_json['course_score']
    # print(course_name, course_credit, course_type, course_year, course_semester, student_number, student_name,
    #       student_banji_name, course_score)  # 成功获得post的数据

    try:
        teacher = Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    # 找到这门课程的id,为了防止有多门同名的课，这里使用filter以保证只能找出一门课
    try:
        course_list = Course.objects.filter(course_name=course_name, course_credit=course_credit,
                                            course_type=course_type, course_teacher=teacher.id,
                                            course_year=course_year, course_semester=course_semester)
        # print(len(course_list))
        course = course_list[0]
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    print('课程名', course.course_name, '课程的id', course.id)

    # 找到班级
    try:
        banji = Banji.objects.get(banji_name=student_banji_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})

    # 通过班级和学号和姓名唯一确定一名学生
    try:
        student = Student.objects.get(student_number=student_number, student_name=student_name,
                                      student_banji_id=banji.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    print('学生的id', student.id)

    # 保存教师提交的学生的成绩
    # 由学生和课程找到含有成绩的记录
    try:
        score = scoremng.models.Score.objects.get(student_id=student.id, course_id=course.id)

        # 修改这条成绩记录中的成绩
        score.score = course_score

        # 把这条成绩记录设为已提交
        score.teacher_upload = True
    except Exception:
        # 如果这名学生之前没有出现成绩表中
        score = scoremng.models.Score(student_id=student.id, course_id=course.id,
                                      score=course_score)

    # 存储到数据库中
    try:
        score.save()
    except Exception:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR})

    # 把剩余没有提交的课返回到前端，采用先在选课表中查看学生是否选课，再在成绩表中查看是否有这名学生的成绩的方法来判断老师是否提交这名学生的成绩
    # 存储老师没有提交成绩的学生
    student_score_list = []

    # 在课表中查看这名老师带的所有的课程
    teacher_course_list = Course.objects.filter(course_year=int(course_year),
                                                course_semester=int(course_semester),
                                                course_teacher=teacher.id)

    # 对于这名老师在year学年semester学期带的每一门课
    for teacher_course in teacher_course_list:
        course_id = teacher_course.id
        # print(teacher_course.id)
        try:
            course = Course.objects.get(id=course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

        # 选这门课的学生的列表
        student_course_list = Selection.objects.filter(selection_course_id=course_id)

        for student_course in student_course_list:
            # print(student_course.selection_student_id)
            student_id = student_course.selection_student_id
            # print(student_id)
            # 由学生的名字找到学生的这条记录
            try:
                student = Student.objects.get(id=student_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

            # 由学生的记录找到学生的班级
            banji_id = student.student_banji_id
            try:
                banji = Banji.objects.get(id=banji_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})

            # 尝试用学生的id和课程的id在统计成绩的表格中寻找这条记录，如果没有找到, 说明老师没有提交，需要返回前端
            try:
                score = scoremng.models.Score.objects.get(student_id=student_id,
                                                          course_id=course_id)
            except Exception:
                # 如果进入到except中说明老师没有提交这名学生的记录
                # print(student.id) # 打印出老师没有提交成绩的学生的id
                student_score = {
                                'student_number': student.student_number,
                                'student_name': student.student_name,
                                'student_banji_name': banji.banji_name,
                                'course_name': course.course_name,
                                'course_type': course.course_type,
                                'course_year': course.course_year,
                                'course_semester': course.course_semester,
                                'course_credit': course.course_credit,
                                'course_score': 0,
                            }
                student_score_list.append(student_score)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'student_score_list': student_score_list})
