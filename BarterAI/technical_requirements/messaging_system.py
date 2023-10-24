```python
import asyncio
from aiohttp import web
import json

class MessagingSystem:

    def __init__(self):
        self.users = {}  # {user_id: websocket}

    async def register(self, websocket, user_id):
        self.users[user_id] = websocket

    async def unregister(self, websocket, user_id):
        del self.users[user_id]

    async def send_message(self, sender_id, receiver_id, message):
        if receiver_id in self.users:
            await self.users[receiver_id].send_json({
                'sender_id': sender_id,
                'message': message
            })

    async def handle_websocket(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        user_id = request.match_info.get('user_id')
        await self.register(ws, user_id)

        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                data = json.loads(msg.data)
                await self.send_message(user_id, data['receiver_id'], data['message'])

        await self.unregister(ws, user_id)

        return ws

messaging_system = MessagingSystem()
app = web.Application()
app.router.add_route('GET', '/ws/{user_id}', messaging_system.handle_websocket)

web.run_app(app)
```