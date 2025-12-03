from django.urls import path

from task_manager.users.forms import UserFormLogin
from task_manager.users.views import (
    MyLoginView,
    MyLogoutView,
    UserCreateView,
    UsersIndexView,
    UserUpdateView,
)

app_name = 'users'

urlpatterns = [
    path('', UsersIndexView.as_view(), name='users'),
    path("create/", UserCreateView.as_view(), name="create"),
    path('login/', MyLoginView.as_view(
        template_name="registration/login.html",
        authentication_form=UserFormLogin,
    ), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
]