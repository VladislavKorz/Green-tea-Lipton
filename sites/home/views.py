from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'title': "Привет",
    }
    return render(request,'home/dashboard.html', context)
@login_required
def calendar(request):
    context = {
        'title': "Календарь",
    }
    return render(request,'home/calendar.html', context)