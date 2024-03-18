from django.apps import AppConfig


class ProjectsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OPM_arch_Project.projects_app'

    def ready(self):
        import OPM_arch_Project.projects_app.signals
