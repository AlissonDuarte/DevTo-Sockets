from django.urls import path

from . import consumers

ws_urlpatterns = [
    path("ws/test/", consumers.Consumer.as_asgi())
]