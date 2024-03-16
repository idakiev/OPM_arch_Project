from django import forms

from OPM_arch_Project.clients_app.models import Client


class ClientCreateForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['is_active', 'is_main',]


class ClientUpdateForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['is_active', 'is_main']
