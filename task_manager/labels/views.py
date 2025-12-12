from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from task_manager.mixins import RequireMessageMixin

from .forms import LabelForm
from .models import Label


# Create your views here.
# path ''
class LabelsIndexView(RequireMessageMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = "labels"


# path 'create/'
class LabelCreateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = LabelForm()
        context = {
            "form": form,
            "button": _("Create"),
        }
        return render(request, "labels/create.html", context)
        
    def post(self, request, *args, **kwargs):
        form = LabelForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("The label was created successfully"))
            return redirect('labels:index') 
        context = {
            'form': form,
            'button': _("Create"),
        }
        return render(request, 'labels/create.html', context)


# path 'delete'
class LabelDeleteView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        name = Label.objects.get(pk=label_pk).name
        context = {
            "label_pk": label_pk,
            "name": name,
        }
        return render(
            request,
            "labels/delete.html",
            context
        )
    
    def post(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        label = Label.objects.get(pk=label_pk)
        if label.tasks.exists():
            messages.error(
                request,
                _("It is not possible to delete a label "
                    "because it is being used"))
            return redirect('labels:index')
        else:
            label.delete()
            messages.success(request, _("Label successfully deleted"))
            return redirect('labels:index')


# path 'update/'
class LabelUpdateView(RequireMessageMixin, View):
    def get(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        label = Label.objects.get(pk=label_pk)
        form = LabelForm(instance=label)
        context = {
            "form": form,
            "label_pk": label_pk,
            "button": _("Edit"),
        }
        return render(
            request,
            "labels/update.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        
        label = Label.objects.get(pk=label_pk)
        form = LabelForm(request.POST, instance=label)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("Label successfully edited"))
            return redirect('labels:index')
        context = {
            'form': form,
            "button": _("Edit"),
            }

        return render(request, 'labels/update.html', context)
    
