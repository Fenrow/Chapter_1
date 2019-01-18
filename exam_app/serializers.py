from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Exam, Quest, Answer

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    quests = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='quest-detail',
        read_only=True
        )

    class Meta:
        model = Exam
        fields = ('url', 'owner', 'title', 'quests')

class QuestSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    answers = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='answer-detail',
        read_only=True
        )

    class Meta:
        model = Quest
        fields = ('url', 'owner', 'text', 'answers')

class AnswerSerializerUser(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    quest_owner = serializers.ReadOnlyField(source='quest.owner.username')
    result = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = ('url', 'text', 'owner', 'quest_owner', 'result')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    exams = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='exam-detail',
        read_only=True
        )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'exams', 'quests', 'answers')
