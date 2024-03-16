from django.contrib import admin
from django.contrib.auth import get_user_model

from OPM_arch_Project.clients_app.models import Client, Municipality, City

UserModel = get_user_model()


class EmployeesInline(admin.StackedInline):
    model = UserModel
    fk_name = 'client'
    can_delete = True
    verbose_name_plural = 'employees'
    fields = ['email', 'is_active', 'is_staff', 'is_superuser',]
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('name', 'city', 'street_name', 'street_number', 'is_active')
    fields = (
        'name', 'country', 'city', 'street_name', 'street_number',
        'telephone_number', 'website', 'is_active', 'is_main',
    )
    inlines = [
        EmployeesInline
    ]
    verbose_name_plural = 'Clients'


class CitiesInLine(admin.StackedInline):
    model = City
    extra = 0


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    model = Municipality
    inlines = [
        CitiesInLine
    ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('name', 'municipality',)
    list_filter = ('municipality',)
