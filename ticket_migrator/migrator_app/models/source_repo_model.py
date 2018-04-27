from django.db import models


class Source_Repo(models.Model):
    url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.url

    def get_repo(self):
        '''Reurn the username/reponame of the source repo'''
        return self.url.split('https://github.com/')[1]
