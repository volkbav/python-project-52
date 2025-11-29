
# Create your views here.
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from .forms import UserFormCreate


# path ''
class UsersIndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


# path 'create/
class UserFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserFormCreate()
        return render(request, "users/create.html", {"form": form})
        
    def post(self, request, *args, **kwargs):
        form = UserFormCreate(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('users')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно 
        # на страницу с заполненной формой
        return render(request, 'users/create.html', {'form': form})