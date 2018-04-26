from django.db import models
from .backlog_model import Backlog


class Backlog_Issues(models.Model):
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE)
    issue_id = models.IntegerField()
    priority = models.IntegerField()
