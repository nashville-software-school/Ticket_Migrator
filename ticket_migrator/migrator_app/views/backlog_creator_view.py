from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from migrator_app.models import *
from django import forms

def create_backlog_and_tickets(request):
    source_repo_id = request.POST.get("source_repo_id")
    backlog_name = request.POST.get("backlog_name")
    issues_array = request.POST.get("issues_array")

    new_backlog = backlog_model.Backlog(name=backlog_name, source_repo=source_repo_id)
    new_backlog.save()

    # new_backlog.id

    for issue in issues_array:
        new_issue = backlog_issues_model.Backlog_Issues(backlog=new_backlog.id, issue_id=issue.id, priority=issue.priority)
        new_issue.save()

    return JsonResponse({'backlog_id': new_backlog.id})
    