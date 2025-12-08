# from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Task


# path ''
class TasksIndexView(ListView):
    model = Task
    template_name = "statuses/index.html"
    context_object_name = "statuses"