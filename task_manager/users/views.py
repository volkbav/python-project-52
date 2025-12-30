# task_manager/users/views.py
# Create your views here.
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from task_manager.mixins import (
    UserPermissionMixin,
    UserServerPermissionMixin,
)

from .forms import UserFormCreate


# path ''
class UsersIndexView(UserServerPermissionMixin, ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


# path 'create/'
class UserCreateView(UserServerPermissionMixin, View):
    def get(self, request, *args, **kwargs):
        form = UserFormCreate()
        context = {
            'form': form,
            'button': _("Register"),
        }
        return render(request, "users/create.html", context)
        
    def post(self, request, *args, **kwargs):
        form = UserFormCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("User successfully registered"))
            return redirect('login')
        context = {
            'form': form,
            'button': _("Register"),
        }

        return render(request, 'users/create.html', context)


# path 'delete'
class UserDeleteView(UserPermissionMixin, View):
    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        username = User.objects.get(pk=user_pk).username
        context = {
            "user_pk": user_pk,
            "username": username,
        }
        return render(
            request,
            "users/delete.html",
            context
        )
    
    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        if user:
            try:
                user.delete()
            except ProtectedError:
                messages.error(
                    request,
                    _("It is not possible to delete a user "
                        "because it is being used"))
                return redirect('users:index')
            messages.success(request, _("User successfully deleted"))
            return redirect('users:index')  # Редирект на указанный маршрут
        messages.error(request, _('Oops'))
        return redirect('users:index')


# path 'update/'
class UserUpdateView(UserPermissionMixin, View):
    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        form = UserFormCreate(instance=user)
        context = {
            "form": form,
            "user_pk": user_pk,
            "button": _("Edit"),
        }
        return render(
            request,
            "users/update.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        
        if request.user.pk != user_pk:
            raise PermissionDenied()
        user = User.objects.get(pk=user_pk)
        form = UserFormCreate(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("User successfully edited"))
            return redirect('users:index')
        
        context = {
            'form': form,
            "button": _("Edit"),
        }
        return render(request, 'users/update.html', context)

