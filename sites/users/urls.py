from django.urls import path
from users.views import *

urlpatterns = [
    path('', AccountView , name="account"),
    path('login/', LoginView.as_view(), name="login-form"),
    path('logout/', LogoutView.as_view(), name="logout"),
]