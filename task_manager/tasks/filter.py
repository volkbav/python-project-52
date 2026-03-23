# task_manager/tasks/filter.py
from django.contrib.auth import get_user_model
from django.forms import CheckboxInput, Select
from django.utils.translation import gettext_lazy as _
from django_filters import (
    BooleanFilter,
    FilterSet,
    ModelChoiceFilter,
)

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.projects.models import Project

from .models import Task


class TaskFilter(FilterSet):
    self_tasks = BooleanFilter(
        label=_("Only my tasks"),
        method="filter_self_tasks",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,  # ставим по умолчанию отмеченный чекбокс
    )

    project = ModelChoiceFilter(
        queryset=Project.objects.all(),
        label=_("Project"),  # Явно задаем лейбл
        widget=Select(attrs={"class": "form-select"})
    )

    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_("Status"),  # Явно задаем лейбл
        widget=Select(attrs={"class": "form-select"})
    )
    
    executor = ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=_("Executor"),  # Явно задаем лейбл
        widget=Select(attrs={"class": "form-select"})
    )

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label"),
        widget=Select(attrs={"class": "form-select"})
    )

    widget_classes = {
        "filter_self_tasks": "form-check-input",
    }

    class Meta:
        model = Task
        fields = ['project', "status", "executor", "labels"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form.label_suffix = ""  # убираем двоеточие

        for field_name in ["project", "status", "executor", "labels"]:
            if field_name in self.form.fields:
                placeholder = self.form.fields[field_name].label
                self.form.fields[field_name].widget.attrs['placeholder'] = str(placeholder)  # noqa: E501

        if 'executor' in self.form.fields:
            self.form.fields['executor'].label_from_instance = lambda obj: (
            f"{obj.first_name} {obj.last_name}".strip() or obj.username
            )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
