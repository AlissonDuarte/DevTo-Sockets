import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from socketapp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socketdevto.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.ws_urlpatterns
        )
    ),
})