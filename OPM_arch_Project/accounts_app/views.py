
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

from django.shortcuts import render, redirect

from OPM_arch_Project.accounts_app.forms import EditProfileForm, CheckAuthForm, LoginUserForm, \
    ChangePasswordUserForm
from OPM_arch_Project.accounts_app.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts_app/login_user.html'
    redirect_authenticated_user = True
    form_class = LoginUserForm

    def form_valid(self, form):
        result = super().form_valid(form)

        if form.redirect_to_password:
            return redirect('user_change_password')

        return result

    #
    # def form_valid(self, form):
    #     email = form.cleaned_data['email']
    #
    #     return redirect('change_password', email=email)


class LogOutUserView(auth_views.LogoutView):
    template_name = 'accounts_app/logout_user.html'


class ChangePasswordUserView(auth_views.PasswordChangeView):
    template_name = 'accounts_app/change_password_user.html'
    form_class = ChangePasswordUserForm
    success_url = reverse_lazy('profile_user')


def check_auth_user(request):
    form = CheckAuthForm()
    user = request.user

    if request.method == 'POST':
        form = CheckAuthForm(request.POST)

        if form.is_valid():
            return check_auth_success(request)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts_app/check_auth.html', context=context)


def check_auth_success(request):
    return render(request, 'accounts_app/check_auth_success.html')


class ProfileUserView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'accounts_app/profile_user.html'


class ProfileDetailsUserView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'accounts_app/profile_details.html'


class ProfileEditUserView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts_app/profile_edit.html'

    def get(self, request, *args, **kwargs):
        result = super().get(self, *args, **kwargs)

        if request.user.pk == self.object.pk or request.user.is_superuser:
            return result
        else:
            return render(request, template_name='403.html')

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'profile_user'
        )
