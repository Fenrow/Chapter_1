from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Exam, Quest, Answer

class ExamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exam
        fields = ('id', 'title', 'owner')

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'title', 'text')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'title', 'text')

class UserSerializer(serializers.ModelSerializer):
    exams = serializers.PrimaryKeyRelatedField(many=True, queryset=Exam.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'exams')
