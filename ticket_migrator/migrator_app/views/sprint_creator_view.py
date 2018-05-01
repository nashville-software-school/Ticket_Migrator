from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from migrator_app.models import *
from django import forms
from django.contrib.auth.decorators import login_required
import json

@login_required
def create_sprint_and_tickets(request):
    source_repo_id = int(request.POST.get("source_repo_id"))
    source_repo = source_repo_model.Source_Repo.objects.get(pk=source_repo_id)
    sprint_name = request.POST.get("sprint_name")
    issues_array = json.loads(request.POST.get("issue_array"))

    new_sprint = sprint_model.Sprint(
        name=sprint_name, source_repo=source_repo)
    new_sprint.save()

    for issue in issues_array:
        new_issue = sprint_issues_model.Sprint_Issues(
            sprint=new_sprint, issue_id=issue['id'], priority=issue['priority'])
        new_issue.save()

    return JsonResponse({'sprint_id': new_sprint.id})
