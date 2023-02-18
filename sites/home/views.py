from django.db.models import Q
from django.shortcuts import render
from .models import *
from faq.models import FAQ
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'title': "Привет",
    }
    return render(request,'home/index.html', context)
@login_required
def calendar(request):
    context = {
        'title': "Календарь",
    }
    return render(request,'home/calendar.html', context)




def search_faq(request):
    query = request.GET.get('q')
    if query:
        results = FAQ.objects.filter(
            Q(question__icontains=query) | Q(answer__icontains=query)
        )
    else:
        results = None
    return render(request, 'faq/faq_list.html', {'results': results})
