from google.cloud import resource_manager

key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'   # File containing GCP key

# Instantiates a client

# Authenticate using service account credentials
# Replace 'path/to/your/service-account-key.json' with the path to your service account key file
client = resource_manager.Client.from_service_account_json(key_path)

# Project ID of the project you want to retrieve quota for
project_id = 'bi-team-189611'

# Retrieve project information
project = client.fetch_project(project_id)

# Extract BigQuery quota information
bigquery_quota = project.get('quota', {}).get('bigquery', {})

# Print the quota information
print("BigQuery Quota Information:")
print("Queries per day:", bigquery_quota.get('queriesPerDay', 'N/A'))
print("Queries per minute:", bigquery_quota.get('queriesPerMinute', 'N/A'))
# Add more fields as needed

