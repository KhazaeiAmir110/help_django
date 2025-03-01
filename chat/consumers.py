from channels.generic.websocket import WebsocketConsumer


class PriceConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
