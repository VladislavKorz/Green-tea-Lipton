from django.shortcuts import render

def roadMapsViews(request):
    context = {
        'title': "Карта уровней"
    }
    return render(request,'home/road_maps.html', context)
