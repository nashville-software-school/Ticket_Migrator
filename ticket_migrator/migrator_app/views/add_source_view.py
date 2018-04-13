from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *

def renderAddSource(request):
    return render(request, 'migrator_app/add_source.html')

def addSource(request):
    new_repo = source_repo_model.Source_Repo(url=request.POST['source_repo'])
    new_repo.save()

    return render(request, 'migrator_app/backlog_groomer.html')
    

        