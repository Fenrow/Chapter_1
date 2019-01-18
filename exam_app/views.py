from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from django.shortcuts import redirect

from .models import Exam, Quest, Answer
from .serializers import ExamSerializer, QuestSerializer, AnswerSerializerUser, UserSerializer
from .permissions import IsOwnerOrReadOnly

class Exam_list(generics.ListCreateAPIView):
    """A list of all Exams"""

    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Exam_detail(generics.RetrieveUpdateDestroyAPIView):
    """A single Exam"""

    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    """A List of all users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """A single user detail"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestList(generics.ListCreateAPIView):

    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class AnswerList(generics.ListCreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializerUser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializerUser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializer):
        if serializer.get_owner() == serializer.get_quest_owner():
            serializer.save(result=self.request.data['result'])
        else:
            return None


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'exams': reverse('exam-list', request=request, format=format),
        'quest': reverse('quest-list', request=request, format=format),
        'answer': reverse('answer-list', request=request, format=format),
    })
