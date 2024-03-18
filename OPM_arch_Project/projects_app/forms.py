from django import forms

from OPM_arch_Project.projects_app.models import Project


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
