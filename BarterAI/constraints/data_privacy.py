```python
import os
from cryptography.fernet import Fernet

class DataPrivacy:
    def __init__(self):
        self.key = os.getenv('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        """Encrypts the user data"""
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypts the user data"""
        decrypted_data = self.cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

    def store_data(self, user_id, data):
        """Stores the user data in encrypted form"""
        encrypted_data = self.encrypt_data(data)
        # Store the encrypted data in the database
        # db.store(user_id, encrypted_data)

    def retrieve_data(self, user_id):
        """Retrieves and decrypts the user data"""
        # Retrieve the encrypted data from the database
        # encrypted_data = db.retrieve(user_id)
        # decrypted_data = self.decrypt_data(encrypted_data)
        # return decrypted_data
```
This code provides a class `DataPrivacy` that handles encryption and decryption of user data to ensure privacy and GDPR compliance. The actual database operations are commented out as they would depend on the specific database being used.