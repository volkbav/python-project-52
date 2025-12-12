from django.urls import path

from .views import (
#     StatusCreateView,
#     StatusDeleteView,
    LabelsIndexView,
#     StatusUpdateView,
)

app_name = 'labels'

urlpatterns = [
    path('', LabelsIndexView.as_view(), name='labels'),
    # path('create/', StatusCreateView.as_view(), name='create'),
    # path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete'), 
    # path('<int:pk>/update/', StatusUpdateView.as_view(), name='update'),
]