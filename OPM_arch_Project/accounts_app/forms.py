from django.contrib.auth import forms as auth_forms, get_user_model, authenticate
from django import forms
from django.core.exceptions import ValidationError

from OPM_arch_Project.accounts_app.models import Profile
from OPM_arch_Project.core.utils import generate_verification_code, send_verification_email

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.redirect_to_password = False

    def clean(self):

        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            user = UserModel.objects.filter(email=email).first()
            if user and user.check_password(password) and not user.is_active and user.verification_code:
                user.is_active = True
                user.verification_code = False
                user.save()
                self.redirect_to_password = True
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        cleaned_data = super().clean()

        return cleaned_data


class ChangePasswordUserForm(auth_forms.PasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })


# TODO: Check how to fix the auth process if email is existing in the db.
class CheckAuthForm(forms.ModelForm):

    def clean(self):
        users_emails = UserModel.objects.values_list('email')

        for mail in users_emails:
            if self.data['email'] in mail:
                user = UserModel.objects.get(email=self.data['email'])
                if not user.is_active and not user.verification_code:
                    email = self.data['email']
                    verification_code = generate_verification_code(length=10)
                    send_verification_email(email, verification_code)

                    user.verification_code = True
                    user.set_password(verification_code)
                    user.save()
                    return

                elif user.verification_code:
                    raise ValidationError('Your verification email is already sent. '
                                          'Please check your email and follow the instructions.')

        raise ValidationError('This email is not a valid email address!')

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
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget.attrs['hidden'] = 'hidden'
        self.fields['password2'].widget.attrs['hidden'] = 'hidden'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Converting email to lowercase
            email = email.lower()
            existing_users = UserModel.objects.filter(email__iexact=email)
            if existing_users.exists():
                raise forms.ValidationError("A user with that email address already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        # Generating default password
        default_password = generate_verification_code(length=12)

        user.set_password(default_password)

        # Converting email to lowercase before saving to DB
        user.email = user.email.lower()

        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ['email', 'client', ]
        field_classes = {"email": forms.EmailField}
        help_texts = {
            'email': 'Enter your email address.'
        }


class EditUserForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
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
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'},
            ),
        }
