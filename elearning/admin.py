from django.contrib import admin
from .models import *


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(Students)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'group']
