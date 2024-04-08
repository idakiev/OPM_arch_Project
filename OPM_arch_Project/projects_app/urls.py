from django.urls import include, path

from OPM_arch_Project.projects_app.views import ProjectsListView, ProjectsCreateView, ProjectsDetailsView, \
    ProjectsUpdateView, BaseProjectsUpdateView, ProjectsFilesDetailView, ProjectsFilesCreateView, \
    ProjectsFilesUpdateView, ProjectsFilesDeleteView

urlpatterns = [
    path('', include([
        path('list/', ProjectsListView.as_view(), name='projects_list'),
        path('create/', ProjectsCreateView.as_view(), name='projects_create'),
        path('<int:pk>/', include([
            path('details/', ProjectsDetailsView.as_view(), name='projects_details'),
            path('update/', ProjectsUpdateView.as_view(), name='projects_update'),
            path('update/base/', BaseProjectsUpdateView.as_view(), name='projects_base_update'),
            path('files/', include([
                path('', ProjectsFilesDetailView.as_view(), name='projects_files'),
                path('create/', ProjectsFilesCreateView.as_view(), name='projects_files_create'),
                path('<int:pk_file>/update/', ProjectsFilesUpdateView.as_view(), name='projects_files_update'),
                path('<int:pk_file>/delete/', ProjectsFilesDeleteView.as_view(), name='projects_files_delete'),
            ])),
        ])),
    ]))
]
