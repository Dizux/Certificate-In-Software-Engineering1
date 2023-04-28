from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('capture_message', views.capture_message, name='capture_message'),
]