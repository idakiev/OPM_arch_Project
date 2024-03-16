
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from OPM_arch_Project.clients_app.forms import ClientCreateForm, ClientUpdateForm
from OPM_arch_Project.clients_app.models import Client


class ClientDetailView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'clients_app/client_details.html'
    model = Client


class ClientCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'clients_app/client_create.html'
    model = Client
    form_class = ClientCreateForm

    def get_success_url(self):
        return reverse_lazy('index')


class ClientUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'clients_app/client_update.html'
    model = Client
    form_class = ClientUpdateForm
    success_url = reverse_lazy('index')
