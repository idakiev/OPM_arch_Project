from enum import Enum

from django.db import models
from django.contrib.auth import models as auth_models

from OPM_arch_Project.accounts_app.managers import AppUserManager
from OPM_arch_Project.clients_app.models import Client
from OPM_arch_Project.core.model_mixins import ChoicesEnumMixin


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    client = models.ForeignKey(
        to=Client,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class SpecialityChoices(ChoicesEnumMixin, Enum):
    ARCHITECT = 'Architect'
    CIVIL_ENGINEER = 'Civil Engineer'
    MEP_ENGINEER = 'MEP Engineer'
    HVAC_ENGINEER = 'HVAC Engineer'
    ROAD_ENGINEER = 'ROAD Engineer'
    VIZ_ARTIST = '3D Artist'
    OTHER = 'Other'


class RoleChoices(ChoicesEnumMixin, Enum):
    JUNIOR = 'Junior'
    INTERMEDIATE = 'Intermediate'
    SENIOR = 'Senior'
    TEAM_LEADER = 'Team Leader'
    PROJECT_MANAGER = 'Project Manager'
    OTHER = 'Other'


class Profile(models.Model):
    PHONE_NUMBER_MAX_LENGTH = 150
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 50

    user = models.OneToOneField(
        AppUser, on_delete=models.CASCADE, primary_key=True,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    speciality = models.CharField(
        max_length=SpecialityChoices.max_name_len(),
        choices=SpecialityChoices.choices(),
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=RoleChoices.max_name_len(),
        choices=RoleChoices.choices(),
        blank=True,
        null=True,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        blank=True,
        null=True,
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.email} - {self.first_name} {self.last_name}"
