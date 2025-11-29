# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm



class UserFormCreate(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm password"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user