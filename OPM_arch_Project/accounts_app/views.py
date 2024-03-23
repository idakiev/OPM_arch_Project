
from django.contrib.auth import mixins as auth_mixins, get_user_model, login
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

from django.shortcuts import render, redirect

from OPM_arch_Project.accounts_app.forms import CreateUserForm, EditProfileForm, CheckAuthForm
from OPM_arch_Project.accounts_app.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts_app/login_user.html'
    redirect_authenticated_user = True


class LogOutUserView(auth_views.LogoutView):
    template_name = 'accounts_app/logout_user.html'


# TODO: Check how to fix the auth process if email is existing in the db.
def check_auth_user(request):
    users_emails = UserModel.objects.values_list('email')
    form = CheckAuthForm()

    user = request.user

    if request.method == 'POST':
        form = CheckAuthForm(request.POST)
        for mail in users_emails:
            if form.data['email'] in mail:
                user = UserModel.objects.get(email=form.data['email'])
                return redirect('login_user')

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts_app/check_auth.html', context=context)


class RegisterUserView(views.CreateView):
    form_class = CreateUserForm
    template_name = 'accounts_app/register_user.html'
    success_url = reverse_lazy('profile_user')

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)

        if self.request.user.is_authenticated:
            return redirect('profile_user')

        return result

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


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
