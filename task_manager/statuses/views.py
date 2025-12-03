from django.views.generic import ListView

from .models import Status

# Create your views here.

# path ''
class StatusIndexView(ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"