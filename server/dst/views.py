from django.shortcuts import render
from django.http import JsonResponse,Http404, StreamingHttpResponse
from django.utils import timezone
from server import error_code
import json
import  os
import entity.models
import dst.models
from server.decorators import admin_required,login_required


# Create your views here.

@login_required
def new_dst(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    tnum=user.user_teacher_id
    dst = entity.models.DissertationTopic(
        dissertation_title=request_json['dissertation']['dissertation_title'],
        dissertation_content=request_json['dissertation']['dissertation_content'],
        dissertation_requirement=request_json['dissertation']['dissertation_requirement'],
        dissertation_capacity=request_json['dissertation']['dissertation_capacity'],
        dissertation_tnum_id=tnum,
    )
    try:
        dst.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

@login_required
def stu_select(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    snum=user.user_student_id
    check_result = dst.models.Application.objects.filter(student_id=snum)
    if check_result.exists():
            return  JsonResponse({**error_code.CLACK_STUDENT_SELECT_DST_EXISTS})
    stu_select_dst = dst.models.Application(
        dissertation_id=request_json['dissertation_id'],
        student_id=snum,
    )
    try:
        stu_select_dst.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

@login_required
def dst_list(request):
    request_json = json.loads(request.body)
    dsts = entity.models.DissertationTopic.objects.all()
    result_list = []
    for dst in dsts:
        tname=list(entity.models.Teacher.objects.filter(id=dst.dissertation_tnum_id))
        tt=tname[0]
        result_list_te = [{
            'dissertation_id': dst.id,
            'dissertation_title': dst.dissertation_title,
            'dissertation_content': dst.dissertation_content,
            'dissertation_requirement': dst.dissertation_requirement,
            'dissertation_capacity': dst.dissertation_capacity,
            'dissertation_approval': dst.dissertation_approval,
            'dissertation_pub_time': dst.dissertation_pub_time,
            'dissertation_teacher': tt.teacher_name,
        } ]
        result_list = result_list + result_list_te

    return JsonResponse({**error_code.CLACK_SUCCESS, 'dst_list': result_list})

@login_required
def dst_list_approval(request):
    request_json = json.loads(request.body)
    dsts = entity.models.DissertationTopic.objects.filter(dissertation_approval=True)
    result_list=[]
    for dst in dsts:
        tname=list(entity.models.Teacher.objects.filter(id=dst.dissertation_tnum_id))
        tt=tname[0]
        result_list_te = [{
            'dissertation_id': dst.id,
            'dissertation_title': dst.dissertation_title,
            'dissertation_content': dst.dissertation_content,
            'dissertation_requirement': dst.dissertation_requirement,
            'dissertation_capacity': dst.dissertation_capacity,
            'dissertation_pub_time': dst.dissertation_pub_time,
            'dissertation_teacher': tt.teacher_name,
        } ]
        result_list = result_list + result_list_te

    return JsonResponse({**error_code.CLACK_SUCCESS, 'dst_list': result_list})

@login_required
def teacher_dst_list(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    tnum = user.user_teacher_id
    dsts = entity.models.DissertationTopic.objects.filter(dissertation_tnum_id=tnum)
    result_list = [{
        'dissertation_id': dst.id,
        'dissertation_title': dst.dissertation_title,
        'dissertation_content': dst.dissertation_content,
        'dissertation_requirement': dst.dissertation_requirement,
        'dissertation_capacity': dst.dissertation_capacity,
        'dissertation_approval':dst.dissertation_approval,
        'dissertation_pub_time':dst.dissertation_pub_time,
    } for dst in dsts]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'teacher_dst_list': result_list})

@login_required
def stu_dst_list(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    snum = user.user_student_id
    dd=dst.models.Determination.objects.filter(student_id=snum)
    tnum=dd[0].dissertation_id
    dsts = entity.models.DissertationTopic.objects.filter(id=tnum)
    tname = list(entity.models.Teacher.objects.filter(id=dsts[0].dissertation_tnum_id))
    tt = tname[0]
    result_list = [{
        'dissertation_id': dsta.id,
        'dissertation_title': dsta.dissertation_title,
        'dissertation_content': dsta.dissertation_content,
        'dissertation_requirement': dsta.dissertation_requirement,
        'dissertation_capacity': dsta.dissertation_capacity,
        'dissertation_pub_time': dsta.dissertation_pub_time,
        'dissertation_teacher': tt.teacher_name,
    } for dsta in dsts]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'stu_dst_list': result_list})

@login_required
def stu_view_dst(request):
    request_json = json.loads(request.body)
    dstid=request_json['dissertation_id']
    dsts = entity.models.DissertationTopic.objects.filter(id=dstid)
    tname = list(entity.models.Teacher.objects.filter(id=dsts[0].dissertation_tnum_id))
    tt = tname[0]
    result_list = [{
        'dissertation_id': dsta.id,
        'dissertation_title': dsta.dissertation_title,
        'dissertation_content': dsta.dissertation_content,
        'dissertation_requirement': dsta.dissertation_requirement,
        'dissertation_capacity': dsta.dissertation_capacity,
        'dissertation_pub_time': dsta.dissertation_pub_time,
        'dissertation_teacher': tt.teacher_name,
    } for dsta in dsts]
    return JsonResponse({**error_code.CLACK_SUCCESS, 'stu_dst_list': result_list})

