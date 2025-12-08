from django.urls import path

from .views import (
    TaskCreateView,
    # StatusDeleteView,
    # StatusUpdateView,
    TasksIndexView,
)

app_name = 'tasks'

urlpatterns = [
    path('', TasksIndexView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create'),
    # path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete'), 
    # path('<int:pk>/update/', StatusUpdateView.as_view(), name='update'),
]