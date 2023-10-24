```python
from BarterAI.user_profile_and_listings.trade_history import TradeHistory
from BarterAI.technical_requirements.messaging_system import MessagingSystem
from BarterAI.technical_requirements.cloud_storage import CloudStorage

class FeedbackAndRating:
    def __init__(self, user_id, trade_id):
        self.user_id = user_id
        self.trade_id = trade_id
        self.trade_history = TradeHistory(user_id)
        self.messaging_system = MessagingSystem()
        self.cloud_storage = CloudStorage()

    def leave_feedback(self, feedback_text, rating):
        # Check if the user was part of the trade
        if not self.trade_history.was_user_part_of_trade(self.trade_id):
            return "User was not part of the trade."

        # Save feedback and rating to the trade history
        self.trade_history.save_feedback(self.trade_id, feedback_text, rating)

        # Notify the other user about the new feedback
        other_user_id = self.trade_history.get_other_user_id(self.trade_id)
        self.messaging_system.send_message(other_user_id, f"New feedback received for trade {self.trade_id}")

        return "Feedback and rating saved successfully."

    def view_feedback(self):
        # Retrieve feedback and rating from the trade history
        feedback, rating = self.trade_history.get_feedback_and_rating(self.trade_id)

        return feedback, rating
```