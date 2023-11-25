from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('places/', views.place_list, name='placeList'),
    path('placecreate/', csrf_exempt(views.place_create), name='placeCreate'),
]