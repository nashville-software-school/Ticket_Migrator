from django.db import models
from .source_repo_model import Source_Repo

class Backlog(models.Model):
    name = models.CharField(max_length=200)
    source_repo = models.ForeignKey(Source_Repo, on_delete=models.DO_NOTHING)