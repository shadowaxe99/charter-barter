```python
from BarterAI.user_profile_and_listings.upload_items import upload_item
from BarterAI.technical_requirements.cloud_storage import save_to_cloud

class ItemListing:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def list_item(self, item_details):
        item_id = upload_item(item_details)
        self.items.append(item_id)
        save_to_cloud(self.user_id, self.items)

    def remove_item(self, item_id):
        if item_id in self.items:
            self.items.remove(item_id)
            save_to_cloud(self.user_id, self.items)

    def get_listed_items(self):
        return self.items
```