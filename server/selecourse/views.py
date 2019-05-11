# Create your views here.
import json


import selecourse.models
from django.http import JsonResponse
from entity.models import Student,Student_course, Course,Teacher,Classroom,Department,DateAndClassroom
from selecourse.models import Selection
import entity
from server import error_code

#学生查询选课信息,并且可以选的课程后面会有一个选课按钮对应sele_button
def student_inquiry(request):
    #list保存所有的课程objects
    course_list=[]

    request_json=json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    #通过学生学号来判断查询到的课程是否为已选
    student_number=request_json['student_number']
    #通过学生学号获得对应的学生记录

    try:
        student=Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

    courses_selected = []  # 保存所有已选课程记录
    #通过student中的id字段获得选课表中对应的所有选课信息
    if Selection.objects.filter(selection_student_id=student.id).exists()==False:
        return JsonResponse({**error_code.CLACK_SELECTION_NOT_EXISTS})

    else:
        selected=Selection.objects.filter(selection_student_id=student.id)
        for sele in selected:
            cou=Course.objects.filter(id=sele.selection_course_id)
            courses_selected.append(cou)

    # 得到通过学年，学期得到全部的课程信息，初始时由排课系统分配选课权限,默认应全部为未选且可选
    try:
        temp= Course.objects.filter(course_year=year)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

    try:
        courses= temp.objects.filter( course_semester=semester)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

    for course in courses:#遍历通过学年和学期过滤得到的所有课程记录
            dateAndclassroom = DateAndClassroom.objects.filter(course_id=course.id)
            classroom=Classroom.objects.filter(id=dateAndclassroom.classroom_id)
            temp=Student_course.objects.filter(student_id=student.id)
            student_course=temp.objects.filter(course_id=course.id)
            if course in courses_selected: #表明该课程为已选
                course.course_access="已选"
            course_info = {
                "course_name": course.course_name,
                "course_credit": course.course_credit,
                "course_type": course.course_type,
                "classroom_name": classroom.classroom_name,
                "course_year": course.course_year,
                "course_semester": course.course_semester,
                "course_capacity": course.course_capacity,
                "course_teacher": course.course_teacher,
                "course_access": student_course.course_access,
                "course_department": course.course_department,
                "course_allowance":course.course_allowance,#课程余量
                "start_week":dateAndclassroom.start_week,#开始周数
                "end_week":dateAndclassroom.end_week,#结束周数
                "day_of_week":dateAndclassroom.day_of_week, #星期几
                "start":dateAndclassroom.start, #开始节数
                "end":dateAndclassroom.end, #结束节数
            }
            course_list.append(course_info)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'course_list': course_list})

#老师查询选课情况
def teacher_inquiry(request):
    # list保存所有的课程名和对应的选课学生名objects
    course_student_list = []

    request_json=json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    teacher_number = request_json['teacher_number']
    course_name = request_json['course_name']

    #通过老师工号获得对应的老师记录
    try:
        teacher=Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    course_list=[]#保存老师要查询的指定课程
    try:
        # 通过老师记录获得老师所教授的课程
        courses = Course.objects.filter(course_teacher_id=teacher.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

    for course in courses:
        # 通过学年、学期和课程名筛选课程，最后得到一条符合要求的课程
        if course.course_name==str(course_name) and year == str(course.course_year) and semester == str(course.course_semester):
            course_list.append(course)
    if len(course_list)==0:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    else:
        try:
            #如果课程存在，则获取该指定课程的上课教室
            dateandroom=DateAndClassroom.objects.filter(course_id=course_list[0].id)
            classroom=Classroom.objects.filter(id=dateandroom.classroom_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_CLASSROOM_NOT_EXISTS})

        #在selection中通过课程id过滤得到对应的学生
        seles=Selection.objects.filter(selection_course_id=course_list[0].id)
        for sele in seles:
            #通过选课表中的记录过滤的到学生记录
            try:
                student=Student.objects.filter(id=sele.selection_student_id)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
            temp ={
                "student_name": student.student_name,
                "student_number": student.student_number,
                 "course_name":course_list[0].course_name,
                 "classroom_name":classroom.classroom_name,
                 "course_credit":course_list[0].course_credit,
                 "course_allowance":course_list[0].course_allowance,#课程余量
                 "course_capacity":course_list[0].course_capacity,#课程容量
                }
            course_student_list.append(temp)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'course_student_list': course_student_list})

