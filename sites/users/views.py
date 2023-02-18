from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from users.forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.decorators.csrf import csrf_exempt


class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        form = CustomAuthenticationForm()
        context = {
            'title':'Логин',
            'form':form,
        }
        try:
            context['user_id'] = kwargs['user_id']
        except:
            pass
        return render(request, 'users/login.html', {'form': form})

    
    def post(self, request, *args, **kwargs):
        form = CustomAuthenticationForm(data=request.POST)
        
        if form.is_valid():
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
        else:
            return render(request, 'users/login.html', {'form': form})

        return redirect('profile')

class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

    
    def post(self, request, *args, **kwargs):
        pass

@login_required
def AccountView(request):
    if request.user:
        profile = request.user.profile
    else:
        profile = None
    context = {
        'title': 'Профиль пользователя',
        'profile': profile
    }
    return render(request, 'users/profile.html', context)


@login_required
def ContactsView(request):
    context = {
        'title': 'Контакты',
        'contactAll': Profile.objects.all(),
        'contactDepartment': Profile.objects.filter(department=request.user.profile.department),
        'contactManagement': Profile.objects.filter(manager=True),
    }
    return render(request, 'users/contacts.html', context)


def sync(request,user_id):
    user_id = user_id.replace('%20','')
    if request.user.is_authenticated:
        current_user = request.user
        current_user.profile.telegram_id = user_id
        current_user.save()
        return redirect("profile")
    
    return redirect("profile")