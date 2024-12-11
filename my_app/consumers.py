# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        self.room_name = "notifications"  # Can be any name
        self.room_group_name = f'notifications_{self.room_name}'  # Group name

        # Join the WebSocket to the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name  # This is the unique channel name for this WebSocket connection
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group when the WebSocket disconnects
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Method to receive a message from WebSocket (client to server)
    async def receive(self, text_data):
        # Print the received message (optional)
        print(f"Received: {text_data}")

        # Send a response back to the WebSocket client
        await self.send(text_data=json.dumps({
            'message': 'Message received!'
        }))

    # Method to send messages from the server to WebSocket (this will be called by Django views)
    async def send_message(self, event):
        # Extract the message from the event (sent by the Django view)
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps(message))
