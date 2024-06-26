from google.cloud import bigquery
from google.oauth2 import service_account

project_id = 'usage-data-reporting' # when authenticating using an explicit method, the project id is provided by the json file
dataset_id = 'PROD_IFM_Usage'
key_path = 'C:/Dev/bq/Usage_Reporting_key/usage-data-reporting-3dd6a008b5ae.json'   # File containing GCP key

query = """
SELECT  Cal_Year, Cal_Year_Month, Platform, Sum(No_lic) As Denials
FROM `usage-data-reporting.PROD_IFM_Usage_C5.tbl_mat_monthly` 
WHERE Cal_Date >= '2023-01-01'
GROUP BY 1, 2, 3
ORDER BY 3, 1, 2
"""

# Set GCP Credentials: method 1 (using google.cloud only)
client_ref1 = bigquery.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials

project_ref1 = client_ref1.project    # project id is provided by the json file that contains both credentials and project id

client_ref2 = bigquery.Client.

print('project: ', project_ref1)
print('executing query...')
query_job1 = client_ref1.query(query)
results1 = query_job1.result()
print('results query 1: ')
for row in results1:
    print(row)

# Set GCP Credentials: method 2 (using google.oauth2)
sa_credentials = service_account.Credentials.from_service_account_file(key_path)
client_ref2 = bigquery.Client(credentials=sa_credentials, project=project_id)
dataset_ref2 = client_ref2.dataset(dataset_id)

query_job2 = client_ref2.query(query)
results2 = query_job2.result()
print('results query 2: ')
for row in results2:
    print(row)

