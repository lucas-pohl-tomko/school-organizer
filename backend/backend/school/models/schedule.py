from django.db import models
from django.db.models.fields import TimeField
from .professor import Professor
from .student import Student

DAYS_OF_THE_WEEK = [
    ("MONDAY", 'Monday'),
    ("TUESDAY", 'Tuesday'),
    ("WEDNESDAY", 'Wednesday'),
    ("THURSDAY", 'Thursday'),
    ("FRIDAY", 'Friday'),
    ("SATURDAY", 'Saturday'),

]


class DayOfTheWeek(models.Model):
    dayOfTheWeek = models.CharField(max_length=50, choices=DAYS_OF_THE_WEEK)

    def __str__(self):
        return self.dayOfTheWeek

class Time(models.Model):

    time = models.TimeField()
    def __str__(self):
        return str(self.time)

class Schedule(models.Model):

    dayOfTheWeek = models.ForeignKey(
        'DayOfTheWeek',
        on_delete=models.CASCADE,
    )
    time = models.ForeignKey(
        'Time',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return str((self.time, self.dayOfTheWeek))
    

class ScheduleStudentProfessor(models.Model):
    schedule = models.ForeignKey(
        'Schedule',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
    )
    professor = models.ForeignKey(
        'Professor',
        on_delete=models.CASCADE,
    )
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ScheduleStudentProfessor'
        verbose_name_plural = 'ScheduleStudentProfessors'
        
    def __str__(self):
        return str((self.student, self.professor, self.schedule))