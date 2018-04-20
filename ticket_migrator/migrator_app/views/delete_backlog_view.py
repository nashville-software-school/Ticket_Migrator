from django.shortcuts import redirect
from migrator_app.models import *

def delete_backlog(request, backlog_id):
    backlog_model.Backlog.objects.filter(pk=backlog_id).delete()
    return redirect('../')
    