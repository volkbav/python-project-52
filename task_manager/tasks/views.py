from django.contrib import messages

# from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

# from .forms import TaskFormCreate
# from task_manager.mixins import RequireMessageMixin
from .models import Task


# Create your views here.
# path ''
class TasksIndexView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"


# # path 'create/'
# class StatusCreateView(RequireMessageMixin, View):
#     def get(self, request, *args, **kwargs):
#         form = StatusForm()
#         context = {
#             "form": form,
#             "button": _("Create"),
#         }
#         return render(request, "statuses/create.html", context)
        
#     def post(self, request, *args, **kwargs):
#         form = StatusForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, _("The status was created successfully"))
#             return redirect('statuses:statuses') 
#         context = {
#             'form': form,
#             'button': _("Create"),
#         }
#         return render(request, 'statuses/create.html', context)


# # path 'delete'
# class StatusDeleteView(RequireMessageMixin, View):
#     def get(self, request, *args, **kwargs):
#         status_pk = kwargs.get('pk')
#         name = Status.objects.get(pk=status_pk).name
#         context = {
#             "status_pk": status_pk,
#             "name": name,
#         }
#         return render(
#             request,
#             "statuses/delete.html",
#             context
#         )
    
#     def post(self, request, *args, **kwargs):
#         status_pk = kwargs.get('pk')
#         status = Status.objects.get(pk=status_pk)
#         if status:
#             status.delete()
#             messages.success(request, _("Status successfully deleted"))
#             return redirect('statuses:statuses')
#         messages.error(request, _('Oops'))
#         return redirect('statuses:statuses')


# # path 'update/'
# class StatusUpdateView(RequireMessageMixin, View):
#     def get(self, request, *args, **kwargs):
#         status_pk = kwargs.get('pk')
#         status = Status.objects.get(pk=status_pk)
#         form = StatusForm(instance=status)
#         context = {
#             "form": form,
#             "status_pk": status_pk,
#             "button": _("Edit"),
#         }
#         return render(
#             request,
#             "statuses/update.html",
#             context,
#         )

#     def post(self, request, *args, **kwargs):
#         status_pk = kwargs.get('pk')
        
#         status = Status.objects.get(pk=status_pk)
#         form = StatusForm(request.POST, instance=status)
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, _("Status successfully edited"))
#             return redirect('statuses:statuses')
#         context = {
#             'form': form,
#             "button": _("Edit"),
#             }

#         return render(request, 'statuses/update.html', context)
    
