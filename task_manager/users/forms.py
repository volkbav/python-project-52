# users/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.functions import attrs_add


class UserFormCreate(ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _("Password"),
        }),
        label=_("Password"),
        help_text=_("Your password must contain at least 3 characters.")
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _("Confirm password"),
        }),
        label=_("Confirm password"),
        help_text=_("Please enter the password again to confirm.",)
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label_suffix = ""
        placeholders = {
            'first_name': _("First name"),
            'last_name': _("Last name"),
            'username': _("Username"),
        }
        
        attrs_add(self.fields, placeholders)
        
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'password1', 
            'password2'
        ]
        labels = {
            'first_name': _("First name"),
            'last_name': _("Last name"),
            'username': _("Username"),
            'password1': _("Password"),
        }
        help_texts = {
            'username': _(
                "Required field. No more than 150 characters. "
                "Only letters, numbers, and symbols @/./+/-/_."
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", _("Passwords do not match"))
        elif password1 and len(password1) < 3:
            self.add_error("password2", _(
                "The entered password is too short. "
                "It must contain at least 3 characters."))
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    

class UserFormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if name == 'username':
                field.widget.attrs['placeholder'] = _("Имя пользователя")
            elif name == 'password':
                field.widget.attrs['placeholder'] = _("Пароль")

        
