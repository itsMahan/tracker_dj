from django import forms
from .models import Counter



class CounterUpdateForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['name', 'start_date']