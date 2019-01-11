from rest_framework import generics

from .models import Exam, Quest, Answer
from .serializers import ExamSerializer, QuestSerializer, AnswerSerializer

class Exam_list(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class Exam_instance(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
