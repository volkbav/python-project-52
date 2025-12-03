from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin


class UserPermissionMixin(LoginRequiredMixin):

    # LoginRequiredMixin
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in."))
            return redirect("login")

        user_pk = kwargs.get("pk")
        if request.user.pk != user_pk:
            messages.error(request, _("You don't have the rights to change another user."))
            return redirect("users:users")

        return super().dispatch(request, *args, **kwargs)
