# Create your views here.
import json


import selecourse.models
from django.http import JsonResponse
from entity.models import Student,Banji,Course,Teacher,Classroom,Department,DateAndClassroom
from selecourse.models import Selection,Year_semester
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
        student=Student.objects.get(student_number=student_number)#get返回是objects不能超过2个
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})

    #得到通过学年，学期得到全部的课程信息，初始时由排课系统为每个学生分配选课权限
    try:#filter得到的都是QuerySet类型
        courses = Course.objects.filter(course_semester=semester,course_year=year)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})

    for course in courses:#遍历通过学年和学期过滤得到的所有课程记录
        dateAndclassroom = DateAndClassroom.objects.get(course_id=course.id)
        classroom=Classroom.objects.get(id=dateAndclassroom.classroom_id)
        # student_course=Student_course.objects.get(student_id=student.id,course_id=course.id)
        teacher=Teacher.objects.get(id=course.course_teacher_id)
        department=Department.objects.get(id=course.course_department_id)
        flag=True
        if Selection.objects.filter(selection_student_id=student.id,selection_course_id=course.id).exists():
            flag=False
        course_info = {
                "course_id": course.id,
                "course_name": course.course_name,
                "course_credit": course.course_credit,
                "course_type": course.course_type,
                "classroom_name": classroom.classroom_name,
                "course_year": course.course_year,
                "course_semester": course.course_semester,
                "course_allowance":course.course_allowance,#课程余量
                "course_capacity": course.course_capacity,#课程容量
                "course_teacher": teacher.teacher_name,
                "course_access": flag,
                "course_department": department.department_name,
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

    #通过老师工号获得对应的老师记录
    try:
        teacher=Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    try:
        # 通过老师记录获得老师所教授的全部课程记录
        courses = Course.objects.filter(course_year=year,course_semester=semester,course_teacher_id=teacher.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    for course in courses:
        try:
            #如果课程存在，则获取该指定课程的上课教室
            dateandroom=DateAndClassroom.objects.get(course_id=course.id)
            classroom=Classroom.objects.get(id=dateandroom.classroom_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_CLASSROOM_NOT_EXISTS})
        department=Department.objects.get(id=course.course_department_id)
        type="必修"
        if course.course_type==1:
            type = "选修"
        temp ={
                    "teacher_name":teacher.teacher_name,
                    "course_name": course.course_name,
                    "course_id":course.id,
                    "course_type":type,
                    "course_credit":course.course_credit,
                    "course_allowance":course.course_allowance,#课程余量
                    "course_capacity":course.course_capacity,#课程容量
                    "course_classroom":classroom.classroom_name,
                    "course_department":department.department_name,
                }
        course_student_list.append(temp)
    return JsonResponse({**error_code.CLACK_SUCCESS, 'course_student_list': course_student_list})

#学生选课,在课程信息表中点击有权选但未选的课程进行选课操作
def sele_button(request):
    #通过点击按钮，将学生号和课程号保存到其对应的选课表selection中
    request_json = json.loads(request.body)
    student_number = request_json["student_number"]
    course_id=request_json["course_id"]
    #通过课程id找到对应的课程记录
    try:
        course = Course.objects.get(id=course_id)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    #通过课程course找到其对应的DateAndClassroom信息
    try:
        date_info=DateAndClassroom.objects.get(course_id=course.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_DATEANDCLASSROOM_NOT_EXISTS})
    #通过学生名找到对应的学生记录
    try:
        student=Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    #通过student.id过滤得到该学生所有的选课记录，即所有已选的课程
    seles=Selection.objects.filter(selection_student_id=student.id)
    if seles.count()==0:
        course.course_allowance =course.course_allowance-1  # 课程余量减去1
        try:
            course.save()
        except Exception:
            return JsonResponse({**error_code.CLACK_ALLOWANCE_UPDATE_FAILED})
        sele_cou =Selection(selection_course_id=course.id, selection_student_id=student.id)
        # 存储到数据库中
        try:
            sele_cou.save()
        except Exception:
            return JsonResponse({**error_code.CLACK_SAVE_FAIL})
        return JsonResponse({**error_code.CLACK_SUCCESS})
    else:#判断课程是否出现冲突
        flag=True
        for sele in seles:
            #通过每一条sele得到对应的course
            cou=Course.objects.get(id=sele.selection_course_id)
            #通过得到的课程cou，过滤得到其对应的DateAndClassroom
            date_selected=DateAndClassroom.objects.get(course_id=cou.id)
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
            course.course_allowance = course.course_allowance - 1  # 课程余量减去1
            try:
                course.save()
            except Exception:
              return JsonResponse({**error_code.CLACK_ALLOWANCE_UPDATE_FAILED})
            sele_cou =Selection(selection_course_id=course.id, selection_student_id=student.id)
            # 存储到数据库中
            try:
                sele_cou.save()
            except Exception:
              return JsonResponse({**error_code.CLACK_SAVE_FAIL})
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
        student=Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    try:
        sele=Selection.objects.get(selection_student_id=student.id,selection_course_id=course.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_SELECTION_NOT_EXISTS})
    try:
        sele.delete()  # 删除这条选课记录
    except Exception:
        return JsonResponse({**error_code.CLACK_DELETE_FAIL})

    course.course_allowance=course.course_allowance+1#课程余量加1
    try:
        course.save()
    except Exception:
        return JsonResponse({**error_code.CLACK_ALLOWANCE_UPDATE_FAILED})
    return JsonResponse({**error_code.CLACK_SUCCESS})

