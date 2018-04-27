from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *
from django.contrib.auth.decorators import login_required
import base64
from pip._vendor import requests
# from ticket_migrator.migrator_app.models import source_repo_model


# - method to get id of source repo that contains all the issues
# - pull info from this source repo
# - right container should be populated with issues

@login_required
def drag_view(request, source_repo_id):

    # this 404 function requests specific id source repo from database or will redirect to 404 if not found:
    selected_source_repo = get_object_or_404(
        source_repo_model.Source_Repo, pk=source_repo_id)
    # this variable allows you to omit 'https://github.com' from the url on line 24
    github_location = selected_source_repo.url.split("https://github.com/")[1]

    headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
    url = f'https://spyproxy.bangazon.com/student/commit/https://api.github.com/repos/{github_location}/issues'

    response = requests.get(url, headers=headers).json()

    # Make an object for each issue returned from GitHub API in 'context' format
    # Issues builds a dictionary object [comprehension] for each item in respone with key/values for html template
    issues = [{"github_id": issue['id'], "issue_number":issue['number'],
               "issue_title":issue['title']} for issue in reversed(response)]

    context = {
        "source_repo": selected_source_repo,
        'issues': issues,
    }
    return render(request, 'migrator_app/dragdrop_issues.html', context)