# 老师查看已发布的课题信息
@login_required
def view_published_dissertation(request):
    request_json = json.loads(request.body)
    tid = entity.models.Teacher.objects.get(teacher_number=request_json['teacher_number'])
    result = entity.models.DissertationTopic.objects.filter(dissertation_tnum=tid)
    rlist = []
    # 获取当前时间
    time = timezone.now()
    lenth = len(result)
    for i in range(lenth):
        if result[i].dissertation_pub_time.year == time.year:
            temp = {
                'dissertation_id': result[i].id,
                'dissertation_title': result[i].dissertation_title,
                'dissertation_capacity': result[i].dissertation_capacity,
                'dissertation_pub_time': result[i].dissertation_pub_time,
                'dissertation_approval': result[i].dissertation_approval
            }
            rlist.append(temp)
    return JsonResponse({'rlist': rlist})

# 老师在修改时默认显示的是上一次发布的课题全部信息
@login_required
def view_detail(request):
    request_json = json.loads(request.body)
    result = entity.models.DissertationTopic.objects.filter(id=request_json['dissertation_id'])
    dlist = [{
        'dissertation_id': result[0].id,
        'dissertation_title': result[0].dissertation_title,
        'dissertation_content': result[0].dissertation_content,
        'dissertation_requirement': result[0].dissertation_requirement,
        'dissertation_capacity': result[0].dissertation_capacity,
        'dissertation_pub_time': result[0].dissertation_pub_time,
        'dissertation_approval': result[0].dissertation_approval,
        'dissertation_tnum':result[0].dissertation_tnum_id
    }]
    return JsonResponse({'dlist': dlist})

# 老师修改课题
@login_required
def change_dst(request):
    request_json = json.loads(request.body)

    new_title = request_json['dissertation_title']
    new_content = request_json['dissertation_content']
    new_requirement = request_json['dissertation_requirement']
    new_capacity = request_json['dissertation_capacity']
    new_time = request_json['dissertation_pub_time']

    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_title=new_title)
    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_content=new_content)
    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_requirement=new_requirement)
    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_capacity=new_capacity)
    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_pub_time=new_time)
    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_approval=False)

    return JsonResponse({**error_code.CLACK_SUCCESS})

# 管理员审核课题
@admin_required
def dst_approval(request):
    request_json = json.loads(request.body)

    entity.models.DissertationTopic.objects.filter(id=request_json["dissertation_id"]).update(dissertation_approval=True)

    return JsonResponse({**error_code.CLACK_SUCCESS})

# 教师查看某课题的选择情况
@login_required
def view_selected(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    tnum = user.user_teacher_id
    dsts = entity.models.DissertationTopic.objects.filter(dissertation_tnum_id=tnum)
    result_list = []
    for dsd in dsts:
        tname = list(dst.models.Application.objects.filter(id=dsd.dissertation_tnum_id))
        result_list_te = [{
            'title': dsd.dissertation_title,
            'fixed_capacity': dsd.dissertation_capacity,
            'now_capacity': len(tname),
        }]
        result_list = result_list + result_list_te

    return JsonResponse({**error_code.CLACK_SUCCESS, 'view_list': result_list})


# 教师查看所有选择该课题的学生
@login_required
def view_student(request):
    request_json = json.loads(request.body)
    dsts = dst.models.Application.objects.filter(dissertation_id=request_json['dissertation_id'])
    result_list = []
    for dsd in dsts:
        stu_number = dsd.student_id
        m = entity.models.Student.objects.filter(id=stu_number)
        name = m[0].student_name
        banji = m[0].student_banji.id
        major_n = entity.models.Banji.objects.filter(id=banji)
        major_num = major_n[0].id
        mmm = entity.models.Banji.objects.filter(id=major_num)
        major = mmm[0].banji_major.major_name
        result_list_te = [{
            'student_number': stu_number,
            'student_name': name,
            'major_name': major,
        }]
        result_list = result_list + result_list_te
    return JsonResponse({'stu_list': result_list})

# 教师上传学生论文的成绩和评语
@login_required
def upload_score(request):
    request_json = json.loads(request.body)
    snum = request_json['student_number']
    stu = entity.models.Student.objects.filter(student_number=snum)
    sid=stu[0].id
    sc = dst.models.Grade(
        grade_dissertation_id=request_json['dissertation_id'],
        grade_student_id=sid,
        grade_grade=request_json['score'],
        grade_comment=request_json['comment']
    )
    try:
        sc.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})

