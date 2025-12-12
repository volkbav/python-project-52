# tasks/forms.py
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.functions import attrs_add

from .models import Task


class TaskForm(ModelForm):
        
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
             'labels',
        ]
        labels = {
            'name': _("Name"),
            'description': _("Description"),
            'status': _("Status"),
            'executor': _("Executor"),
             'labels': _("Labels"),
        }
        widgets = {
            'labels': forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  

        super().__init__(*args, **kwargs)
        
        placeholders = {
            'name': _("Name"),
            'description': _("Description"),
            'status': _("Status"),
            'executor': _("Executor"),
            'labels': _("Labels"),
        }
    
        attrs_add(self.fields, placeholders)
        
    def save(self, commit=True):
        task = super().save(commit=False)
        if self.user:
            task.author = self.user
        if commit:
            task.save()
            self.save_m2m()  # сохраняем связь ManyToMany
        return task

