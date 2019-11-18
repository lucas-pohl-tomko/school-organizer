from django.contrib import admin

from .models import Student,Professor, StudentProfessor,DayOfTheWeek,Time

admin.site.register(Student)
admin.site.register(StudentProfessor)
admin.site.register(Professor)
# admin.site.register(Schedule)
admin.site.register(DayOfTheWeek)
admin.site.register(Time)