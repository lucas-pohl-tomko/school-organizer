from django.db import models
from django.db.models.fields import DateTimeField

from .professor import Professor
from .schedule import ScheduleStudentProfessor

ROLE_PROFESSOR = [
    (0, 'Guitarra/Violao'),
    (1, 'Violino'),
    (2, 'Sopro'),
    (3, 'Piano/Teclado')
]

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)    

    professors = models.ManyToManyField(
        'Professor',
        related_name='students',
        through='ScheduleStudentProfessor'
    )
    
    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

class StudentProfessor(models.Model):
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
    )
    professor = models.ForeignKey(
        'Professor',
        on_delete=models.CASCADE,
    )
    role = models.IntegerField(choices=ROLE_PROFESSOR)

    def __str__(self):
        return str((self.student, self.professor, self.role))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'StudentProfessor'
        verbose_name_plural = 'StudentProfessors'