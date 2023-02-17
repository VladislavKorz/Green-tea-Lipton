from django.urls import path, include
from users.views import LoginView, LogoutView, AccountView


urlpatterns = [
    path('login/', LoginView.as_view(), name="login-form"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', AccountView.as_view() , name="account"),
]