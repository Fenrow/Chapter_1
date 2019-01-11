from rest_framework import serializers
from .models import Exam, Quest, Answer

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title')

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'title', 'text')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'title', 'text')
