from django.urls import path
from task_manager.users.views import UsersIndexView, UserFormCreateView


urlpatterns = [
    path('', UsersIndexView.as_view(), name='users'),
    path("create/", UserFormCreateView.as_view(), name="user_create"),
]