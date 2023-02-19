from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.urls import reverse
from django.db.models import Count

@login_required
def roadMapsViews(request):
    context = {}
    context['title']= "Карта уровней"
    context['mapObj'] =guideAction.objects.all()

    if request.user.profile.rols == "HR" or request.user.profile.rols == "DIR":
        context['extend'] = True
        guide_actions = guideAction.objects.annotate(user_count=Count('guideAction_users'))
        context['mapObj'] = guide_actions
        
            
    
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