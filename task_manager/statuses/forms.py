from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Status


class StatuseForm(ModelForm):
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
        
        for name, field in self.fields.items():
            field.widget.attrs.setdefault('class', 'form-control')
            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]

    