from rest_framework import generics, permissions

from school.models import Professor
from school.serializers import ProfessorSerializer


class ProfessorList(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = ()


class ProfessorDestroy(generics.DestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class ProfessorUpdate(generics.UpdateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class ProfessorCreate(generics.CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = ()


class ProfessorGet(generics.RetrieveAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = ()
