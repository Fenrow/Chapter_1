from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Exam, Quest, Answer
from .serializers import ExamSerializer, QuestSerializer, AnswerSerializer

@csrf_exempt
def exam_list(request):
    if request.method == 'GET':
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def exam(request, exam_id):

    try:
        exam = Exam.objects.get(id=exam_id)
    except Exam.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExamSerializer(exam)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExamSerializer(exam, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        exam.delete()
        return HttpResponse(status=204)