#将可以选的课程加入到该学生对应的已选课表中
def add_course(course,student):
    sele_cou=selecourse.models.Selection(selection_course_id=course.id,seletion_student_id=student.id)
    # 存储到数据库中
    try:
        sele_cou.save()
        return JsonResponse({**error_code.CLACK_SUCCESS})
    except Exception:
        return JsonResponse({**error_code.CLACK_SAVE_FAIL})

#学生选课,在课程信息表中点击有权选但未选的课程进行选课操作
def sele_button(request):
    #通过点击按钮，将学生号和课程号保存到其对应的选课表selection中
    request_json = json.loads(request.body)
    course_id=request_json["course_id"]
    student_number=request_json["student_number"]
    #通过课程id找到对应的课程记录
    try:
        course = Course.objects.get(id=course_id)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    #通过课程course找到其对应的DateAndClassroom信息
    try:
        date_info=DateAndClassroom.objects.filter(course_id=course.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_DATEANDCLASSROOM_NOT_EXISTS})
    #通过学生名找到对应的学生记录
    try:
        student=Student.objects.filter(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    #通过student.id过滤得到该学生所有的选课记录，即所有已选的课程
    seles=Selection.objects.filter(selection_student_id=student.id)
    #判断课程是否出现冲突
    flag=True
    for sele in seles:
        #通过每一条sele得到对应的course
        cou=Course.objects.filter(id=sele.selection_course_id)
        #通过得到的课程cou，过滤得到其对应的DateAndClassroom
        date_selected=DateAndClassroom.objects.filter(course_id=cou.id)
        if date_info.start_week <= date_selected.end_week and date_info.end_week >=date_selected.start_week:
            #表示周数有交叉
            if date_info.day_of_week==date_selected.day_of_week:
                #表示一周之内的星期有交叉
                if date_info.start <= date_selected.end and date_info.end >=date_selected.start:
                    #一天之内上课节数有交叉
                    flag=False #此时表明课程发生了冲突
        if flag==False:
            break
    if flag and course.course_allowance>0:
        #如果无冲突且课程余量不为0，则执行加入课程操作
        course.course_access="已选"
        course.course_allowance=course.course_allowance-1#课程余量减去1
        add_course(course,student)
        return JsonResponse({**error_code.CLACK_SUCCESS})
    else: #选课失败
        return JsonResponse({**error_code.CLACK_SELECTION_FAIL})

#学生在课程信息表中点击已选的课程后面的删除按钮进行删除选课操作
def dele_button(request):
    #通过点击按钮，将对应的学生号和课程号记录从选课表selection中删除
    request_json = json.loads(request.body)
    course_id=request_json["course_id"]
    student_number=request_json["student_number"]
    #通过课程名找到对应的课程记录
    try:
        course = Course.objects.get(id=course_id)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    #通过学生名找到对应的学生记录
    try:
        student=Student.objects.filter(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    #通过student.id过滤得到该学生所有的选课记录，即所有已选的课程
    seles=Selection.objects.filter(selection_student_id=student.id)
    #通过course_name在该名学生的所有选课记录中找到指定要删除的课程记录
    try:
        sele=seles.objects.filter(selection_course_id=course.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_SELECTION_NOT_EXISTS})
    try:
        sele.delete()#删除这条选课记录
        course.course_allowance=course.course_allowance+1#课程余量加1
        return JsonResponse({**error_code.CLACK_SUCCESS})
    except Exception:
        return JsonResponse({**error_code.CLACK_DELETE_FAIL})

#教师下载选课名单
def teacher_download(request):
    # 保存所有课程的选课名单和课程名称
    student_list = []

    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    course_name = request_json['course_name']

    # 通过课程名得到对应的course
    try:
        course = Course.objects.get(course_name=course_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    # 通过学年和学期筛选对应的课程
    if year == str(course.course_year) and semester == str(course.course_semester):
        # 在selection中过滤得到
        seles = Selection.objects.filter(selection_course_id=course.id)

        #从得到的选课记录中的selection_student_id过滤得到对应的student_name
        for sele in seles:
            try:
                student = Student.objects.filter(id=sele.selection_student_id)
                temp = {
                    "course_name": course.course_name,
                    "student_name": student.student_name,
                    "student_number": student.student_number,
                }
                student_list.append(temp)
            except Exception:
                return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
        return JsonResponse({**error_code.CLACK_SUCCESS, 'course_student_list': student_list})
    else:
        return JsonResponse({**error_code.CLACK_DOWNLOAD_FAILED})

#向管理员提供各类报表
def  admin_reports(request):
    #保存课程容量和已选容量
    reports_list=[]

    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    department_name = request_json['course_department']
    teacher_name=request_json['teacher_name']
    course_name = request_json['course_name']

    #通过学院名获得学院记录
    try:
        department=Department.objects.get(department_name=department_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_DEPARTMENT_NOT_EXISTS})

    #通过学院记录得到对应的课程记录  1.学院名过滤
    temp=Course.objects.filter(course_deaprtment_id=department.id)

    #通过teacher_name得到对应老师的课程记录
    try:
        teacher=Teacher.objects.filter(teacher_name=teacher_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    #通过teacher.id得到对应老师教授的课程记录 2.老师名过滤
    temp1=temp.objects.filter(course_teacher_id=teacher.id)

    # 通过老师对应的课程和课程名记录得到对应的course  3.课程名过滤
    try:
        course = temp1.objects.filter(course_name=course_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    # 通过学年和学期筛选对应的课程 4.学年学期过滤
    if year == str(course.course_year) and semester == str(course.course_semester):
        reports_list.append(course.course_capacity)#课程容量
        reports_list.append(course.course_allowance) #课程余量
    #将课程容量和课程已选人数加入到reports_list中进行返回
    return JsonResponse({**error_code.CLACK_SUCCESS, 'reports_list': reports_list})

#学生课表查询接口
def course_inquiry(request):
    #保存查询学生的课表信息，即已选的所有课程信息
    timetable=[] #课表

    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    student_number = request_json['student_number']
    #通过学生学号获得该学生的记录
    try:
        student=Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    #通过学生id获得选课表selection中的对应所有记录
    seles=Selection.objects.filter(selection_student_id=student.id)
    for sele in seles: #获取每门课程的所有信息
        course=Course.objects.filter(id=sele.selection_course_id)
        #通过课程记录获得对应的DateAndClassroom
        if year == str(course.course_year) and semester == str(course.course_semester):
                dateAndclassroom = DateAndClassroom.objects.filter(course_id=course.id)
                classroom=Classroom.objects.filter(id=dateAndclassroom.classroom_id)
                course_info = {
                    "course_name": course.course_name,
                    "course_credit": course.course_credit,
                    "classroom_name": classroom.classroom_name,
                    "course_teacher": course.course_teacher,
                    "start_week": dateAndclassroom.start_week,  # 开始周数
                    "end_week": dateAndclassroom.end_week,  # 结束周数
                    "day_of_week": dateAndclassroom.day_of_week,  # 星期几
                    "start": dateAndclassroom.start,  # 开始节数
                    "end": dateAndclassroom.end,  # 结束节数
                }
                timetable.append(course_info)
        return JsonResponse({**error_code.CLACK_SUCCESS, 'course_list': timetable})