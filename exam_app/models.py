from django.db import models


class Exam(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='exams', on_delete=models.CASCADE)


class Quest(models.Model):
    title = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    title = models.ForeignKey(Quest, on_delete=models.CASCADE)
    text = models.TextField()
