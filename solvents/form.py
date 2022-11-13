from django import forms
from .models import solvents

class solventUpdate(forms.ModelForm):
    class Meta:
        model=solvents
        fields=['name','company','qty','price']