from django.shortcuts import render
from migrator_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from migrator_app.utils.encrypt import aes_encrypt
from django.contrib.auth import authenticate


@login_required
def profile(request):
    current_user = request.user
    context = {"user": current_user}

    if request.method == 'POST':
        if ('delete_token' in request.POST):
            current_user.profile.token = None
            current_user.save()

        else:
            raw_password = request.POST['password']
            user = authenticate(username=request.user.username,
                                password=raw_password)

            if(user):
                token = request.POST['token']
                ciphertext = aes_encrypt(raw_password, token)
                current_user.profile.token = ciphertext
                current_user.save()

    return render(request, 'migrator_app/profile.html', context)
