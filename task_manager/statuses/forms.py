from django.forms import ModelForm
from .models import Status
from django.utils.translation import gettext_lazy as _

class StatuseForm(ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
        labels = {
            'name': _("Name"),
        }
    
    """def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data"""