from django.forms import ModelForm
from django.forms import fields
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'organiser',
            'description',
            'category',
            'event_date'
        ]
