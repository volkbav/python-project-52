from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.functions import attrs_add

from .models import Status


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
        labels = {
            'name': _("Name"),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': _("Name")
        }
        
        attrs_add(self.fields, placeholders)