#教师下载选课名单
def teacher_download(request):
    # 保存所有课程的选课名单和课程名称
    student_list = []

    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    teacher_number=request_json['teacher_number']
    course_id = request_json['course_id']

    try:
        #通过老师名得到对应的老师记录,默认老师不存在重名
        teacher=Teacher.objects.get(teacher_number=teacher_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})

    # 通过课程名和老师id得到对应的course
    try:
        course = Course.objects.get(id=course_id)
    except Exception:
        return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
    # 在selection中过滤得到
    seles = Selection.objects.filter(selection_course_id=course.id)
    #从得到的选课记录中的selection_student_id过滤得到对应的student_name
    for sele in seles:
        try:
            student = Student.objects.get(id=sele.selection_student_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
        try:
            banji=Banji.objects.get(id=student.student_banji_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_BANJI_NOT_EXISTS})
        temp = {
                "course_name": course.course_name,
                "student_name": student.student_name,
                "student_number": student.student_number,
                "student_banji":banji.banji_name,
                }
        student_list.append(temp)
    if len(student_list)==0:
        return JsonResponse({**error_code.CLACK_DOWNLOAD_FAILED})
    else:
        return JsonResponse({**error_code.CLACK_SUCCESS, 'course_student_list': student_list})


#向管理员提供各类报表
def  admin_reports(request):
    #保存课程容量和已选容量
    reports_list=[]

    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    department_name = request_json['department_name']
    teacher_name=request_json['teacher_name']
    course_name = request_json['course_name']

    #通过学院名获得学院记录
    try:
        department=Department.objects.get(department_name=department_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_DEPARTMENT_NOT_EXISTS})

    try:#默认老师没有重名
        teacher=Teacher.objects.get(teacher_name=teacher_name)
    except Exception:
        return JsonResponse({**error_code.CLACK_TEACHER_NOT_EXISTS})
    try:
        course=Course.objects.get(course_year=year,course_semester=semester,course_name=course_name,course_department_id=department.id,course_teacher_id=teacher.id)
    except Exception:
        return JsonResponse({**error_code.CLACK_DELETE_FAIL})

    info = {
            "course_allowance":course.course_allowance,#课程余量
            "course_capacity": course.course_capacity,#课程容量
            }
    reports_list.append(info)
    if len(reports_list)==0:
        return JsonResponse({**error_code.CLACK_REPORT_FAIL})
    #将课程容量和课程已选人数加入到reports_list中进行返回
    else:
        return JsonResponse({**error_code.CLACK_SUCCESS, 'reports_list': reports_list})

#学生课表查询接口
def course_inquiry(request):
    #保存查询学生的课表信息，即已选的所有课程信息
    course_list=[] #保存课表

    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    student_number = request_json['student_number']
    #通过学生学号获得该学生的记录
    try: #学号唯一
        student=Student.objects.get(student_number=student_number)
    except Exception:
        return JsonResponse({**error_code.CLACK_STUDENT_NOT_EXISTS})
    #通过学生id获得选课表selection中的对应所有记录
    seles=Selection.objects.filter(selection_student_id=student.id)
    for sele in seles: #获取每门课程的所有信息
        try:
            course=Course.objects.get(id=sele.selection_course_id)
        except Exception:
            return JsonResponse({**error_code.CLACK_COURSE_NOT_EXISTS})
        #通过课程记录获得对应的DateAndClassroom
        if year == course.course_year and semester == course.course_semester:
                dateAndclassroom = DateAndClassroom.objects.get(course_id=course.id)
                classroom=Classroom.objects.get(id=dateAndclassroom.classroom_id)
                teacher=Teacher.objects.get(id=course.course_teacher_id)
                type="必修"
                if course.course_type==1:
                    type = "选修"
                course_info = {
                    "course_name": course.course_name,
                    "course_type":type,
                    "course_credit": course.course_credit,
                    "classroom_name": classroom.classroom_name,
                    "course_teacher": teacher.teacher_name,
                    "start_week": dateAndclassroom.start_week,  # 开始周数
                    "end_week": dateAndclassroom.end_week,  # 结束周数
                    "day_of_week": dateAndclassroom.day_of_week,  # 星期几
                    "start": dateAndclassroom.start,  # 开始节数
                    "end": dateAndclassroom.end,  # 结束节数
                }
                course_list.append(course_info)
    if len(course_list)==0:
        return JsonResponse({**error_code.CLACK_TIMETABLE_FAIL})
    else:
        return JsonResponse({**error_code.CLACK_SUCCESS, 'course_list': course_list})

#管理员设置学期学年
def set_year_semester(request):
    #输入year和semester来写入Year_semester表中
    request_json = json.loads(request.body)
    year = request_json['year']
    semester = request_json['semester']
    inital = Year_semester.objects.all()
    if inital.count()==0:
        y_s = Year_semester(year=2016, semester=1)
        y_s.save()
    courses=Course.objects.filter(course_year=year,course_semester=semester)
    if courses.count()==0:
        return  JsonResponse({**error_code.CLACK_SET_YEAR_SEMESTER_FAIL})
    else:
        year_semester = Year_semester.objects.all()
        temp=Year_semester.objects.get(id=year_semester[0].id)
        temp.year=year
        temp.semester=semester
        temp.save()
        return JsonResponse({**error_code.CLACK_SUCCESS})

#管理员查询学期学年
def inquiry_year_semester(request):
    #返回year和semester
    year_semester_list=[]
    year_semester = Year_semester.objects.all()

    if year_semester.count()==0:
        return JsonResponse({**error_code.CLACK_INQUIRY_YEAR_SEMESTER_FAIL})
    else:
        info = {
            "year": year_semester[0].year,  # 学年
            "semester": year_semester[0].semester,  # 学期
        }
        year_semester_list.append(info)
        return JsonResponse({**error_code.CLACK_SUCCESS, 'year_semester_list': year_semester_list})