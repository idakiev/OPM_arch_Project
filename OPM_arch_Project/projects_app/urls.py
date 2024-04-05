from django.urls import include, path

from OPM_arch_Project.projects_app.views import ProjectsListView, ProjectsCreateView, ProjectsDetailsView, \
    ProjectsUpdateView, BaseProjectsUpdateView

urlpatterns = [
    path('', include([
        path('list/', ProjectsListView.as_view(), name='projects_list'),
        path('create/', ProjectsCreateView.as_view(), name='projects_create'),
        path('<int:pk>/', include([
            path('details/', ProjectsDetailsView.as_view(), name='projects_details'),
            path('update/', ProjectsUpdateView.as_view(), name='projects_update'),
            path('update/base/', BaseProjectsUpdateView.as_view(), name='projects_base_update'),
        ])),
    ]))
]
