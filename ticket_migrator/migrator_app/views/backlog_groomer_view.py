from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *
from django import forms

def renderRepoSelector(request):
    source_repo_list = source_repo_model.Source_Repo.objects.all()
    backlog_list = backlog_model.Backlog.objects.all()

    choices = [('#', 'Select Source Repo'), ('./addsourceform', 'Manage Source Repos')]
    choices[1:1] = [(f'./drag_drop/{repo.id}', repo.url) for repo in source_repo_list]

    context = {'choices':choices, "backlogs":backlog_list}
    return render(request, 'migrator_app/repo_selector.html', context)