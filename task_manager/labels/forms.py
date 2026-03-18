from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.utils import attrs_add

from .models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ["name"]
        labels = {
            'name': _("Name"),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        placeholders = {
            'name': _("Name")
        }
        
        attrs_add(self.fields, placeholders)

