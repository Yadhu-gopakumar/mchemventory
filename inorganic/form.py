from django import forms
from .models import inorganic

class inoganicUpdate(forms.ModelForm):
    class Meta:
        model=inorganic
        fields=['name','company','qty','price']