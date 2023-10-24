```python
import uuid
from BarterAI.technical_requirements.security_functions import hash_password

class User:
    def __init__(self, username, password, email):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password = hash_password(password)
        self.email = email
        self.trade_history = []
        self.wishlist = []

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_trade_history(self):
        return self.trade_history

    def get_wishlist(self):
        return self.wishlist

def register_user(username, password, email):
    new_user = User(username, password, email)
    # Save the user data to the database
    # This function should be implemented in the cloud_storage.py file
    save_user_data(new_user)
    return new_user
```