from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'ems/home.html')


def users(request):
    return HttpResponse('Users')


def organisers(request):
    return HttpResponse('organisers')


def shippers(request):
    return HttpResponse('shippers')


def store(request):
    return HttpResponse('store')