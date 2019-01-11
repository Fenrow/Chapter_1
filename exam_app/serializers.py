from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Exam, Quest, Answer

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exam
        fields = ('url', 'id', 'title', 'owner')

class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quest
        fields = ('url', 'id', 'title', 'text')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('url', 'id', 'title', 'text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    exams = serializers.HyperlinkedRelatedField(many=True, view_name='exam-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'exams')
