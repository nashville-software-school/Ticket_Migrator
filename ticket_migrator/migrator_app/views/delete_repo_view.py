from django.shortcuts import redirect
from migrator_app.models import *


def delete_repo(request, source_repo_id):
    source_repo_model.Source_Repo.objects.filter(pk=source_repo_id).delete()
    return redirect('../addsourceform')
