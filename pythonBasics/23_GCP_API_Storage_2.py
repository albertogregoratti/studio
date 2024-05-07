# ****************************************************************************************************
# Working with google storage buckets: loading a file from a local folder into a cloud storage bucket
# ****************************************************************************************************
from google.cloud import storage
from pathlib import Path

# ***********************************************************************************
# Environment variables
# ***********************************************************************************

# Set GCP SA credentials
key_path = 'C:/Dev/fd/bi-team-189611-c78f094e47ef.json'
# key_path = 'C:/Dev/bq/bi_team_key/bi-team-189611-bq_studio.json'

# Create a google cloud storage client
gs_client = storage.Client.from_service_account_json(key_path)

# Set a target
target_bucket = 'freshdesk_gbq'	    # Bucket
target_folder = 'groups/gbq_in/'    # SubFolder(s) within the bucket

# Get the bucket object
bucket_ref = gs_client.bucket(target_bucket)

# Set source and target file path/name
source_folder = Path('C:/Dev/freshdesk/groups/gbq_in')
source_file = 'test.json'
source_path = source_folder / source_file
print('Source path: ', source_path)

target_file = 'test.json'
target_path = target_folder + target_file
print('Target path: ', target_path)


## MAIN##
# Create an object (blob) in the bucket
blob_target = bucket_ref.blob(target_path)

# Upload the file
blob_target.upload_from_filename(filename=source_path)

print('Done')
