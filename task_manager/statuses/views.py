from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from task_manager.mixins import RequireMessageMixin

from .forms import StatusForm
from .models import Status


# Create your views here.
# path ''
class StatusIndexView(RequireMessageMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"


# path 'create/'
class StatusCreateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        context = {
            "form": form,
            "button": _("Create"),
        }
        return render(request, "statuses/create.html", context)
        
    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("The status was created successfully"))
            return redirect('statuses:index') 
        context = {
            'form': form,
            'button': _("Create"),
        }
        return render(request, 'statuses/create.html', context)


# path 'delete'
class StatusDeleteView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        name = Status.objects.get(pk=status_pk).name
        context = {
            "status_pk": status_pk,
            "name": name,
        }
        return render(
            request,
            "statuses/delete.html",
            context
        )
    
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = Status.objects.get(pk=status_pk)
        if status:
            try:
                status.delete()
            except ProtectedError:
                messages.error(
                    request,
                    _("It is not possible to delete a status "
                        "because it is being used"))
                return redirect('statuses:index')
            messages.success(request, _("Status successfully deleted"))
            return redirect('statuses:index')
        messages.error(request, _('Oops'))
        return redirect('statuses:index')


# path 'update/'
class StatusUpdateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = Status.objects.get(pk=status_pk)
        form = StatusForm(instance=status)
        context = {
            "form": form,
            "status_pk": status_pk,
            "button": _("Edit"),
        }
        return render(
            request,
            "statuses/update.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        
        status = Status.objects.get(pk=status_pk)
        form = StatusForm(request.POST, instance=status)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("Status successfully edited"))
            return redirect('statuses:index')
        context = {
            'form': form,
            "button": _("Edit"),
            }

        return render(request, 'statuses/update.html', context)
    
