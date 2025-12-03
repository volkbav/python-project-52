from django.urls import path

from task_manager.statuses.views import StatusIndexView

app_name = 'statuses'

urlpatterns = [
    path('', StatusIndexView.as_view(), name='statuses'),
]