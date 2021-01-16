from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
        )


class LoginForm:
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
