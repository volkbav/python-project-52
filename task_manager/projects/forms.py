# tasks/forms.py
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.utils import attrs_add

from .models import Project


class ProjectForm(ModelForm):
        
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'executor',
            # 'tasks',
            'status',
            'labels',
            'start_date',
            'deadline',
            'is_active', 
        ]

        labels = {
            'name': _("Name"),
            'description': _("Description"),
            'executor': _("Executor"),
            'status': _("Status"),
            'labels': _("Labels"),
            'start_date': _('Start date'),
            'deadline': _('Deadline'),
            'is_active': _('Is active'), 
            
        }
        widgets = {
            'labels': forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.executor = kwargs.pop('executor', None)
        
        super().__init__(*args, **kwargs)
        self.fields['executor'].initial = self.executor
        self.label_suffix = ""
        placeholders = {
            'name': _("Name"),
            'description': _("Description"),
            'executor': _("Executor"),
            'status': _("Status"),
            'labels': _("Labels"),
            'start_date': _('Start date'),
            'deadline': _('Deadline'),
            'is_active': _('Is active'), 
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
        project = super().save(commit=False)
        if self.user:
            project.author = self.user
        if commit:
            project.save()
            self.save_m2m()  # сохраняем связь ManyToMany
        return project

