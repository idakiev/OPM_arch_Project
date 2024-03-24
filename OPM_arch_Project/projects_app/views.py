from django.http import request
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm, ProjectsUpdateForm
from OPM_arch_Project.projects_app.models import Project, BaseProject


class ProjectsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Project
    template_name = 'projects_app/projects_list.html'

    def get_queryset(self):
        result = super().get_queryset()
        projects = Project.objects.filter(base_project__client=self.request.user.client)

        if not self.request.user.client.is_main:
            return projects

        return result


class ProjectsCreateView(auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin, views.CreateView):
    model = BaseProject
    template_name = 'projects_app/projects_create.html'
    form_class = ProjectsCreateForm
    permission_required = 'projects_app.add_baseproject'

    def get_success_url(self):
        return reverse_lazy('projects_list')


class ProjectsDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = BaseProject
    template_name = 'projects_app/projects_details.html'


class ProjectsUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Project
    template_name = 'projects_app/projects_update.html'
    form_class = ProjectsUpdateForm
    permission_required = 'projects_app.change_baseproject'

    def get_success_url(self):
        return reverse_lazy('projects_details', kwargs={'pk': self.object.pk})
