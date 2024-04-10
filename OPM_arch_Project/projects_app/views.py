from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import request
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm, ProjectsUpdateForm, ProjectsCommentForm, \
    BaseProjectUpdateForm, ProjectsFilesCreateForm, ProjectsFilesUpdateForm, ProjectsFilesDeleteForm, SearchForm
from OPM_arch_Project.projects_app.models import Project, BaseProject, ProjectComment, ProjectFile


class ProjectsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Project
    template_name = 'projects_app/projects_list.html'
    ordering = ['-pk']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)

        return context

    def get_queryset(self):
        result = super().get_queryset()
        project_name_pattern = self.request.GET.get('project_name', None)

        if self.request.user.client is None or not self.request.user.client.is_main:
            result = Project.objects.filter(base_project__client=self.request.user.client)

        if project_name_pattern:
            filter_query = Q(base_project__name__icontains=project_name_pattern)
            return result.filter(filter_query)

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
        first_files = ProjectFile.objects.filter(project_id=self.object.project.pk).order_by('-modified_at')[:6]
        all_files = ProjectFile.objects.filter(project_id=self.object.project.pk)
        result['all_files'] = all_files
        result['first_files'] = first_files
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
    permission_required = 'projects_app.change_project'

    def get_success_url(self):
        return reverse_lazy('projects_details', kwargs={'pk': self.object.pk})


class ProjectsFilesDetailView(auth_mixins.LoginRequiredMixin,views.DetailView):
    model = BaseProject
    template_name = 'projects_app/projects_files.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)

        all_files = ProjectFile.objects.filter(project_id=self.object.project.pk).order_by('-modified_at')
        result['all_files'] = all_files
        return result

    def get(self, *args, **kwargs):
        result = super().get(*args, **kwargs)

        if not self.request.user.client.is_main and self.object.client != self.request.user.client:
            raise PermissionDenied

        return result


class ProjectsFilesCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = ProjectFile
    template_name = 'projects_app/projects_files_create.html'
    form_class = ProjectsFilesCreateForm

    def get_initial(self):
        initial = super().get_initial()
        initial['project'] = self.get_project()
        initial['uploaded_by'] = self.request.user
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['project'].disabled = True
        form.fields['uploaded_by'].disabled = True

        return form

    def get_project(self):
        project_id = self.kwargs['pk']
        result = Project.objects.get(pk=project_id)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.get_project()
        return context

    def get_success_url(self):
        return reverse_lazy('projects_details', kwargs={'pk': self.object.project.pk})

    def get(self, *args, **kwargs):
        result = super().get(*args, **kwargs)

        if (not self.request.user.is_superuser
                and self.get_project().base_project.client != self.request.user.client
                and self.request.user not in self.get_project().employees.all()):
            raise PermissionDenied

        return result


class ProjectsFilesUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = ProjectFile
    template_name = 'projects_app/projects_files_update.html'
    form_class = ProjectsFilesUpdateForm
    context_object_name = 'file'

    def get_object(self, queryset=None):
        pk_project = self.kwargs.get('pk')
        pk_file = self.kwargs.get('pk_file')
        return get_object_or_404(ProjectFile, project__pk=pk_project, pk=pk_file)

    def get_success_url(self):
        pk_project = self.kwargs.get('pk')
        return reverse('projects_details', kwargs={'pk': pk_project})

    def get(self, *args, **kwargs):
        result = super().get(*args, **kwargs)

        if not self.request.user.is_superuser and self.object.uploaded_by != self.request.user:
            raise PermissionDenied

        return result


class ProjectsFilesDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = ProjectFile
    template_name = 'projects_app/projects_files_delete.html'
    # form_class = ProjectsFilesDeleteForm
    context_object_name = 'file'

    def get_object(self, queryset=None):
        pk_project = self.kwargs.get('pk')
        pk_file = self.kwargs.get('pk_file')
        return get_object_or_404(ProjectFile, project__pk=pk_project, pk=pk_file)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectsFilesDeleteForm(initial={
            'title': self.object.title,
            'file': self.object.file,
            'project': self.object.project,
            'uploaded_by': self.object.uploaded_by,
        })

        return context

    def delete(self, request, *args, **kwargs):
        file = self.get_object()
        file.delete()

        return redirect(self.get_success_url)

    def get_success_url(self):
        return reverse_lazy(
            'projects_details', kwargs={'pk': self.object.project.pk}
        )

    def get(self, *args, **kwargs):
        result = super().get(*args, **kwargs)

        if not self.request.user.is_superuser and self.object.uploaded_by != self.request.user:
            raise PermissionDenied

        return result
