from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ


def faq(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    
    return render(request, 'faq/faq_list.html', {'objlist': FAQ.objects.all()})