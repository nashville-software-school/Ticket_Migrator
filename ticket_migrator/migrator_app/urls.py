from django.urls import path
from migrator_app.views import *

app_name = 'migrator_app'
urlpatterns = [
    path('addsourceform/', add_source_view.renderAddSource, name='renderAddSource'),
    path('addsource/', add_source_view.addSource, name='addSource'),
    path('reposelector/', backlog_groomer_view.renderRepoSelector, name='renderRepoSelector'),
    path('<int:backlog_id>/migrate/', select_target_repos_view.select_target_repos, name='select_target_repos'),
    path('<int:backlog_id>/success/', success_view.success, name='success'),
]