from django.contrib import admin
from migrator_app.models import backlog_issues_model, backlog_model, source_repo_model


# Register your models here.

admin.site.register(backlog_model.Backlog)
admin.site.register(source_repo_model.Source_Repo)
admin.site.register(backlog_issues_model.Backlog_Issues)