```python
import datetime
from BarterAI.user_profile_and_listings import User

class Message:
    def __init__(self, sender_id, receiver_id, content):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.timestamp}: {self.content}"

class Chat:
    def __init__(self, user1_id, user2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.messages = []

    def send_message(self, sender_id, content):
        if sender_id not in [self.user1_id, self.user2_id]:
            raise ValueError("Sender not part of this chat")
        message = Message(sender_id, self.user2_id if sender_id == self.user1_id else self.user1_id, content)
        self.messages.append(message)

    def get_chat_history(self):
        return "\n".join(str(message) for message in self.messages)

class Negotiation:
    def __init__(self, user1_id, user2_id, item1_id, item2_id):
        self.chat = Chat(user1_id, user2_id)
        self.item1_id = item1_id
        self.item2_id = item2_id
        self.status = "ongoing"

    def negotiate(self, sender_id, content):
        if self.status != "ongoing":
            raise ValueError("Negotiation has ended")
        self.chat.send_message(sender_id, content)

    def accept_trade(self, user_id):
        if user_id not in [self.chat.user1_id, self.chat.user2_id]:
            raise ValueError("User not part of this negotiation")
        if self.status != "ongoing":
            raise ValueError("Negotiation has ended")
        self.status = "accepted" if user_id == self.chat.user1_id else "rejected"

    def get_negotiation_status(self):
        return self.status
```