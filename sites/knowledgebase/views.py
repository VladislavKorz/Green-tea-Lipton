
from django.shortcuts import render
from .models import KnowledgeBase

# Общее!!!!!!!!!!

def KnowledgeBaseViews(request):
    context = {
        'title': "База знаний",
        # 'listObj': KnowledgeBase.objects.filter(category=request.user.profile.department)
        'listObj': KnowledgeBase.objects.all()
    }
    return render(request,'knowledgeBase/knowledgebase.html', context)

