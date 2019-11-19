from rest_framework import generics, permissions

from school.models import ScheduleStudentProfessor, Time, DayOfTheWeek, Schedule
from school.serializers import ScheduleStudentProfessorSerializer, ScheduleSerializer,TimeSerializer,DayOfTheWeekSerializer

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

