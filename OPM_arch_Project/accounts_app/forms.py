from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from OPM_arch_Project.accounts_app.models import Profile


UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ChangePasswordUserForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


# TODO: Check how to fix the auth process if email is existing in the db.
class CheckAuthForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class CreateUserForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'client',)
        help_texts = {
            'email': 'Enter your email address.'
        }


class EditUserForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name'},
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name'},
            ),
            'profile_picture': forms.ClearableFileInput(),
        }
