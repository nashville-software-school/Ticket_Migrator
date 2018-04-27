from django.shortcuts import redirect, render
from migrator_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from migrator_app.utils.encrypt import aes_encrypt


def register(request):
    if(request.method == 'GET'):
        return render(request, 'migrator_app/register.html')

    if(request.method == 'POST'):
        username = request.POST['email']

        raw_password1 = request.POST['password1']
        raw_password2 = request.POST['password2']

        if(raw_password1 != raw_password2):
            throw(error)

        user = User.objects.create_user(username, '', raw_password1)
        user = authenticate(username=username, password=raw_password1)
        login(request, user)

        token = request.POST['token']

        ciphertext = aes_encrypt(raw_password1, token)
        user.profile.token = ciphertext
        user.save()

        return redirect('../')
