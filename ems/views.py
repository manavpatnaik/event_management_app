from ems.decorators import allowed_users
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import EventForm, ItemForm, OrganiserForm, CreateUserForm
from .decorators import *
from .models import *


def selection(request):
    return render(request, 'auth/selection.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print(form.errors)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='participant')
                user.groups.add(group)
                Participant.objects.create(
                    user=user,
                )
                messages.success(request, 'Account created for ' + username )
                return redirect('login')
        context = {
            'form': form
        }
        return render(request, 'auth/registerParticipant.html', context)


def registerPageOrganiser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print(form.errors)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='organiser')
                user.groups.add(group)
                Organiser.objects.create(
                    user=user,
                )
                messages.success(request, 'Account created for ' + username )
                return redirect('login')
        context = {
            'form': form
        }
        return render(request, 'auth/registerOrganiser.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    advertised_events = [event.getEvent() for event in Advertisement.objects.all()[:4]]
    all_events = Event.objects.all()[:6]
    group = group = request.user.groups.all()[0].name
    context = {
        'events': advertised_events,
        'all_events': all_events,
        'group': group
    }
    return render(request, 'ems/home.html', context)


@login_required(login_url='login')
def editProfile(request, pk):
    participant = Participant.objects.get(id=pk)
    context = {
        'participant': participant
    }
    return render(request, 'ems/edit_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'participant', 'organiser'])
def users(request):
    participants1 = Participant.objects.all()[0::2]
    participants2 = Participant.objects.all()[1::2]
    context = {
        'participants1': participants1,
        'participants2': participants2,
    }
    return render(request, 'ems/users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'participant', 'organiser'])
def events(request):
    events1 = Event.objects.all()[0::2]
    events2 = Event.objects.all()[1::2]
    context = {
        'events1': events1,
        'events2': events2
    }
    return render(request, 'ems/events.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'organiser'])
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
    return render(request, 'forms/add_event.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'participant', 'organiser'])
def view_event(request, pk):
    event = Event.objects.get(id=pk)
    merchandise = event.organiser.item_set.all()
    context = {
        'event': event,
        'merchandise': merchandise
    }
    return render(request, 'ems/event.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_participant(request):

    return render(request, 'ems/add_participant.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'participant', 'organiser'])
def organisers(request):
    organisers1 = Organiser.objects.all()[0::2]
    organisers2 = Organiser.objects.all()[1::2]
    context = {
        'organisers1': organisers1,
        'organisers2': organisers2
    }
    return render(request, 'ems/organisers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrganiser(request):
    form = OrganiserForm()
    if request.method == 'POST':
        form = OrganiserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organisers')
    context = {
        'form': form
    }
    return render(request, 'forms/add_organiser.html', context)


@login_required(login_url='login')
def shippers(request):
    return HttpResponse('shippers')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'participant', 'organiser'])
def store(request):
    items1 = Item.objects.all()[0::2]
    items2 = Item.objects.all()[1::2]
    context = {
        'items1': items1,
        'items2': items2
    }
    return render(request, 'ems/store.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'organiser'])
def createItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    context = {
        'form': form
    }
    return render(request, 'forms/add_item.html', context)