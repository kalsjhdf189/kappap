from django.urls import path
from pr5 import views

urlpatterns = [
    path('', views.index),
]
