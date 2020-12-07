import json
import channels
from channels.generic.websocket import AsyncWebsocketConsumer
import time
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        self.user = await channels.auth.get_user(self.scope)
        print("connected")
        self.sendtime =  time.time_ns()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'latency',
                'user' : self.user.username
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("disconnected")
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msgtype = text_data_json['type']
        user = text_data_json['user']
        if(msgtype == 'msg'):
            message = text_data_json['message']
            print(text_data_json)
            print(message)
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'user': user,
                    'message': message
                }
            )
        elif msgtype == 'played':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'played',
                    'user': user,
                }
            )
        elif msgtype == 'paused':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'paused',
                    'user': user,
                }
            )
        elif msgtype == 'latency':
            recievetime =  time.time_ns()
            self.latencytime = (recievetime - self.sendtime)/2
            print(self.user.username)
            print(self.latencytime/10**9)

    # Receive message from room group
    async def paused(self, event):
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type':"paused",
            'user': user,
        }))
    
    async def played(self, event):
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type':"played",
            'user': user,
        }))
    
    async def latency(self, event):
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type':"latency",
            'user': user,
        }))
    