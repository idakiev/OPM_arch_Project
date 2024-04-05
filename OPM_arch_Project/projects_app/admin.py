from django.contrib import admin

from OPM_arch_Project.projects_app.forms import ProjectsCreateForm
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
    pass


@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    pass
