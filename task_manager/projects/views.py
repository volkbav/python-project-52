# task_manager/projects/views.py
# from django.contrib import messages
from django.http import Http404
from django.shortcuts import render  # redirect, 
from django.views import View
from django_filters.views import FilterView

from task_manager.mixins import (
    LoginRequiredMixin,
    ProjectPermissionMixin,
    RequireMessageMixin,
)

from .filter import TaskFilter
from .models import Project


# Create your views here.
class ProjectsIndexView(RequireMessageMixin, FilterView):
    model = Project
    template_name = "projects/index.html"
    filterset_class = TaskFilter


# path '<int:pk>/create/'
class ProjectCreateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {
            "form": form,
            "button": _("Create"),
        }
        return render(request, "tasks/create.html", context)
       
        
    def post(self, request, *args, **kwargs):  # noqa: E303
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
       


# path '<int:pk>/update/'
class ProjectUpdateView(LoginRequiredMixin, View):
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
       
    

# path '<int:pk>/delete'
class ProjectDeleteView(ProjectPermissionMixin, View):
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
        


# path '<int:pk>/'
class ProjectView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        project_pk = kwargs.get('pk')
        project = Project.objects.get(pk=project_pk)
        context = {
            "project": project,
        }
        return render(request, "projects/show_project.html", context)