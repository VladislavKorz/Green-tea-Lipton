from django.urls import path
from .views import *

urlpatterns = [
    path('', roadMapsViews, name='roadMaps'),
    path('<int:pk>', roadMapsSingle, name='roadMapsSingle'),
    
]
