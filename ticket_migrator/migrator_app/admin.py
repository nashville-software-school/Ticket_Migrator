from django.contrib import admin
from migrator_app.models import sprint_issues_model, sprint_model, source_repo_model


# Register your models here.

admin.site.register(sprint_model.Sprint)
admin.site.register(source_repo_model.Source_Repo)
admin.site.register(sprint_issues_model.Sprint_Issues)