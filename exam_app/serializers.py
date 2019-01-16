from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Exam, Quest, Answer

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    quests = serializers.HyperlinkedRelatedField(many=True, view_name='quest-detail', read_only=True)

    class Meta:
        model = Exam
        fields = '__all__' #('url', 'id', 'title', 'owner')

class QuestSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    answers = serializers.HyperlinkedRelatedField(many=True, view_name='answer-detail', read_only=True)

    class Meta:
        model = Quest
        fields = '__all__' #('url', 'id', 'title', 'text')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Answer
        fields = '__all__' #('url', 'id', 'title', 'text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    exams = serializers.HyperlinkedRelatedField(many=True, view_name='exam-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'exams', 'quests', 'answers')
