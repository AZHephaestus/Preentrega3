from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class gameform(forms.ModelForm):
    class Meta:
        model = models.game
        fields = "__all__"


class genreform(forms.ModelForm):
    class Meta:
        model = models.gamegenre
        fields = "__all__"

class gamebygenreform(forms.ModelForm):
    class Meta:
        model = models.gamebygenre
        fields = "__all__"

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model= User
        fields= ["username", "password"]
        widgets = {
        "username": forms.TextInput(attrs={"class": "formcontrol"}),
        "password": forms.PasswordInput(attrs={"class": "formcontrol"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ["username", "password1", "password2"]
        widgets = {
        "username": forms.TextInput(attrs={"class": "formcontrol"}),
        "password1": forms.PasswordInput(attrs={"class": "formcontrol"}),
        "password2": forms.PasswordInput(attrs={"class": "formcontrol"}),
        }