from django.forms import CheckboxInput, Select
from django.utils.translation import gettext_lazy as _
from django_filters import (
    BooleanFilter,
    FilterSet,
    ModelChoiceFilter,
)

from task_manager.functions import attrs_add
from task_manager.labels.models import Label

from .models import Task


class TaskFilter(FilterSet):
    self_tasks = BooleanFilter(
        label=_("Only my tasks"),
        method="filter_self_tasks",
        widget=CheckboxInput()
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
        fields = ["status", "executor", "labels"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "status": _("Select status"),
            "executor": _("Select executor"),
            "labels": _("Select labels"),
        }

        attrs_add(self.form.fields, placeholders, )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
