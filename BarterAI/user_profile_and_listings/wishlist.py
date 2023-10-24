```python
class Wishlist:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_item(self, item_id):
        if item_id not in self.items:
            self.items.append(item_id)

    def remove_item(self, item_id):
        if item_id in self.items:
            self.items.remove(item_id)

    def get_items(self):
        return self.items

    def clear_wishlist(self):
        self.items = []

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.wishlist = Wishlist(user_id)

    def add_item_to_wishlist(self, item_id):
        self.wishlist.add_item(item_id)

    def remove_item_from_wishlist(self, item_id):
        self.wishlist.remove_item(item_id)

    def get_wishlist(self):
        return self.wishlist.get_items()

    def clear_wishlist(self):
        self.wishlist.clear_wishlist()
```