from django.db import models

class Source_Repo(models.Model):
    url = models.CharField(max_length=200)