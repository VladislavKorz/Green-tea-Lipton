from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def roadMapsViews(request):
    context = {
        'title': "Карта уровней",
        'mapObj': guideAction.objects.all()
    }
    return render(request,'roadMaps/road_maps.html', context)
@login_required
def roadMapsSingle(request, pk):
    context = {
        'title': "Карта уровней",
        'mapObj': guideAction.objects.all()
    }
    return render(request,'roadMaps/road_maps.html', context)
