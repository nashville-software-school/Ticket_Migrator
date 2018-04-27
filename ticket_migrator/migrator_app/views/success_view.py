from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


from migrator_app.utils.decrypt import aes_decrypt
from migrator_app.utils.automator import automator
import json


@login_required
def success(request, backlog_id):

    password = request.POST.get("credentials", "")

    user = authenticate(username=request.user.username,
                        password=password)

    if(user):
        selected_backlog = get_object_or_404(
            backlog_model.Backlog, pk=backlog_id)
        target_repos = json.loads(request.POST.get("target_repos", ""))

        token = aes_decrypt(password, request.user.profile.token)

        auto = automator(selected_backlog, target_repos, token)
        auto.run()

        context = {'backlog': selected_backlog, 'target_repos': target_repos}

        return render(request, 'migrator_app/success.html', context)

    else:
        context = {'backlog': None, 'target_repos': [
            "MIGRATION FIALED : PASSWORD NOT VALID"]}

        return render(request, 'migrator_app/success.html', context)
