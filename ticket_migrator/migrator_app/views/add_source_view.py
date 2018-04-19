from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from migrator_app.models import *

def renderAddSource(request):
    source_repos = source_repo_model.Source_Repo.objects.all()
    context = {"source_repos":source_repos}
    return render(request, 'migrator_app/add_source.html', context)

def addSource(request):
    new_repo = source_repo_model.Source_Repo(url=request.POST['source_repo'])
    new_repo.save()

    return redirect(f'../drag_drop/{new_repo.id}')
    

        