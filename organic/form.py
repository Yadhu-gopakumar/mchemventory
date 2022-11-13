from django import forms
from .models import organic

class oganicUpdate(forms.ModelForm):
    class Meta:
        model=organic
        fields=['name','company','qty','price']