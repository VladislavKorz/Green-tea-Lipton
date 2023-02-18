from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

@login_required
def roadMapsViews(request):
    context = {
        'title': "Карта уровней",
        'mapObj': guideAction.objects.all()
    }
    return render(request,'roadMaps/road_maps.html', context)

    
@xframe_options_exempt
def roadMapsSingle(request, pk):
    level = guideAction.objects.get(pk=pk)
    
    context = {
        'title': f"Уровень {level.order_count}",
        'level': level,
    }
    return render(request,'roadMaps/singleRM.html', context)
