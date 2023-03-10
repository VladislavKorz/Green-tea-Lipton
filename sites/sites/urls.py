"""sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import error_404,error_500

handler404 = error_404
handler500 = error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('notification/',include('notification.urls')),
    path('account/', include('users.urls')),
    path('road-maps/', include('roadMaps.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('tasks/', include('tasks.urls')),
    path('ads/', include('ads.urls') ),
    path('faq/', include('faq.urls')),
    path('knowledgebase/', include('knowledgebase.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
