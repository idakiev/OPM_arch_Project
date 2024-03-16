from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OPM_arch_Project.accounts_app'

    def ready(self):
        import OPM_arch_Project.accounts_app.signals
