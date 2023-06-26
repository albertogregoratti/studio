# doc: https://cloud.google.com/storage/docs/listing-buckets
# doc: https://cloud.google.com/storage/docs/listing-objects

from google.cloud import storage

key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'   # File containing GCP key

# Instantiates a client
client_ref1 = storage.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials
project_ref1 = client_ref1.project

# List all buckets within a project storage
buckets = client_ref1.list_buckets()
print('All buckets within ', project_ref1)
for b in buckets: print(b)

# List all files (blobs) within a bucket
files1 = client_ref1.list_blobs('freshdesk_gbq')
print('All files within freshdesk_gbq')
for i in files1: print(i.name)

# Copy a file from one bucket into another
source_bucket = client_ref1.get_bucket('freshdesk_gbq')
source_file = source_bucket.blob('gbq_contacts2019-12-3_full.json')
destination_bucket = client_ref1.get_bucket('freshdesk_gbq_old')

new_file = source_bucket.copy_blob(source_file, destination_bucket, 'bck_gbq_contacts2019-12-3_full.json')
print('Finished copying ', source_file, ' from: ', source_bucket, ' to ', destination_bucket)

# Deleting a file
source_file.delete()
print('File ', source_file, 'has been deleted' )

# Copy a list of files with a prefix into another bucket and deleting the originals
files2 = client_ref1.list_blobs(source_bucket, prefix='gbq_contacts')
print('All files within freshdesk_gbq')
for i in files2:
    source_blob =
    print(i.name)

