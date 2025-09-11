    # myapp/forms.py
from django import forms
from .models import Dbs

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Dbs
        fields = ['name', 'image']