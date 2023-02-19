from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from knowledgebase.views import *



urlpatterns = [
    path('', knowledgebase, name='knowledgebase' )
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)