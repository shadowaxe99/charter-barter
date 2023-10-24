```python
from BarterAI.user_profile_and_listings.trade_history import TradeHistory
from BarterAI.technical_requirements.messaging_system import MessagingSystem

class FeedbackAndRating:
    def __init__(self, user_id, trade_id):
        self.user_id = user_id
        self.trade_id = trade_id
        self.trade_history = TradeHistory(user_id)
        self.messaging_system = MessagingSystem()

    def leave_feedback(self, feedback_text, rating):
        trade = self.trade_history.get_trade(self.trade_id)
        if not trade:
            return "Trade not found."

        trade['feedback'] = feedback_text
        trade['rating'] = rating
        self.trade_history.update_trade(self.trade_id, trade)

        self.messaging_system.send_message(self.user_id, "Thank you for your feedback!")

    def get_feedback(self):
        trade = self.trade_history.get_trade(self.trade_id)
        if not trade:
            return "Trade not found."

        return trade['feedback'], trade['rating']
```