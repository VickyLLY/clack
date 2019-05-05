from django.contrib import admin
from dst import models

# Register your models here.

admin.site.register(models.Application)
admin.site.register(models.Determination)
admin.site.register(models.File)
admin.site.register(models.Grade)
admin.site.register(models.Review)
