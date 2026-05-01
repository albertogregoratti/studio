# doc: https://cloud.google.com/storage/docs/listing-buckets
# doc: https://cloud.google.com/storage/docs/listing-objects

from google.cloud import storage
from google.auth.transport.requests import AuthorizedSession
import google.auth


# key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'   # File containing GCP key
key_path = 'C:/Dev/bq/Usage_Reporting_key/usage-data-reporting-0192446b1bb9.json'

# Instantiates a client
client_ref1 = storage.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials
project_ref1 = client_ref1.project

# List all buckets within a project storage
# buckets = client_ref1.list_buckets()
# print('All buckets within ', project_ref1)
# for b in buckets: print(b)

# List all files (blobs) within a bucket
# files1 = client_ref1.list_blobs('sap-bods')
# print('All files within sap-bods')
# for i in files1: print(i.name)

# Copy a file from one bucket into another
# source_bucket = client_ref1.get_bucket('gbs-dea-dev_anti_piracy')
# source_file = source_bucket.blob('redflag/rf_cov_2014.json')
# destination_bucket = client_ref1.get_bucket('gbs-dea-dev_anti_piracy')
#
# new_file = source_bucket.copy_blob(source_file, destination_bucket, 'test.json')
# print('Finished copying ', source_file, ' from: ', source_bucket, ' to ', destination_bucket)

# Deleting a file
# source_file.delete()
# print('File ', source_file, 'has been deleted' )

# Copy a list of files with a prefix into another bucket and deleting the originals
# files2 = client_ref1.list_blobs(source_bucket, prefix='gbq_contacts')
# print('All files within freshdesk_gbq')
# for i in files2:
#     source_blob =
#     print(i.name)


# def list_soft_deleted_objects('usageent'):
    # Get application default credentials
creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
authed_session = AuthorizedSession(creds)

url = (
        f"https://storage.googleapis.com/storage/v1/b/usageent/o"
        "?softDeleted=true"
    )


response = authed_session.get(url)
response.raise_for_status()

data = response.json()

print("Soft-deleted objects:")
if "items" not in data:print("(None found)")
    # return []

for obj in data["items"]:
    print(f"- {obj['name']} (generation={obj['generation']})")
