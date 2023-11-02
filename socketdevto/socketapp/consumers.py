import json
import time
from socketapp.models import *
from channels.generic.websocket import WebsocketConsumer


class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            self.send(text_data=json.dumps({"value":Random.objects.all().count()}))
            time.sleep(2)
        self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data=text_data)
        self.close()