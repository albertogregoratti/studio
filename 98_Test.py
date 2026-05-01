import json
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pprint import pprint

# Load your service account credentials from the JSON file
SERVICE_ACCOUNT_FILE = 'c:/Temp/usage-data-reporting-3a7e2ee0de44.json'
SCOPES = ['https://www.googleapis.com/auth/datastudio.readonly']

# Authenticate using service account credentials
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# credentials = service_account.Credentials(service_account_email='apitest@usage-data-reporting.iam.gserviceaccount.com', scopes=SCOPES)

# Define the API endpoint for assets
API_ENDPOINT = 'https://datastudio.googleapis.com/v1/assets'

# Define the asset ID
asset_id = '2990cc00-a174-443f-9014-69f6f881cd97'

# Authenticate with service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize the Data Studio API client
datastudio = build('datastudio', 'v1', credentials=credentials)
# datastudio = build(credentials=credentials)



# Get asset metadata
# response = datastudio.assets().get(name=f'assets/{asset_id}').execute()
response = datastudio.datastudio().assets().list()

# Print metadata
print("Asset Metadata:")
print(response)


