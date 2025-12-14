# task_manager/views.py

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from .users.forms import UserFormLogin


class HomePageView(TemplateView):
    template_name = 'root.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = _('World')
        return context


class MyLoginView(LoginView):
    form_class = UserFormLogin
    template_name = "registration/login.html"

    def form_valid(self, form):
        messages.success(self.request, _("Logged in successfully"))
        return super().form_valid(form)
    

class MyLogoutView(LogoutView):
    next_page = 'login'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("You have logged out"))
        return super().dispatch(request, *args, **kwargs)

