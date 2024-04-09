from django import forms


class SearchForm(forms.Form):

    project_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by project name...'
            }
        )
    )
