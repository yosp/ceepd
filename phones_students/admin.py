from django.contrib import admin
from models import *
from django.contrib.admin import ModelAdmin

class phoneAdm(admin.ModelAdmin):
	list_display = ('phone','student_id')

admin.site.register(Phone_Student, phoneAdm)