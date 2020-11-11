from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm
from .models import *

def home(request):
    advertised_events = [event.getEvent() for event in Advertisement.objects.all()[:4]]
    all_events = Event.objects.all()[:6]
    context = {
        'events': advertised_events,
        'all_events': all_events
    }
    return render(request, 'ems/home.html', context)


def users(request):
    participants1 = Participant.objects.all()[0::2]
    participants2 = Participant.objects.all()[1::2]
    context = {
        'participants1': participants1,
        'participants2': participants2,
    }
    return render(request, 'ems/user.html', context)


def events(request):
    events1 = Event.objects.all()[0::2]
    events2 = Event.objects.all()[1::2]
    context = {
        'events1': events1,
        'events2': events2
    }
    return render(request, 'ems/events.html', context)


def createEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    context = {
        'form': form
    }
    return render(request, 'forms/create_event.html', context)

def create_participant(request):

    return render(request, 'ems/create_user.html')


def organisers(request):
    organisers1 = Organiser.objects.all()[0::2]
    organisers2 = Organiser.objects.all()[1::2]
    context = {
        'organisers1': organisers1,
        'organisers2': organisers2
    }
    return render(request, 'ems/organisers.html', context)


def shippers(request):
    return HttpResponse('shippers')


def store(request):
    return HttpResponse('store')