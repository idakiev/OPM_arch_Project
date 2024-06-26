from datetime import datetime
from enum import Enum

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models

from smart_selects import db_fields as smart_fields

from OPM_arch_Project.accounts_app.models import AppUser
from OPM_arch_Project.clients_app.models import Municipality, City, Client
from OPM_arch_Project.core.model_mixins import ChoicesEnumMixin, Timestamp
from OPM_arch_Project.core.validators import validate_file_size

UserModel = get_user_model()


class ProjectTypeChoices(ChoicesEnumMixin, Enum):
    SINGLE_HOUSE = 'Single House'
    ROW_HOUSES = 'Row Houses'
    MULTI_FAMILY_SMALL = 'Small Multi-Family building'
    MULTI_FAMILY_MEDIUM = 'Medium Multi-Family building'
    MULTI_FAMILY_BIG = 'Big Multi-Family building'
    OFFICE_BUILDING = 'Office building'
    PUBLIC_BUILDING = 'Public building'
    RENOVATION = 'Renovation'
    OTHER = 'Other'


class ProjectPhaseChoices(ChoicesEnumMixin, Enum):
    PRE_DESIGN = 'Pre-design'
    DESIGN = 'Design'
    PERMISSION = 'Permission'
    EXECUTIVE = 'Executive'
    OTHER = 'Other'


class ProjectStatusChoices(ChoicesEnumMixin, Enum):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'


class ProjectProgressChoices(ChoicesEnumMixin, Enum):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'


class BaseProject(Timestamp, models.Model):
    NAME_MAX_LENGTH = 150

    client = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )
    city = smart_fields.ChainedForeignKey(
        City,
        chained_field='municipality',
        chained_model_field='municipality',
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )
    project_type = models.CharField(
        max_length=ProjectTypeChoices.max_name_len(),
        choices=ProjectTypeChoices.choices(),
        blank=False,
        null=False,
    )
    project_phase = models.CharField(
        max_length=ProjectPhaseChoices.max_name_len(),
        choices=ProjectPhaseChoices.choices(),
        blank=False,
        null=False,
    )
    project_manager = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"is_staff": True},
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.client} - {self.name}"


class Project(Timestamp, models.Model):

    base_project = models.OneToOneField(
        BaseProject,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    employees = models.ManyToManyField(
        UserModel,
        limit_choices_to={"client__is_main": True},
        default=None,
        blank=True,
    )
    start_date = models.DateField(
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=ProjectStatusChoices.max_name_len(),
        choices=ProjectStatusChoices.choices(),
        blank=True,
        null=True,
    )
    progress = models.CharField(
        max_length=ProjectProgressChoices.max_name_len(),
        choices=ProjectProgressChoices.choices(),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.base_project}"

    def get_project_timeframe(self):
        if self.start_date and self.end_date:
            start_date = str(self.start_date)
            end_date = str(self.end_date)
            timeframe = datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")

            return timeframe.days

    @admin.display(description="Client")
    def get_client_name(self):
        return self.base_project.client


class ProjectFile(Timestamp, models.Model):
    TITLE_MAX_LENGTH = 25

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )
    file = models.FileField(
        upload_to="media/projects_files",
        validators=(
            validate_file_size,
        )
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.RESTRICT,
    )
    uploaded_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f"{self.project.base_project.name} - {self.title}"


class ProjectComment(Timestamp, models.Model):
    TEXT_MAX_LENGTH = 300

    text = models.TextField(
        max_length=TEXT_MAX_LENGTH,
        blank=False,
        null=False,
    )
    project = models.ForeignKey(
        to=BaseProject,
        on_delete=models.RESTRICT,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f"{self.user} - {self.project}"

    class Meta:
        ordering = ["created_at"]
