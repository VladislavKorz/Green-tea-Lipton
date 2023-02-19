
from django.shortcuts import render
from .models import KnowledgeBase, Category


def knowledgebase(request):
    categories = Category.objects.all()
    res=[]
    
    context = {
        'categories': categories,
    }
    print(context)
    return render(request, 'knowledgebase/knowledgebase.html', context=context)


