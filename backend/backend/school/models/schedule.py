from django.db import models
from django.db.models.fields import TimeField

DAYS_OF_THE_WEEK = [
    ("MONDAY", 'Monday'),
    ("TUESDAY", 'Tuesday'),
    ("WEDNESDAY", 'Wednesday'),
    ("THURSDAY", 'Thursday'),
    ("FRIDAY", 'Friday'),
    ("SATURDAY", 'Saturday'),
    # ("1", 'Monday'),
    # ("2", 'Tuesday'),
    # ("3", 'Wednesday'),
    # ("4", 'Thursday'),
    # ("5", 'Friday'),
    # ("6", 'Saturday'),
]


class DayOfTheWeek(models.Model):
    dayOfTheWeek = models.CharField(max_length=50, choices=DAYS_OF_THE_WEEK)


    def __str__(self):
        return self.dayOfTheWeek

class Time(models.Model):
    time = models.TimeField()

    def __str__(self):
        return self.str(time)

# class Schedule(models.Model):
#     dayOfTheWeek = models.ForeignKey(
#         'DayOfTheWeek',
#         on_delete=models.CASCADE,
#     )
#     time = models.ForeignKey(
#         'Time',
#         on_delete=models.CASCADE,
#     )
#     def __str__(self):
#         return str((self.time, self.dayOfTheWeek))