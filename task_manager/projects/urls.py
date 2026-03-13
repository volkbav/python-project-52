from django.urls import path

from .views import (
    # TaskCreateView,
    # TaskDeleteView,
    ProjectsIndexView,
    # TaskUpdateView,
    # TaskView,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectsIndexView.as_view(), name='index'),
    # path('create/', TaskCreateView.as_view(), name='create'),
    # path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    # path('<int:pk>/', TaskView.as_view(), name='task'), 
    # path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
]