from OPM_arch_Project.clients_app.models import Client
from OPM_arch_Project.projects_app.models import Project


def main_client(request):
    main_company = Client.objects.filter(is_main=True).first()

    if main_company:
        context = {
            'main_client': main_company,
        }

        return context
    return {}


def clients_count(request):
    main_clients = Client.objects.filter(is_main=True).count()
    total_count = Client.objects.count() - main_clients

    context = {
        'clients_count': total_count,
    }
    return context


def all_projects_count(request):
    main_projects = Project.objects.filter(base_project__client__is_main=True).count()
    all_projects = Project.objects.all().count() - main_projects

    context = {
        'all_projects_count': all_projects,
    }

    return context
