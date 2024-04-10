from django.contrib import admin

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm
from OPM_arch_Project.projects_app.models import BaseProject, Project, ProjectFile, ProjectComment


@admin.register(BaseProject)
class BaseProjectAdmin(admin.ModelAdmin):
    model = BaseProject
    list_display = ('client', 'name', 'municipality', 'project_type', 'project_phase',)
    list_filter = ('client', 'municipality', 'project_type', 'project_phase',)
    search_fields = ('client', 'name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    form = ProjectsCreateForm
    list_display = ('base_project', 'start_date', 'end_date', 'status', 'progress',)
    list_filter = ('status', 'progress', 'end_date',)


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    model = ProjectFile

    list_display = ('__str__', 'file', 'uploaded_by', 'created_at', 'modified_at',)
    list_filter = ('project', 'uploaded_by', 'created_at', 'modified_at',)
    sortable_by = ('uploaded_by', 'created_at', 'modified_at',)


@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    model = ProjectComment
    form = ProjectsCreateForm

    list_display = ('user', 'project',)
    list_filter = ['user', 'project__client']
    search_fields = ('user__email', 'project__name',)
