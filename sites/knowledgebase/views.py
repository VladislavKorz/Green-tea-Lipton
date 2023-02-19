
from django.shortcuts import render
from .models import KnowledgeBase


def KnowledgeBase(request):
    context = {
        'title': "Обьявления",
    }
    return render(request,'KnowledgeBase/knowledgebase.html', context)

