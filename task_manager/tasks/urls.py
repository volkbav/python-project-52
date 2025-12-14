from django.urls import path


from .views import (
    TaskCreateView,
    TaskDeleteView,
    TasksIndexView,
    TaskUpdateView,
    # TaskFilterView
)

app_name = 'tasks'

urlpatterns = [
    path('', TasksIndexView.as_view(), name='index'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'), 
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    # temp path
    # path('filter/', TaskFilterView.as_view(), name='filter')
]