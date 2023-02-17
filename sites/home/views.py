from django.shortcuts import render

def index(request):
    context = {
        'title': "Привет"
    }
    return render(request,'home/index.html', context)
