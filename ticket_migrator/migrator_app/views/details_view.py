from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *

from operator import itemgetter
from django.contrib.auth.decorators import login_required
import requests
import base64
import json


@login_required
def details(request, sprint_id):

    selected_sprint = get_object_or_404(sprint_model.Sprint, pk=sprint_id)
    github = selected_sprint.source_repo.url.split('https://github.com/')[1]

    headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
    url = f'https://spyproxy.bangazon.com/student/commit/https://api.github.com/repos/{github}/issues?per_page=70'

    response = requests.get(url, headers=headers).json()

    issues = [{"number": api_issue['number'], "title": api_issue['title'], "priority": sprint_issue['priority']}
              for sprint_issue in sorted(list(selected_sprint.sprint_issues_set.all().values()),key=itemgetter('priority'))
              for api_issue in response if api_issue['id'] == sprint_issue['issue_id']]

    context = {"sprint": selected_sprint,
               "issues": issues}

    return render(request, 'migrator_app/details.html', context)

