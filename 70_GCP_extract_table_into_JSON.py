from google.cloud import bigquery
from google.oauth2 import service_account
import json

# Initialize the BigQuery client
key_path = 'C:/Dev/bq/Looker/Usage/usage-data-reporting-89d67b6f773b.json'
bq_client_ref = bigquery.Client.from_service_account_json(key_path)

# bq_client_ref = bigquery.Client()

# Set your project ID, dataset ID, and table ID
project_id = 'gbs-dea-dev-5bc16c62'
# dataset_id = 'your-dataset-id'
# table_id = 'your-table-id'

# Construct the full table ID
##full_table_id = f"{project_id}.{dataset_id}.{table_id}"

# Create the query
query = """
SELECT *
FROM `gbs-dea-dev-5bc16c62.analytics_anti_piracy_presentation.cov_leads`
 WHERE
  EXTRACT(year FROM date_of_notification) = 2021
  AND take_down_notice_date_1 IS NOT NULL
  AND site_down_date IS NULL
  AND lead_closed_sn IS null
"""

# Run the query
query_job = bq_client_ref.query(query)

# Get the results
results = query_job.result()

# Convert the results to a list of dictionaries
data = [dict(row) for row in results]

# Write the data to a JSON file
output_file = 'C:/Temp/rf_cov_2021.json'
with open(output_file, 'w') as f:
    json.dump(data, f, default=str)

print(f"Data has been extracted and saved to {output_file}")