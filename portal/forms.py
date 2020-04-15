from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _ 

class LoginUsuarioForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Usuario'}))
    password = forms.CharField(label=_("Clave"),
                                widget=forms.PasswordInput({
                                    'class': 'form-control',
                                    'placeholder': 'Clave'}))