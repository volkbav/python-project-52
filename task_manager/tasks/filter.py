from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter, ModelMultipleChoiceFilter
from django.utils.translation import gettext_lazy as _
from .models import Task
from task_manager.labels.models import Label

from task_manager.functions import attrs_add
from django.forms import CheckboxInput, Select


class TaskFilter(FilterSet):
    my_tasks = BooleanFilter(
        label=_("Only my tasks"),
        method="filter_my_tasks",
        widget=CheckboxInput()
    )

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label"),
        widget=Select(attrs={"class": "form-control"})
    )

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

        attrs_add(self.form.fields, placeholders)

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
