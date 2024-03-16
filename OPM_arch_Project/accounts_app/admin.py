from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from OPM_arch_Project.accounts_app.forms import CreateUserForm, EditProfileForm, EditUserForm
from OPM_arch_Project.accounts_app.models import Profile


UserModel = get_user_model()


@admin.register(Profile)
class AdminAppProfile(admin.ModelAdmin):
    model = Profile
    form = EditProfileForm


@admin.register(UserModel)
class AdminAppUser(UserAdmin):
    model = UserModel
    add_form = CreateUserForm
    form = EditUserForm

    list_display = ('pk', 'email', 'is_staff', 'is_active', "is_superuser")
    search_fields = ('email',)
    ordering = ('pk',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('client',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',  "is_superuser", 'groups',
                                    'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "client",),
            },
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(AdminAppUser, self).get_inline_instances(request, obj)
