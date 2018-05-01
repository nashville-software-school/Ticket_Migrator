from django.db import models
from .sprint_model import Sprint


class Sprint_Issues(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    issue_id = models.IntegerField()
    priority = models.IntegerField()
