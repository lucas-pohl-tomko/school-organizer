from django.contrib import admin

from .models import Student,Professor, StudentProfessor, Schedule

admin.site.register(Student)
admin.site.register(StudentProfessor)
admin.site.register(Professor)
admin.site.register(Schedule)