from django import template

from OPM_arch_Project.projects_app.models import Project

register = template.Library()


@register.inclusion_tag('projects_app/partials/projects.html')
def show_projects(projects):

    return {'projects': projects}


@register.inclusion_tag('projects_app/partials/projects_as_employee.html')
def show_projects_as_employee(request, projects):

    return {'projects': projects, 'request': request}


@register.inclusion_tag('projects_app/partials/projects_as_manager.html')
def show_projects_as_manager(request, base_projects):

    return {'base_projects': base_projects, 'request': request}
