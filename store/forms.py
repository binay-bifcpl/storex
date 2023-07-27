# store/forms.py

from django import forms
from .models import StoreEntry
from .models import Usage

class StoreEntryForm(forms.ModelForm):
    class Meta:
        model = StoreEntry
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


# store/forms.py


class UsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
