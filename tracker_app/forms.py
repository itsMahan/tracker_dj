from django import forms
from .models import Tracker


class TrackerUpdateForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['name', 'start_date', 'end_date']