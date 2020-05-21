from django import forms
from .models import linksave

class linksavelist(forms.ModelForm):
    class Meta:
        model = linksave
        fields = ["title","link","currentuser"]
        