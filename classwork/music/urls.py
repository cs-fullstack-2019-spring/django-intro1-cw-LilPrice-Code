# Sending routes
from django.urls import path

from . import views

urlpatterns = [
    path('micheal/', views.micheal, name='index'),
    path('johnny/', views.johnny, name='index'),
    path('prince/', views.prince, name='index'),
]