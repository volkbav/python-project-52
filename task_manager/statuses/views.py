from django.shortcuts import render
from .models import Status
from django.views.generic import ListView

# Create your views here.

# path ''
class StatusIndexView(ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"