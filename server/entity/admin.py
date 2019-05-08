from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Classroom)
admin.site.register(models.Department)
admin.site.register(models.Major)
admin.site.register(models.Banji)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Semester)
admin.site.register(models.DateAndClassroom)
admin.site.register(models.Course)
