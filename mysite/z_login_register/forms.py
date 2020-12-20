from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


'''Este archivo es creado a pedales para "customizar" el formulario
predeterminado que Django ofrece para crear usuarios'''

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']