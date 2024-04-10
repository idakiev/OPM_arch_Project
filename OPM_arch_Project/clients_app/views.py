from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from OPM_arch_Project.clients_app.forms import ClientsCreateForm, ClientsUpdateForm
from OPM_arch_Project.clients_app.models import Client


class ClientsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Client
    template_name = 'clients_app/clients_list.html'


class ClientsDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'clients_app/clients_details.html'
    model = Client

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.check_request_permissions():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def check_request_permissions(self):

        if self.request.user.client != self.get_object()\
                and not self.request.user.is_staff:
            raise PermissionDenied

        return True


class ClientsCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'clients_app/clients_create.html'
    model = Client
    form_class = ClientsCreateForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.check_request_permissions():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def check_request_permissions(self):

        if not self.request.user.is_staff:
            raise PermissionDenied

        return True

    def get_success_url(self):
        return reverse_lazy('clients_details', kwargs={'pk': self.object.pk})


class ClientsUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'clients_app/clients_update.html'
    model = Client
    form_class = ClientsUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.check_request_permissions():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def check_request_permissions(self):

        if self.request.user.client != self.get_object()\
                and not self.request.user.is_staff:
            raise PermissionDenied
        elif self.request.user.client.is_main:
            if not self.request.user.is_staff:
                raise PermissionDenied

        return True

    def get_success_url(self):
        return reverse_lazy('clients_details', kwargs={'pk': self.object.pk})
