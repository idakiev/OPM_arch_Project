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
    list_display = ('name', 'city', 'street_name', 'street_number', 'is_active', 'is_main', 'number_of_employees')
    list_filter = ['is_active', 'is_main', 'name', 'city',]
    sortable_by = ['name', 'city', 'is_main', 'is_active',]
    ordering = ['-is_main', 'name']
    fields = (
        'name', 'country', 'city', 'street_name', 'street_number',
        'telephone_number', 'website', 'is_active', 'is_main',
    )
    inlines = [
        EmployeesInline
    ]
    verbose_name_plural = 'Clients'

    @admin.display(description='Employees')
    def number_of_employees(self, request):
        num_employees = UserModel.objects.filter(client=request.pk).count()
        return num_employees


class CitiesInLine(admin.StackedInline):
    model = City
    extra = 0


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    model = Municipality
    list_display = ('name', 'province', 'region', 'cities_count')
    list_filter = ['province', 'region',]
    inlines = [
        CitiesInLine
    ]
    search_fields = ['name', 'province', 'region',]

    def cities_count(self, request):
        count = City.objects.filter(municipality__name=request.name).count()
        return count


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('name', 'municipality',)
    list_filter = ('municipality',)
    search_fields = ['name', 'municipality__name']
