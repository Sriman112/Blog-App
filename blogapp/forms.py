from django import forms
from .models import blogpost

class blogform(forms.ModelForm):
    class Meta:
        model=blogpost
        fields=('title','body',)
