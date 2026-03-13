from django.urls import path

from .views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectsIndexView,
    ProjectUpdateView,
    ProjectView,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectsIndexView.as_view(), name='index'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete'),
    path('<int:pk>/', ProjectView.as_view(), name='project'), 
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='update'),
]