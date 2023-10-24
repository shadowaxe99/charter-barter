```python
import os
from cloud_storage import upload_to_cloud
from user_data_schema import User, Item

def upload_item(user_id, item_details):
    """
    Function to upload item details and images to the cloud storage
    """
    # Create an Item instance
    item = Item(user_id=user_id, **item_details)

    # Upload item images to cloud storage
    for image in item_details['images']:
        image_path = os.path.join('user_items', str(user_id), str(item.id), image)
        item.image_urls.append(upload_to_cloud(image_path))

    # Save item to database
    item.save()

    return item.id

def update_item(user_id, item_id, item_details):
    """
    Function to update item details and images
    """
    # Fetch the item from database
    item = Item.objects.get(id=item_id, user_id=user_id)

    # Update item details
    for key, value in item_details.items():
        if key != 'images':
            setattr(item, key, value)

    # Upload new images to cloud storage
    for image in item_details.get('images', []):
        image_path = os.path.join('user_items', str(user_id), str(item.id), image)
        item.image_urls.append(upload_to_cloud(image_path))

    # Save updated item to database
    item.save()

    return item.id
```