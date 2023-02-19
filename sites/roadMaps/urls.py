from django.urls import path
from .views import *

urlpatterns = [
    path('', roadMapsViews, name='roadMaps'),
    path('old/', roadMapsViewsOld, name='roadMapsOld'),
    path('<int:pk>', roadMapsSingle, name='roadMapsSingle'),
]
