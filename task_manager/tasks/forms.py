# tasks/forms.py
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.utils import attrs_add

from .models import Task


class TaskForm(ModelForm):
        
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'project',
            'status',
            'executor',
            'labels',
        ]
        labels = {
            'name': _("Name"),
            'description': _("Description"),
            'project': _('Project'),
            'status': _("Status"),
            'executor': _("Executor"),
            'labels': _("Labels"),
        }
        widgets = {
            'labels': forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        self.project_pk = kwargs.pop('project_pk', None)
        
        super().__init__(*args, **kwargs)
        self.fields['project'].initial = self.project_pk     

        self.label_suffix = ""
        placeholders = {
            'name': _("Name"),
            'description': _("Description"),
            'status': _("Status"),
            'executor': _("Executor"),
            'labels': _("Labels"),
        }
    
        attrs_add(self.fields, placeholders)
        
        if 'executor' in self.fields:
            users = User.objects.all()
            self.fields['executor'].label_from_instance = lambda obj: (
                f"{obj.first_name} {obj.last_name}".strip() or obj.username
            )
            self.fields['executor'].queryset = users.order_by(
                'first_name', 
                'last_name'
            )

    def save(self, commit=True):
        task = super().save(commit=False)
        if self.user:
            task.author = self.user
        
        if self.project_pk:  
            task.project_id = self.project_pk

        if commit:
            task.save()
            self.save_m2m()  # сохраняем связь ManyToMany
        return task

