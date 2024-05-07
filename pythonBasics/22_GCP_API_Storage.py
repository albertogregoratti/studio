# doc: https://cloud.google.com/storage/docs/listing-buckets
# doc: https://cloud.google.com/storage/docs/listing-objects

from google.cloud import storage

key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'   # File containing GCP key

# Instantiates a client
client_ref1 = storage.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials
project_ref1 = client_ref1.project

####################################################################################
# List all buckets within a project storage
buckets = client_ref1.list_buckets()
print('All buckets within ', project_ref1)
for b in buckets: print(b)

# List all files (blobs) within a bucket
files1 = client_ref1.list_blobs('freshdesk_gbq')
print('All files within freshdesk_gbq')
for i in files1: print(i.name)

####################################################################################
# Copy a file from one bucket into another
# Create a google cloud storage client
gs_client = storage.Client.from_service_account_json(key_path)

# Set a source
source_bucket = 'freshdesk_gbq'	    # Bucket
source_file = 'test1.json'    # SubFolder(s) within the bucket

# Set a target
target_bucket = 'aftership_test'	    # Bucket
target_file = 'test1.json'

# Get the source bucket and file
source_bucket_cl = gs_client.bucket(source_bucket)
source_blob = source_bucket_cl.blob(source_file)

# Get the destination bucket
target_bucket_cl = gs_client.bucket(target_bucket)

# Copy the blob to the destination bucket
source_bucket_cl.copy_blob(source_blob, target_bucket_cl, new_name='test1.json')

print('done')

