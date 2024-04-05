from django import forms

from OPM_arch_Project.clients_app.models import Client


class ClientsCreateForm(forms.ModelForm):
    website = forms.URLField(initial='https://')

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['is_active', 'is_main',]
        help_texts = {
            'name': f'Maximum length of the name is {Client.NAME_MAX_LENGTH} characters.',
            'telephone_number': f'Should consists only of numbers.',
        }


class ClientsUpdateForm(forms.ModelForm):
    website = forms.URLField(initial='https://')

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['is_active', 'is_main']
