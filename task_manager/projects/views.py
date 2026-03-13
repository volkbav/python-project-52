# task_manager/projects/views.py
# from django.contrib import messages
# from django.shortcuts import redirect, render
from django_filters.views import FilterView

from task_manager.mixins import (
    # LoginRequiredMixin,
    RequireMessageMixin,
    # TaskPermissionMixin,
)

from .models import Project


# Create your views here.
class ProjectsIndexView(RequireMessageMixin, FilterView):
    model = Project
    template_name = "projects/index.html"
    # filterset_class = TaskFilter