from django.db import transaction
from rest_framework import serializers
from school.models import (Student,Professor,StudentProfessor)



class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'middle_name', 'last_name')
    
    @transaction.atomic
    def create(self, validated_data):
        professor = Professor.objects.create(**validated_data)
        professor.save()
        return professor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'middle_name', 'last_name','professors')
    @transaction.atomic
    def create(self, validated_data):

        student = Student.objects.create(**validated_data)
        if "professors" in self.initial_data:
            professors = self.initial_data.get("professors")
            for professor in professors:
                professor_id = professor.get("professor")
                role = professor.get("role")
                professor_instance = Professor.objects.get(pk=professor_id)
                StudentProfessor(student=student, professor=professor_instance, role=role).save()
        student.save()
        return student