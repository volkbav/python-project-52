from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from task_manager.mixins import (
    LoginRequiredMixin,
    RequireMessageMixin,
    TaskPermissionMixin,
)

from .forms import TaskForm
from .models import Task

from django_filters.views import FilterView
from .filter import TaskFilter


# Create your views here.
# path ''
class TasksIndexView(RequireMessageMixin, ListView, TaskFilter):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get(self, request, *args, **kwargs):
        f = TaskFilter(
            request.GET, 
            queryset=Task.objects.all(), 
            request=request
        )
        return render(
            request,
            'tasks/filter.html',
            {'filter': f}
        )


# path 'create/'
class TaskCreateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {
            "form": form,
            "button": _("Create"),
        }
        return render(request, "tasks/create.html", context)
        
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST or None, user=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("The task was created successfully"))
            return redirect('tasks:index') 
        context = {
            'form': form,
            'button': _("Create"),
        }
        return render(request, 'tasks/create.html', context)


# path 'delete'
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


# path 'update/'
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
    

# class TaskFilterView(FilterView):
#     def get(self, request, *args, **kwargs):
#         f = TaskFilter(
#             request.GET, 
#             queryset=Task.objects.all(), 
#             request=request
#         )
#         return render(
#             request,
#             'tasks/filter.html',
#             {'filter': f}
#         )