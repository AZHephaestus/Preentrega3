from django import forms

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