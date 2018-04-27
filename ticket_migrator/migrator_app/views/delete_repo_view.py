from django.shortcuts import redirect
from migrator_app.models import *
from django.contrib.auth.models import User


def delete_repo(request, source_repo_id):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('../')
    return redirect('../accounts/login/')
