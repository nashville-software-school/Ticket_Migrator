from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *
from django import forms
from django.contrib.auth.decorators import login_required

@login_required
def renderRepoSelector(request):
    source_repo_list = source_repo_model.Source_Repo.objects.all()
    sprint_list = sprint_model.Sprint.objects.all()

    choices = [('#', 'Select Source Repository'), ('./addsourceform', 'Manage Source Repositories')]
    choices[1:1] = [(f'./drag_drop/{repo.id}', repo.url) for repo in source_repo_list]

    context = {'choices':choices, "sprints":sprint_list}
    return render(request, 'migrator_app/repo_selector.html', context)