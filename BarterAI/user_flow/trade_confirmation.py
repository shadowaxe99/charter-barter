```python
import json
from BarterAI.technical_requirements.trade_confirmation_security import secure_trade

class TradeConfirmation:
    def __init__(self, trade_id, user_id, item_id):
        self.trade_id = trade_id
        self.user_id = user_id
        self.item_id = item_id

    def confirm_trade(self):
        # Load trade data
        with open('trade_data.json', 'r') as file:
            trade_data = json.load(file)

        # Check if trade exists and is pending
        if self.trade_id in trade_data and trade_data[self.trade_id]['status'] == 'pending':
            # Check if user is part of the trade
            if self.user_id in trade_data[self.trade_id]['users']:
                # Check if item is part of the trade
                if self.item_id in trade_data[self.trade_id]['items']:
                    # Secure the trade
                    secure_trade(self.trade_id)

                    # Update trade status to confirmed
                    trade_data[self.trade_id]['status'] = 'confirmed'

                    # Save trade data
                    with open('trade_data.json', 'w') as file:
                        json.dump(trade_data, file)

                    return "Trade confirmed successfully."
                else:
                    return "Item not part of the trade."
            else:
                return "User not part of the trade."
        else:
            return "Trade not found or already confirmed."

# Example usage
trade = TradeConfirmation('trade123', 'user456', 'item789')
print(trade.confirm_trade())
```