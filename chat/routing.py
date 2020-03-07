from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # similar to django urls specefying which route will execute which consumer(similar to views in django)
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]