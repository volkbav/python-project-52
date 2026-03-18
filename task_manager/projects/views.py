# task_manager/projects/views.py
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views import View
from django_filters.views import FilterView

from task_manager.mixins import (
    LoginRequiredMixin,
    ProjectPermissionMixin,
    RequireMessageMixin,
)

from .filter import ProjectFilter
from .forms import ProjectForm
from .models import Project


# Create your views here.
class ProjectsIndexView(RequireMessageMixin, FilterView):
    model = Project
    template_name = "projects/index.html"
    filterset_class = ProjectFilter


# path '<int:pk>/create/'
class ProjectCreateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = ProjectForm()
        context = {
            "form": form,
            "button": _("Create"),
        }
        return render(request, "projects/create.html", context)
       
        
    def post(self, request, *args, **kwargs):  # noqa: E303
        form = ProjectForm(request.POST or None, user=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("The project was created successfully"))
            return redirect('projects:index') 
        context = {
            'form': form,
            'button': _("Create"),
        }
        return render(request, 'projects/create.html', context)
       

# path '<int:pk>/update/'
class ProjectUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        project_pk = kwargs.get('pk')
        project = Project.objects.get(pk=project_pk)
        form = ProjectForm(instance=project)
        context = {
            "form": form,
            "project_pk":project_pk,
            "button": _("Edit"),
        }
        return render(
            request,
            "projects/update.html",
            context,
        )  

    def post(self, request, *args, **kwargs):
        project_pk = kwargs.get('pk')
        
        project = Project.objects.get(pk=project_pk)
        form = ProjectForm(request.POST, instance=project)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("Project successfully edited"))
            return redirect('projects:index')
        context = {
            'form': form,
            "button": _("Edit"),
            }

        return render(request, 'projects/update.html', context)
       
    

# path '<int:pk>/delete'
class ProjectDeleteView(ProjectPermissionMixin, View):
    def get(self, request, *args, **kwargs):
        project_pk = kwargs.get('pk')
        project = Project.objects.get(pk=project_pk)
        context = {
            "project_pk": project_pk,
            "name": project.name,
        }
        return render(
            request,
            "projects/delete.html",
            context
        )
        
    
    def post(self, request, *args, **kwargs):
        project_pk = kwargs.get('pk')
        project = Project.objects.get(pk=project_pk)
        if project:
            project.delete()
            messages.success(request, _("Project successfully deleted"))
            return redirect('projects:index')
        messages.error(request, _('Oops'))
        return redirect('projects:index')
        


# path '<int:pk>/'
class ProjectView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        project_pk = kwargs.get('pk')
        project = Project.objects.get(pk=project_pk)
        context = {
            "project": project,
        }
        return render(request, "projects/show_project.html", context)