from django import template

from OPM_arch_Project.projects_app.models import Project

register = template.Library()


@register.inclusion_tag('projects_app/projects.html')
def show_projects():
    projects = Project.objects.all()
    return {'projects': projects}
