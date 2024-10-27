import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from notifications import routing
from shop_service.middleware import TokenAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_service.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
