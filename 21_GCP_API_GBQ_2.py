import json
import time
import pprint
from google.cloud import bigquery

# Create a BigQuery client
key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'
bq_client_ref = bigquery.Client.from_service_account_json(key_path)

TableObject = {
   "tableReference": {
     "projectId": "bi-team-189611",
     "datasetId": "TR_aftership_staging",
     "tableId": "test",
   },
   "schema": {
     "fields": [
         {
           "description": "Tag",
           "name": "tag"
         }
       ],
   },
}

tables = bq_client_ref.list_tables()

tables.patch(
    projectId=TableObject['tableReference']['projectId'],\
    datasetId=TableObject['tableReference']['datasetId'],\
    tableId=TableObject['tableReference']['tableId'], \
    body=TableObject).execute()
print ("Table Patched")