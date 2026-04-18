# task_manager/tasks/views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django_filters.views import FilterView

from task_manager.mixins import (
    LoginRequiredMixin,
    RequireMessageMixin,
    TaskPermissionMixin,
)
from task_manager.projects.models import Project
from task_manager.utils import render_markdown

from .filter import TaskFilter
from .forms import TaskForm
from .models import Task


# Create your views here.
# path ''
class TasksIndexView(RequireMessageMixin, FilterView):
    model = Task
    template_name = "tasks/index.html"
    filterset_class = TaskFilter


# path '<int:pk>/create/'
class TaskCreateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        project_id = request.GET.get('project')
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            status = project.status
        else:
            status = None

        form = TaskForm(
            user=request.user,
            project_pk=project_id,
            executor=request.user,
            status=status,
        )
        context = {
            "form": form,
            "button": _("Create"),
        }
        return render(request, "tasks/create.html", context)
        
    def post(self, request, *args, **kwargs):
        project_id = request.GET.get('project')
        form = TaskForm(
            request.POST or None,
            user=request.user,
            project_pk=project_id,
            )
        
        if form.is_valid():
            form.save()
            messages.success(request, _("The task was created successfully"))
            return redirect_task(project_id)
        context = {
            'form': form,
            'button': _("Create"),
        }
        return render(request, 'tasks/create.html', context)


# path '<int:pk>/delete'
class TaskDeleteView(TaskPermissionMixin, View):
    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = Task.objects.get(pk=task_pk)
        context = {
            "task_pk": task_pk,
            "name": task.name,
        }
        return render(
            request,
            "tasks/delete.html",
            context
        )
    
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = Task.objects.get(pk=status_pk)
        if status:
            status.delete()
            messages.success(request, _("Task successfully deleted"))
            return redirect('tasks:index')
        messages.error(request, _('Oops'))
        return redirect('tasks:index')


# path '<int:pk>/update/'
class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        status = Task.objects.get(pk=task_pk)
        form = TaskForm(instance=status)
        context = {
            "form": form,
            "task_pk": task_pk,
            "button": _("Edit"),
        }
        return render(
            request,
            "tasks/update.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        
        task = Task.objects.get(pk=task_pk)
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("Task successfully edited"))
            return redirect('tasks:index')
        context = {
            'form': form,
            "button": _("Edit"),
            }

        return render(request, 'tasks/update.html', context)
    

# path '<int:pk>/'
class TaskView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = Task.objects.get(pk=task_pk)
        task.description_html = render_markdown(task.description)
        context = {
            "task": task,
        }
        return render(request, "tasks/show_task.html", context)
    

def redirect_task(project_id):
    if project_id:
        return redirect(reverse('projects:project', kwargs={'pk': project_id}))
    return redirect(reverse('tasks:index'))