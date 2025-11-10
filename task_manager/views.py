# task_manager/views.py
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'root.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = _('World')
        return context

