from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm
from OPM_arch_Project.projects_app.models import Project, BaseProject


class ProjectsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Project
    template_name = 'projects_app/projects_list.html'


class ProjectsCreateView(auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin, views.CreateView):
    model = BaseProject
    template_name = 'projects_app/projects_create.html'
    form_class = ProjectsCreateForm
    permission_required = 'projects_app.add_baseproject'

    def get_success_url(self):
        return reverse_lazy('projects_list')
