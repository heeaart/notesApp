from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=250)
    publish_date = models.DateField(default=timezone.now)
    body = models.TextField(max_length=2500)
    author = models.CharField(max_length=100, default='')
    noteManager = models.Manager()

    def __str__(self):
        return self.title
