from django.shortcuts import redirect
from migrator_app.models import *


def delete_sprint(request, sprint_id):
    sprint_model.Sprint.objects.filter(pk=sprint_id).delete()
    return redirect('../')
