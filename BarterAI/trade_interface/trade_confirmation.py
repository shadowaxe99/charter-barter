```python
import json
from BarterAI.user_profile_and_listings.trade_history import TradeHistory
from BarterAI.technical_requirements.security_functions import verify_user, encrypt_data

class TradeConfirmation:
    def __init__(self, trade_id, user_id, trade_data_schema):
        self.trade_id = trade_id
        self.user_id = user_id
        self.trade_data_schema = trade_data_schema
        self.trade_history = TradeHistory()

    def confirm_trade(self):
        if not verify_user(self.user_id):
            return {"status": "error", "message": "User verification failed"}

        trade_data = self.trade_data_schema.validate_trade(self.trade_id)
        if not trade_data:
            return {"status": "error", "message": "Invalid trade data"}

        encrypted_trade_data = encrypt_data(json.dumps(trade_data))
        self.trade_history.add_trade(self.user_id, self.trade_id, encrypted_trade_data)

        return {"status": "success", "message": "Trade confirmed"}

    def get_trade_status(self):
        trade_status = self.trade_history.get_trade_status(self.user_id, self.trade_id)
        if not trade_status:
            return {"status": "error", "message": "Trade not found"}

        return {"status": "success", "trade_status": trade_status}
```