# myproject/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from my_app.consumers import MyWebSocketConsumer
from django.urls import path
from my_app.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sse_demo.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # Handle WebSocket connections with authentication middleware
        URLRouter(websocket_urlpatterns)  # Use the routing patterns defined in `routing.py`
    ),
})
