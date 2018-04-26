from django.shortcuts import redirect
from migrator_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):

    username = request.POST['username']
    raw_password = request.POST['password']

    user = User.objects.create_user(username, '', raw_password)

    user = authenticate(username=username, password=raw_password)
    login(request, user)
    return redirect('../profile/')
