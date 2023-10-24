```python
import boto3
from botocore.exceptions import NoCredentialsError

class CloudStorage:

    def __init__(self, access_key, secret_key, bucket_name):
        self.s3 = boto3.client('s3', aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key)
        self.bucket_name = bucket_name

    def upload_file(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name

        try:
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_file(self, object_name, file_name):
        try:
            self.s3.download_file(self.bucket_name, object_name, file_name)
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def list_files(self):
        files = []
        try:
            for file in self.s3.list_objects(Bucket=self.bucket_name)['Contents']:
                files.append(file['Key'])
            return files
        except NoCredentialsError:
            print("Credentials not available")
            return []
```
This Python code uses the boto3 library to interact with Amazon S3 for cloud storage. The CloudStorage class has methods to upload, download, and list files in a specified S3 bucket. The access key, secret key, and bucket name are passed when initializing the class. The upload_file and download_file methods take the local file name and the object name in the bucket as arguments. If the object name is not provided, the local file name is used. The list_files method returns a list of all files in the bucket.