from django.contrib import admin
from django.db import models

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm, ProjectsFilesUpdateForm, ProjectsFilesCreateForm
from OPM_arch_Project.projects_app.models import BaseProject, Project, ProjectFile, ProjectComment


@admin.register(BaseProject)
class BaseProjectAdmin(admin.ModelAdmin):
    model = BaseProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    form = ProjectsCreateForm


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    model = ProjectFile

    list_display = ('__str__', 'file', 'uploaded_by', 'created_at', 'modified_at')
    list_filter = ('uploaded_by', 'created_at', 'modified_at')
    sortable_by = ('project', 'uploaded_by',)


@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    model = ProjectComment
    form = ProjectsCreateForm

    list_display = ('user', 'project',)
    list_filter = ['user', 'project__client']
    search_fields = ('user__email', 'project__name',)
