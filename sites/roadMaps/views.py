from django.shortcuts import render
from .models import *

def roadMapsViews(request):
    context = {
        'title': "Карта уровней",
        'mapObj': guideAction.objects.all()
    }
    return render(request,'home/road_maps.html', context)
