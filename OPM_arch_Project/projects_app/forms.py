from django import forms

from OPM_arch_Project.projects_app.models import BaseProject


class ProjectsCreateForm(forms.ModelForm):

    class Meta:
        model = BaseProject
        fields = '__all__'
