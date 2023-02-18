from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ, Category


def faq(request):
    categories = Category.objects.all()
    res=[]
    
    context = {
        'categories': categories,
    }
    print(context)
    return render(request, 'faq/faq_list.html', context=context)



