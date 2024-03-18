from django.db.models.signals import post_save
from django.dispatch import receiver

from OPM_arch_Project.projects_app.models import BaseProject, Project


@receiver(post_save, sender=BaseProject)
def create_project(sender, instance, created, **kwargs):
    if created:
        Project.objects.create(base_project=instance)
