from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class RequireMessageMixin(LoginRequiredMixin):
    login_url = "login"

    def check_login(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in."))
            return redirect("login")
        return None
    
    def dispatch(self, request, *args, **kwargs):
        response = self.check_login(request)
        if response:
            return response
        
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(RequireMessageMixin):
    def dispatch(self, request, *args, **kwargs):
        response = self.check_login(request)
        if response:
            return response

        user_pk = kwargs.get("pk")
        if request.user.pk != user_pk:
            messages.error(
                request,
                _("You don't have the rights to change another user.")
                )
            return redirect("users:index")

        return super().dispatch(request, *args, **kwargs)
    

class UserServerPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        if settings.SERVER_LOCATION == 'internet':
            return self.request.user.is_authenticated and self.request.user.is_staff
        return True
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(
                    request,
                    _("To register, contact the site administrator")
                )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    
class TaskPermissionMixin(RequireMessageMixin):
    def dispatch(self, request, *args, **kwargs):
        response = self.check_login(request)
        if response:
            return response

        task_pk = kwargs.get("pk")
        task = Task.objects.get(pk=task_pk)
        if request.user != task.author:
            messages.error(
                request,
                _("A task can only be deleted by its author.")
                )
            return redirect("tasks:index")

        return super().dispatch(request, *args, **kwargs)
