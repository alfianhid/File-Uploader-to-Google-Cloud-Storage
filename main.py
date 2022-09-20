# Import libraries
from google.cloud import storage
import urllib.request

# Define variables
project_id = 'data-fellowship-batch-7'
bucket_name = 'datafellowship-batch7'
destination_blob_name = 'materi-kuliah-umum-big-data.pdf'
source_file_name = 'http://www.pasca.ugm.ac.id/download/20181127041448Materi%20Kuliah%20Umum%20Pak%20Mardhani.pdf'
storage_client = storage.Client.from_service_account_json('data-fellowship-batch-7-eb3bce6ce8c5.json')

# Define upload function
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    file = urllib.request.Request(source_file_name, headers={'User-Agent': 'Mozilla/5.0'})   
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    name = urllib.request.urlopen(file).read()
    blob.upload_from_string(name, content_type='application/pdf')
    print("File uploaded successfully!")

# Run the function
upload_blob(bucket_name, source_file_name, destination_blob_name)