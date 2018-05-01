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
def success(request, sprint_id):

    password = request.POST.get("password", "")

    user = authenticate(username=request.user.username,
                        password=password)

    if(user):
        selected_sprint = get_object_or_404(
            sprint_model.Sprint, pk=sprint_id)
        target_repos = json.loads(request.POST.get("target_repos", ""))

        token = aes_decrypt(password, request.user.profile.token)

        auto = automator(selected_sprint, target_repos, token)
        auto.run()

        context = {'sprint': selected_sprint, 'target_repos': target_repos}

        return render(request, 'migrator_app/success.html', context)

    else:
        context = {'sprint': None, 'target_repos': [
            "MIGRATION FIALED : PASSWORD NOT VALID"]}

        return render(request, 'migrator_app/success.html', context)
