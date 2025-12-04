
# Create your views here.
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from .forms import UserFormCreate
from .mixins import UserPermissionMixin


# path ''
class UsersIndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


# path 'create/'
class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserFormCreate()
        return render(request, "users/create.html", {"form": form})
        
    def post(self, request, *args, **kwargs):
        form = UserFormCreate(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, _("User created"))
            return redirect('login')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно 
        # на страницу с заполненной формой
        return render(request, 'users/create.html', {'form': form})


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
            user.delete()
            messages.success(request, _("User successfully deleted"))
            return redirect('users:users')  # Редирект на указанный маршрут
        messages.error(request, _('Ooops'))
        return redirect('users:users')


# path 'update/'
class UserUpdateView(UserPermissionMixin, View):
    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        form = UserFormCreate(instance=user)
        return render(
            request,
            "users/update.html",
            {
                "form": form,
                "user_pk": user_pk
            }
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
            return redirect('users:users')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно 
        # на страницу с заполненной формой
        return render(request, 'users/update.html', {'form': form})
    
