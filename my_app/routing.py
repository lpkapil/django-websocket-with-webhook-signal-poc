# myapp/routing.py

from django.urls import path
from my_app.consumers import MyWebSocketConsumer

websocket_urlpatterns = [
    path('ws/notifications/', MyWebSocketConsumer.as_asgi()),
]
