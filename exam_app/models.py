from django.db import models


class Exam(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(
        'auth.User',
        related_name='exams',
        on_delete=models.CASCADE
        )

class Quest(models.Model):
    text = models.TextField()
    exam = models.ForeignKey(
        Exam,
        related_name='quests',
        on_delete=models.CASCADE
        )

    owner = models.ForeignKey(
        'auth.User',
        related_name='quests',
        on_delete=models.CASCADE
        )


class Answer(models.Model):
    text = models.TextField()
    quest = models.ForeignKey(
        Quest,
        related_name='answers',
        on_delete=models.CASCADE
        )

    owner = models.ForeignKey(
        'auth.User',
        related_name='answers',
        on_delete=models.CASCADE
        )

    result = models.IntegerField()
