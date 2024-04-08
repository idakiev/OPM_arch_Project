from OPM_arch_Project.clients_app.models import Client


def main_client(request):
    main_company = Client.objects.filter(is_main=True).first()

    if main_company:
        context = {
            'main_client': main_company,
        }

        return context
