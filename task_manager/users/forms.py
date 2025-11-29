# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class UserFormCreate(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label=_("Password"),
        help_text=_("Your password must contain at least 3 characters.")
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label=_("Confirm password"),
        help_text=_("Please enter the password again to confirm.",)
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        labels = {
            'first_name': _("First name"),
            'last_name': _("Last name"),
            'username': _("Username"),
            'password': _("Password"),
        }
        help_texts = {
            'username': _(
                "Required field. No more than 150 characters. "
                "Only letters, numbers, and symbols @/./+/-/_."
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError(_("Passwords do not match"))

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user