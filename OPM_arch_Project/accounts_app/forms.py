from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from OPM_arch_Project.accounts_app.models import Profile


UserModel = get_user_model()


# TODO: Check how to fix the auth process if email is existing in the db.
class CheckAuthForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class CreateUserForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'client',)


class EditUserForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
