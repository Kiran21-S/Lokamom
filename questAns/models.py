from django.db import models # type: ignore

# Create your models here.
class Question(models.Model):
    quest = models.TextField()
    questioner = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.quest