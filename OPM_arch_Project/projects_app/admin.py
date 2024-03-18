from django.contrib import admin

from OPM_arch_Project.projects_app.forms import ProjectCreateForm
from OPM_arch_Project.projects_app.models import BaseProject, Project


@admin.register(BaseProject)
class BaseProjectAdmin(admin.ModelAdmin):
    model = BaseProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    form = ProjectCreateForm
