from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
