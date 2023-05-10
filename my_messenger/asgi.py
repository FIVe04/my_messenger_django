import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import my_messenger.chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_messenger.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            my_messenger.chat.routing.websocket_urlpatterns
        )
    )
})
