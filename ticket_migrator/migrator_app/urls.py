from django.urls import path
from migrator_app.views import *

app_name = 'migrator_app'
urlpatterns = [
    path('addsourceform/', add_source_view.renderAddSource, name='renderAddSource'),
    path('addsource/', add_source_view.addSource, name='addSource'),
    path('', sprint_groomer_view.renderRepoSelector, name='renderRepoSelector'),
    path('drag_drop/<int:source_repo_id>', drag_view.drag_view, name='drag_drop'),
    path('migrate/<int:sprint_id>', select_target_repos_view.select_target_repos, name='select_target_repos'),
    path('success/<int:sprint_id>', success_view.success, name='success'),
    path('details/<int:sprint_id>', details_view.details, name='details'),
    path('delete_repo/<int:source_repo_id>', delete_repo_view.delete_repo, name='delete_repo'),
    path('delete_sprint/<int:sprint_id>', delete_sprint_view.delete_sprint, name='delete_sprint'),
    path('createsprint/', sprint_creator_view.create_sprint_and_tickets, name='create_sprint'),
    path('register/', register_view.register, name='register'),
    path('profile/', profile_view.profile, name='profile'),
]