```python
import json

class TradeHistory:
    def __init__(self, user_id):
        self.user_id = user_id
        self.trade_data_schema = {
            "trade_id": "",
            "user_id": "",
            "traded_with": "",
            "user_item": "",
            "exchanged_item": "",
            "trade_date": "",
            "feedback": ""
        }

    def get_trade_history(self):
        try:
            with open(f'./user_data/{self.user_id}_trade_history.json', 'r') as file:
                trade_history = json.load(file)
                return trade_history
        except FileNotFoundError:
            return "No trade history found for this user."

    def add_trade(self, trade_data):
        trade_data = self.validate_trade_data(trade_data)
        if trade_data:
            try:
                with open(f'./user_data/{self.user_id}_trade_history.json', 'r') as file:
                    trade_history = json.load(file)
                    trade_history.append(trade_data)
                with open(f'./user_data/{self.user_id}_trade_history.json', 'w') as file:
                    json.dump(trade_history, file)
                return "Trade added to history."
            except FileNotFoundError:
                with open(f'./user_data/{self.user_id}_trade_history.json', 'w') as file:
                    json.dump([trade_data], file)
                return "Trade added to history."
        else:
            return "Invalid trade data."

    def validate_trade_data(self, trade_data):
        if all(key in trade_data for key in self.trade_data_schema):
            return trade_data
        else:
            return False
```