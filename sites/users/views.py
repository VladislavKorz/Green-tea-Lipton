from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from users.forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required



class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        form = CustomAuthenticationForm()
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

def sync(request):
    return render(request,'users/sync.html')