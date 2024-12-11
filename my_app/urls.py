# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.websocket_notifications, name='websocket_notifications'),
    path('send_message/', views.send_message_to_websocket, name='send_message'),
]
