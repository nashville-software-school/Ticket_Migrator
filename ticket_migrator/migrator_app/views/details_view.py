from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *

from operator import itemgetter
import requests
import base64
import json



def details(request, backlog_id):
    
    selected_backlog = get_object_or_404(backlog_model.Backlog, pk=backlog_id)
    github = selected_backlog.source_repo.url.split('https://github.com/')[1]

    headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
    url = f'https://api.github.com/repos/{github}/issues'

    response = requests.get(url, headers=headers).json()

    issues = [{"number": api_issue['number'], "title": api_issue['title'], "priority": backlog_issue['priority']}
              for backlog_issue in sorted(list(selected_backlog.backlog_issues_set.all().values()),key=itemgetter('priority'))
              for api_issue in response if api_issue['id'] == backlog_issue['issue_id']]

    context = {"backlog": selected_backlog,
               "issues": issues}
        
    return render(request, 'migrator_app/details.html', context)

