from django.db import models
from django.utils import timezone

class TodoModel(models.Model):
    todo = models.CharField(max_length=100, blank=True)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.todo
