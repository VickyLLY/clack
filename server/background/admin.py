from django.contrib import admin
from background import models
# Register your models here.

admin.site.register(models.Notice)
admin.site.register(models.TeacherGroup)
admin.site.register(models.AssignGroup)

