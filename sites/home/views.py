from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'title': "Привет",
    }
    return render(request,'home/index.html', context)

def calendar(request):
    context = {
        'title': "Календарь",
    }
    return render(request,'home/calendar.html', context)