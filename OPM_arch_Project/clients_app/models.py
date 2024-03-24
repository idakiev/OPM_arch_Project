from django.core import validators
from django.db import models

from OPM_arch_Project.core.validators import check_only_digits


class Municipality(models.Model):
    MUNICIPALITY_NAME_MAX_LENGTH = 50
    PROVINCE_NAME_MAX_LENGTH = 50
    REGION_NAME_MAX_LENGTH = 50
    TEL_NUMBER_MAX_LENGTH = 30
    TEL_NUMBER_MIN_LENGTH = 5

    name = models.CharField(
        max_length=MUNICIPALITY_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    province = models.CharField(
        max_length=PROVINCE_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    region = models.CharField(
        max_length=REGION_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    postal_code = models.PositiveIntegerField()
    telephone_number = models.CharField(
        max_length=TEL_NUMBER_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(TEL_NUMBER_MIN_LENGTH),
            check_only_digits,
        ),
        blank=False,
        null=False,
    )
    website = models.URLField(
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name_plural = 'Municipalities'

    def __str__(self):
        return self.name


class City(models.Model):
    CITY_NAME_MAX_LENGTH = 50
    TEL_CODE_MAX_LENGTH = 10
    TEL_CODE_MIN_LENGTH = 2

    name = models.CharField(
        max_length=CITY_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    telephone_code = models.CharField(
        max_length=TEL_CODE_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(TEL_CODE_MIN_LENGTH),
            check_only_digits,
        ),
        blank=False,
        null=False,
    )
    municipality = models.ForeignKey(
        to=Municipality,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Client(models.Model):
    NAME_MAX_LENGTH = 100
    COUNTRY_MAX_LENGTH = 50
    CITY_MAX_LENGTH = 50
    STREET_NAME_MAX_LENGTH = 100
    TEL_NUMBER_MAX_LENGTH = 100
    TEL_NUMBER_MIN_LENGTH = 5

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )
    country = models.CharField(
        max_length=COUNTRY_MAX_LENGTH,
        blank=False,
        null=False,
    )
    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        blank=False,
        null=False,
    )
    street_name = models.CharField(
        max_length=STREET_NAME_MAX_LENGTH
    )
    street_number = models.PositiveIntegerField(
        blank=False,
        null=False,
    )
    telephone_number = models.CharField(
        max_length=TEL_NUMBER_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(TEL_NUMBER_MIN_LENGTH),
            check_only_digits,
        ),
        blank=False,
        null=False,
    )
    website = models.URLField(
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_main = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name
