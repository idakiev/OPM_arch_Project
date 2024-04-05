from django import forms

from OPM_arch_Project.projects_app.models import BaseProject, Project, ProjectComment


class ProjectsCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = BaseProject
        fields = '__all__'


class BaseProjectUpdateForm(forms.ModelForm):

    class Meta:
        model = BaseProject
        fields = '__all__'
        exclude = ['client']


class ProjectsUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['base_project']
        widgets = {
            'employees': forms.CheckboxSelectMultiple(),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'employees': ''
        }


class ProjectsCommentForm(forms.ModelForm):

    class Meta:
        model = ProjectComment
        fields = ['text']
        labels = {
            'text': 'Message'
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'cols': 12})
        }
