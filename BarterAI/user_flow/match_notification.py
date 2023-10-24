```python
import json
from BarterAI.ai_matchmaking_engine import AIModel
from BarterAI.user_profile_and_listings import UserDataSchema
from BarterAI.technical_requirements import MessagingSystem

class MatchNotification:
    def __init__(self):
        self.ai_model = AIModel()
        self.user_data = UserDataSchema()
        self.messaging_system = MessagingSystem()

    def get_potential_matches(self, user_id):
        user_preferences = self.user_data.get_user_preferences(user_id)
        potential_matches = self.ai_model.get_matches(user_preferences)
        return potential_matches

    def send_match_notifications(self, user_id):
        potential_matches = self.get_potential_matches(user_id)
        for match in potential_matches:
            message = self.format_match_message(match)
            self.messaging_system.send_message(user_id, message)

    def format_match_message(self, match):
        item_name = match['item_name']
        match_user_id = match['match_user_id']
        match_item_name = match['match_item_name']
        message = f"You have a new match! User {match_user_id} is interested in trading their {match_item_name} for your {item_name}."
        return message
```