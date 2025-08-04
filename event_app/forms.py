from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'total_events', 'used_events']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['total_events'].required = False
