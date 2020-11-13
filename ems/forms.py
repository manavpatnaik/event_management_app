from django.forms import ModelForm
from django.forms import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Event, Item, Organiser, Participant


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


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class OrganiserForm(ModelForm):
    class Meta:
        model = Organiser
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        exclude = ('user',)