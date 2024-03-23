from django.urls import include, path

from OPM_arch_Project.projects_app.views import ProjectsListView, ProjectsCreateView

urlpatterns = [
    path('', include([
        path('list/', ProjectsListView.as_view(), name='projects_list'),
        path('create/', ProjectsCreateView.as_view(), name='projects_create')
    ]))
]
