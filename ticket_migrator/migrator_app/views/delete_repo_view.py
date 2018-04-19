from django.http import JsonResponse
from migrator_app.models import *

def delete_repo(request, source_repo_id):
    source_repo_model.Source_Repo.objects.filter(pk=source_repo_id).delete()
    return JsonResponse({'delete': source_repo_id})
    