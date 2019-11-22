from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'students/$', StudentList.as_view()),
    url(r'students/(?P<pk>\d+)/$', StudentDestroy.as_view()),
    url(r'students/add/$', StudentCreate.as_view()),
    url(r'students/get/(?P<pk>\d+)/$', StudentGet.as_view()),
    url(r'students/edit/(?P<pk>\d+)/$', StudentUpdate.as_view()),
    url(r'professors/$', ProfessorList.as_view()),
    url(r'professors/(?P<pk>\d+)/$', ProfessorDestroy.as_view()),
    url(r'professors/add/$', ProfessorCreate.as_view()),
    url(r'professors/get/(?P<pk>\d+)/$', ProfessorGet.as_view()),
    url(r'professors/edit/(?P<pk>\d+)/$', ProfessorUpdate.as_view()),
    url(r'schedulestudentsprofessor/$', ScheduleStudentProfessorList.as_view()),
    url(r'schedulestudentsprofessorid/$', ScheduleStudentProfessorIdList.as_view()),
    url(r'schedules/$', ScheduleList.as_view()),
    url(r'time/$', TimeList.as_view()),
    url(r'dayoftheweek/$', DayOfTheWeekList.as_view()),

]
