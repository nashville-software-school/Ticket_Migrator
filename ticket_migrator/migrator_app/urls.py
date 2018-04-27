from django.urls import path
from migrator_app.views import *

app_name = 'migrator_app'
urlpatterns = [
    path('addsourceform/', add_source_view.renderAddSource, name='renderAddSource'),
    path('addsource/', add_source_view.addSource, name='addSource'),
    path('', backlog_groomer_view.renderRepoSelector, name='renderRepoSelector'),
    path('drag_drop/<int:source_repo_id>', drag_view.drag_view, name='drag_drop'),
    path('migrate/<int:backlog_id>', select_target_repos_view.select_target_repos, name='select_target_repos'),
    path('success/<int:backlog_id>', success_view.success, name='success'),
    path('details/<int:backlog_id>', details_view.details, name='details'),
    path('delete_repo/<int:source_repo_id>', delete_repo_view.delete_repo, name='delete_repo'),
    path('delete_backlog/<int:backlog_id>', delete_backlog_view.delete_backlog, name='delete_backlog'),
    path('createbacklog/', backlog_creator_view.create_backlog_and_tickets, name='create_backlog'),
    path('register/', register_view.register, name='register'),
    path('profile/', profile_view.profile, name='profile'),
]