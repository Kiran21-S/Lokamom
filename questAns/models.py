from django.db import models # type: ignore
from django.urls import reverse # type: ignore
 # type: ignore
from django.utils.timezone import now # type: ignore

from datetime import datetime
# Create your models here.

class Question(models.Model):
    time = models.TimeField()
    date = models.DateField()
    quest = models.TextField()
    questioner = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.quest
    
class Reply(models.Model):
    time = models.TimeField()
    date = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replys',)
    answer = models.TextField()
    answerer = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.answer
    
    def get_absolute_url(self):
        return reverse("question_detail")
    