from django.db import models
from django.db.models.fields import TimeField

DAYS_OF_THE_WEEK = [
    ("MONDAY", 'Monday'),
    ("TUESDAY", 'Tuesday'),
    ("WEDNESDAY", 'Wednesday'),
    ("THURSDAY", 'Thursday'),
    ("FRIDAY", 'Friday'),
    ("SATURDAY", 'Saturday'),
]


class Schedule(models.Model):
    horary = models.TimeField()
    dayOfTheWeek = models.CharField(max_length=50, choices=DAYS_OF_THE_WEEK)


    def __str__(self):
        return str(self.horary) + ' ' + self.dayOfTheWeek