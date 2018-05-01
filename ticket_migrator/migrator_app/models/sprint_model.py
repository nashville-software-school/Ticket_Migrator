from django.db import models
from .source_repo_model import Source_Repo


class Sprint(models.Model):
    name = models.CharField(max_length=200, unique=True)
    source_repo = models.ForeignKey(Source_Repo, on_delete=models.CASCADE)

    def __str__(self):
        github = self.source_repo.url.split('https://github.com/')[1]
        return f'{self.name} : {github}'
