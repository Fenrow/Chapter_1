from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Exam, Quest, Answer
from .serializers import ExamSerializer, QuestSerializer, AnswerSerializer

class Exam_list(APIView):
    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Exam_instance(APIView):
    def get_object(self, exam_id):
        try:
            return Exam.objects.get(id=exam_id)
        except Exam.DoesNotExist:
            return Http404

    def get(self, request, exam_id, format=None):
        exam = self.get_object(exam_id)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

    def put(self, request, exam_id, format=None):
        exam = self.get_object(exam_id)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, exam_id, format=None):
        exam = self.get_object(exam_id)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
