from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.urls import reverse

@login_required
def roadMapsViews(request):
    context = {
        'title': "Карта уровней",
        'mapObj': guideAction.objects.all()
    }
    return render(request,'roadMaps/road_maps.html', context)

    
@login_required
def roadMapsViewsOld(request):
    context = {
        'title': "Карта уровней",
        'mapObj': guideAction.objects.all()
    }
    return render(request,'roadMaps/road_mapsOld.html', context)

    
@xframe_options_exempt
def roadMapsSingle(request, pk):
    level = guideAction.objects.get(pk=pk)
    
    context = {
        'title': f"Уровень {level.order_count}",
        'level': level,
        'compl': UserguideAction.objects.filter(user = request.user.profile, guideAction = level).first()
    }
    return render(request,'roadMaps/singleRM.html', context)

    
@login_required
def roadMapsComplied(request, pk):
    level = guideAction.objects.get(pk=pk)
    UserguideAction.objects.get_or_create(guideAction=level, user=request.user.profile)
    return redirect("roadMaps")