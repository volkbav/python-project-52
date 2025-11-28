from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()[:15]
        return render(
            request,
            "users/index.html",
            context={
                "users": users,
            },
        )
