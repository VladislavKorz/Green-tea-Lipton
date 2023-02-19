from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from faq.models import FAQ
from django.contrib.auth.decorators import login_required
from users.models import Profile
from notification.management.commands.notificationBot import send_done_message_to_telegram_chat


@login_required
def index(request):
    context = {
        'title': "Привет",
    }
    return render(request,'home/dashboard.html', context)

@login_required
def calendar(request):
    context = {
        'title': "Календарь",
    }
    return render(request,'home/calendar.html', context)


@login_required
def search_faq(request):
    query = request.GET.get('q')
    if query:
        results = FAQ.objects.filter(
            Q(question__icontains=query) | Q(answer__icontains=query)
        )
    else:
        results = None
    return render(request, 'faq/faq_list.html', {'results': results, 'query': query})

def error_404(request, exception):
    data = {}
    return render(request, 'error_page/error-404.html', data, status=404)

def error_500(request):
    data = {}
    return render(request, 'error_page/error-500.html', data, status=500)


@login_required
def ratings(request):
    users = Profile.objects.filter(rols='NC')
    print(users)
    return render(request, 'home/ratings.html', {'users':users})

@login_required
def feedback(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient', '')
        title = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        profile = Profile.objects.get(user=request.user)
        name = profile.user.first_name
        last_name = profile.user.last_name
        department = profile.department

        if recipient == 'HR':
            dir_profile = department.profiles.filter(roles='HR').first()
            telgram_id = dir_profile.telegram_id

        if recipient == 'Manager':
            dir_profile = department.profiles.filter(roles='DIR').first()
            telgram_id = dir_profile.telegram_id
        
        if recipient == 'Support':
            telgram_id = '516884985'
        send_done_message_to_telegram_chat(
            telgram_id, compose_msg(name, last_name, title, message))
        
        # redirect to the same page with a success message
        return redirect(request.META.get('HTTP_REFERER'))


def compose_msg(name,last_name,title,message): 
    msg = f'Сообщение от {name}, {last_name}:\n{title.capitalize()}\n{message}'
    return msg
