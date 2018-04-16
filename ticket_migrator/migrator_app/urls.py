from django.urls import path
from migrator_app.views import *

app_name = 'migrator_app'
urlpatterns = [
    path('/addsourceform/', add_source_view.renderAddSource, name='renderAddSource'),
    path('/addsource/', add_source_view.addSource, name='addSource'),
    path('/reposelector/', backlog_groomer_view.renderRepoSelector, name='renderRepoSelector'),
]