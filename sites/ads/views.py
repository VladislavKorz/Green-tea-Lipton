from django.shortcuts import render, get_object_or_404
from .models import Advertisement


def faq(request, pk):
    faq = get_object_or_404(Advertisement, pk=pk)
    
    return render(request, 'ads/index.html', {'objlist': Advertisement.objects.all()})