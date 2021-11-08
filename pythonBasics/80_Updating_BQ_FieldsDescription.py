#################################################################################################
# This script updates a BQ table with a schema definition provided by a Stored Procedure.
# The script works in 4 steps:
# 1. Gets the TARGET table schema using a Stored Procedure which combines fields names and description
#    from a Google Sheets file.
#    Note: the CALL to this sp can be replaced by its SQL code. In this case this py script needs access to the Sheets file.
# 2. Transforms the schema information into a json object.
# 3. Creates the schema in the right format to be used by the API
# 4. Call the API to update the TARGET table with fields descriptions
#################################################################################################
from google.cloud import bigquery
from google.oauth2 import service_account
import json

# Set target table
project_id = 'usage-data-reporting'
dataset_id = 'PROD_IFM_Usage_C5'
table_id = 'tbl_bp_monthly_nat'
table_address = project_id + '.' + dataset_id + '.' + table_id

client_ref = bigquery.Client(project=project_id)
table_ref = client_ref.get_table(table_address)

# Set GCP Credentials
key_path = 'C:/Dev/bq/Usage_Reporting_key/usage-data-reporting-3dd6a008b5ae.json'
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform",
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']
)

# Set GCP Client
client_ref = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)

### 1. Get table schema from the BQ sp
query_job = client_ref.query("""
CALL `usage-data-reporting.PROD_SVC_Usage_C5.sp_create_table_schema` ('""" + table_id + """');
  """)
#results = query_job.result()

### 2. Transform query results into a json object
records = [dict(row) for row in query_job]

### 3. Create the table schema from the json object
mySchema = []
for col in records:
    mySchema.append(bigquery.SchemaField(col['name'], col['type'], col['mode'], col['description']))

### 4. Update myTable based on mySchema
myTable = bigquery.Table(table_ref, schema=mySchema)
myTable2 = client_ref.update_table(myTable, ["schema"])
print('Table updated')
