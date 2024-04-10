from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from OPM_arch_Project.accounts_app.forms import CreateUserForm, EditProfileForm, EditUserForm
from OPM_arch_Project.accounts_app.models import Profile


UserModel = get_user_model()


@admin.register(Profile)
class AppProfileAdmin(admin.ModelAdmin):
    model = Profile
    form = EditProfileForm

    list_display = ('user', 'get_name', 'speciality', 'role', 'show_client')
    list_filter = ['role', 'speciality',]

    @admin.display(description='Client')
    def show_client(self, obj):
        user = UserModel.objects.filter(pk=obj.user.pk).first()
        return user.client


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = CreateUserForm
    form = EditUserForm

    list_display = ('pk', 'email', 'client', 'is_staff', 'is_active', "is_superuser",)
    search_fields = ('email',)
    ordering = ('pk',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('client',)}),
        (_('Permissions'),{'fields': ('is_active', 'is_staff',  "is_superuser", 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
       ("User creation", {
                'description': 'New user will be created with default password.',
                "classes": ("wide",),
                "fields": ("email", "client",),
            },
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(AppUserAdmin, self).get_inline_instances(request, obj)
