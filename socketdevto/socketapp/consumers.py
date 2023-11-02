import json
import time
from socketapp.models import *
from channels.generic.websocket import WebsocketConsumer


class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while '1' in Queue.objects.all().values_list('status', flat=True):
            self.send(text_data=json.dumps({"value":Random.objects.all().count()}))
            Random.objects.create(text = "test")
            time.sleep(2)
        self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data=text_data)
        self.close()