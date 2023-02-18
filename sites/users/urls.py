from django.urls import path
from users.views import *

urlpatterns = [
    path('', AccountView , name="profile"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]