from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *
from django.contrib.auth.decorators import login_required

from migrator_app.utils.automator import automator
import json


@login_required
def success(request, backlog_id):

    selected_backlog = get_object_or_404(backlog_model.Backlog, pk=backlog_id)
    target_repos = json.loads(request.POST.get("target_repos", ""))
    credentials = request.POST.get("credentials", "")

    auto = automator(selected_backlog, target_repos, credentials)
    auto.run()

    context = {'backlog': selected_backlog, 'target_repos': target_repos}

    return render(request, 'migrator_app/success.html', context)
