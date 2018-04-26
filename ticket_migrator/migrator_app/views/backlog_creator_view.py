from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from migrator_app.models import *
from django import forms
from django.contrib.auth.decorators import login_required
import json

@login_required
def create_backlog_and_tickets(request):
    source_repo_id = int(request.POST.get("source_repo_id"))
    source_repo = source_repo_model.Source_Repo.objects.get(pk=source_repo_id)
    backlog_name = request.POST.get("backlog_name")
    issues_array = json.loads(request.POST.get("issue_array"))

    new_backlog = backlog_model.Backlog(
        name=backlog_name, source_repo=source_repo)
    new_backlog.save()

    for issue in issues_array:
        new_issue = backlog_issues_model.Backlog_Issues(
            backlog=new_backlog, issue_id=issue['id'], priority=issue['priority'])
        new_issue.save()

    return JsonResponse({'backlog_id': new_backlog.id})