# 教师下载学生的论文文件
@login_required
def download(request):
    request_json = json.loads(request.body)
    try:
        response = StreamingHttpResponse(open(request_json["file_path"], 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(request_json["file_path"])
        return response
    except Exception:
            raise Http404

# 教师确定选题学生
@login_required
def define_stu(request):
    request_json = json.loads(request.body)
    dnum = request_json['dissertation_number']
    snum = request_json['student_number']
    temp = dst.models.Determination(
        dissertation_id=dnum,
        student_id=snum,
    )
    try:
        temp.save()
    except Exception as e:
        return JsonResponse({**error_code.CLACK_UNEXPECTED_ERROR, "exception": str(e)})
    return JsonResponse({**error_code.CLACK_SUCCESS})


@login_required
def everyyear_dst(request):
    request_json = json.loads(request.body)
    tid = entity.models.Teacher.objects.get(teacher_number=request_json["teacher_number"])
    result = entity.models.DissertationTopic.objects.filter(dissertation_tnum=tid)
    rlist = []
    # 获取当前时间
    lenth = len(result)
    for i in range(lenth):
        temp = {
            'dissertation_id': result[i].id,
            'dissertation_title': result[i].dissertation_title,
            'dissertation_capacity': result[i].dissertation_capacity,
            'dissertation_pub_time': result[i].dissertation_pub_time,
            'dissertation_approval': result[i].dissertation_approval
        }
        rlist.append(temp)
    return JsonResponse({'rlist': rlist})

@login_required
def select_dst_teacher_name(request):
    request_json = json.loads(request.body)
    qq = entity.models.Teacher.objects.filter(teacher_name=request_json['teacher_name'])
    query_result = list(qq)
    m = 0
    result_list1 = []
    for i in query_result:
        teacher = query_result[m]
        tnum = teacher.id
        dsts = entity.models.DissertationTopic.objects.filter(dissertation_tnum_id=tnum)
        result_list = []
        for dst in dsts:
            result_list = [{
                'dissertation_id': dst.id,
                'dissertation_title': dst.dissertation_title,
                'dissertation_content': dst.dissertation_content,
                'dissertation_requirement': dst.dissertation_requirement,
                'dissertation_capacity': dst.dissertation_capacity,
                'dissertation_approval': dst.dissertation_approval,
                'dissertation_tnum_id': dst.dissertation_tnum_id,
                'teacher_name': teacher.teacher_name,
            }]
            if(dst.dissertation_approval==True):
                result_list1 = result_list1 + result_list
        m = m + 1
    return JsonResponse({**error_code.CLACK_SUCCESS, 'select_dst_teacher_name_list': result_list1})


@login_required
def select_dst_dst_title(request):
    request_json = json.loads(request.body)
    dsts = entity.models.DissertationTopic.objects.filter(dissertation_title__icontains=request_json['dissertation_title'])
    result_list1 = []
    for dst in dsts:
        tt = entity.models.Teacher.objects.filter(id=dst.dissertation_tnum_id)
        ss = list(tt)
        result_list = [{
            'dissertation_id': dst.id,
            'dissertation_title': dst.dissertation_title,
            'dissertation_content': dst.dissertation_content,
            'dissertation_requirement': dst.dissertation_requirement,
            'dissertation_capacity': dst.dissertation_capacity,
            'dissertation_approval': dst.dissertation_approval,
            'dissertation_tnum_id': dst.dissertation_tnum_id,
            'teacher_name': ss[0].teacher_name,
        }]
        if(dst.dissertation_approval==True):
            result_list1 = result_list1 + result_list
    return JsonResponse({**error_code.CLACK_SUCCESS, 'select_dst_dst_title': result_list1})

@login_required
def upload_file(request):
    if request.method == "POST":
        File = request.FILES.get("myfile", None)
        if File is None:
            return JsonResponse({**error_code.CLACK_DISSERTATION_UPLOAD_FILE_FAILED})
        else:
            with open("./dst/uploads_file/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            request_json = json.loads(request.body)
            query_result = list(entity.models.User.objects.filter(user_name=request_json['user_name']))
            user = query_result[0]
            snum = user.user_student_id
            pp = dst.models.DissertationFile(
                student_id = snum,
                dissertation_file_path = "./dst/uploads_file/%s" % File.name
            )
            try:
                pp.save()
            except Exception as e:
                return JsonResponse({**error_code.CLACK_DISSERTATION_UPLOAD_FILE_FAILED})
            return JsonResponse({**error_code.CLACK_SUCCESS})
    else:
        return JsonResponse({**error_code.CLACK_POST_REQUIRED})

@login_required
def stu_view_grade(request):
    request_json = json.loads(request.body)
    query_result = list(
        entity.models.User.objects.filter(user_name=request_json['user_name']))
    user = query_result[0]
    snum=user.user_student_id
    result = dst.models.Grade.objects.filter(grade_student=snum)
    res=result[0]
    result_list = [{
        'grade': res.grade_grade,
        'comment': res.grade_comment,
    }]
    return JsonResponse({**error_code.CLACK_SUCCESS,'stu_view_grade': result_list})