from rest_framework import generics, permissions

from school.models import ScheduleStudentProfessor, Time, DayOfTheWeek, Schedule
from school.serializers import *

class DayOfTheWeekList(generics.ListAPIView):
    queryset = DayOfTheWeek.objects.all()
    serializer_class = DayOfTheWeekSerializer
    permission_classes = ()

class TimeList(generics.ListAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = ()

class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = ()

class ScheduleStudentProfessorList(generics.ListAPIView):
    queryset = ScheduleStudentProfessor.objects.all()
    serializer_class = ScheduleStudentProfessorSerializer
    permission_classes = ()

class ScheduleStudentProfessorIdList(generics.ListAPIView):
    queryset = ScheduleStudentProfessor.objects.all()
    serializer_class = ScheduleStudentProfessorIdSerializer
    permission_classes = ()

class ScheduleStudentProfessorDestroy(generics.DestroyAPIView):
    queryset = ScheduleStudentProfessor.objects.all()
    serializer_class = ScheduleStudentProfessorSerializer
    permission_classes = ()

class ScheduleStudentProfessorUpdate(generics.UpdateAPIView):
    queryset = ScheduleStudentProfessor.objects.all()
    serializer_class = ScheduleStudentProfessorSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class ScheduleStudentProfessorCreate(generics.CreateAPIView):
    queryset = ScheduleStudentProfessor.objects.all()
    serializer_class = ScheduleStudentProfessorCreateSerializer
    permission_classes = ()


class ScheduleStudentProfessorGet(generics.RetrieveAPIView):
    queryset = ScheduleStudentProfessor.objects.all()
    serializer_class = ScheduleStudentProfessorSerializer
    permission_classes = ()





