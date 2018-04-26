from django.shortcuts import render
from migrator_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    current_user = request.user
    context = {"user": current_user}

    if request.method == 'POST':
        token = request.POST['token']
        current_user.profile.token = token
        current_user.save()

    return render(request, 'migrator_app/profile.html', context)
