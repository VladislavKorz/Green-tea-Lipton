from django.urls import path, include
from users.views import LoginView, LogoutView, AccountView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', LoginView.as_view(), name="login-form"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', AccountView.as_view() , name="account"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)