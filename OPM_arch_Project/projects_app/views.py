from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm, ProjectsUpdateForm, ProjectsCommentForm, \
    BaseProjectUpdateForm
from OPM_arch_Project.projects_app.models import Project, BaseProject, ProjectComment


class ProjectsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Project
    template_name = 'projects_app/projects_list.html'
    ordering = ['-pk']

    def get_queryset(self):
        result = super().get_queryset()
        projects = Project.objects.filter(base_project__client=self.request.user.client)

        if self.request.user.client is None or not self.request.user.client.is_main:
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

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        comments = ProjectComment.objects.filter(project=self.object.project.pk)
        result['comments'] = comments
        result['comment_form'] = ProjectsCommentForm(instance=self.request.user)
        return result

    def get(self, *args, **kwargs):
        result = super().get(*args, **kwargs)

        if not self.request.user.client.is_main and self.object.client != self.request.user.client:
            raise PermissionDenied

        return result

    def post(self, request, *args, **kwargs):
        new_comment = ProjectComment(text=request.POST.get('text'),
                                     project=self.get_object(),
                                     user=self.request.user)
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class BaseProjectsUpdateView(auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin, views.UpdateView):
    model = BaseProject
    template_name = 'projects_app/projects_base_update.html'
    form_class = BaseProjectUpdateForm
    permission_required = 'projects_app.change_baseproject'

    def get_success_url(self):
        return reverse_lazy('projects_details', kwargs={'pk': self.object.project.pk})


class ProjectsUpdateView(auth_mixins.LoginRequiredMixin, auth_mixins.PermissionRequiredMixin, views.UpdateView):
    model = Project
    template_name = 'projects_app/projects_update.html'
    form_class = ProjectsUpdateForm
    permission_required = 'projects_app.change_baseproject'

    def get_success_url(self):
        return reverse_lazy('projects_details', kwargs={'pk': self.object.pk})
