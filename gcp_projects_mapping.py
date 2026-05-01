import json
import pprint
import os, sys

from google.cloud import bigquery
from google.oauth2 import service_account

##############################################################################################
# Set GBQ Project-Dataset-Table
project_id = 'bi-team-189611'
dataset_id = 'bigquery_logs'
table_id = 'gcp_projects_metadata'

# Set GCP Credentials
key_path = 'C:/Dev/fd/bi-team-189611-c78f094e47ef.json'
credentials = service_account.Credentials.from_service_account_file(key_path)

# Set GBQ client
client = bigquery.Client(credentials=credentials, project=credentials.project_id)
# client_ref = bigquery.Client(project=project_id)
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

# Set File path with metadata
mapping_file = 'C:/Temp/gcp_projects.json'
##############################################################################################
# Read json file (array of objects) with projects metadata
with open(mapping_file, 'r') as fi:
    content = fi.read()
    # print(content)
fi.close()
# print(content)
# Loading the Json string into a Python dictionary
dict_obj = json.loads(content)
# print(dict_obj[0])
# for i in dict_obj:
#     print(i)
for i in [1,5]:
    print(dict_obj[i]['projectId'])
#
# keys_required = {"projectId", "projectNumber", "name"}
# rows = []
# rows = dict_obj if isinstance(dict_obj, list) else [dict_obj]
# for row in rows:
#     rows.append({k: row.get(k) for k in keys_required})
#     print(row)


# for i in dict_obj:
#     print(i['projectId'], ' - ', i['projectNumber'], ' - ', i['name'])
#
table_schema = [
        bigquery.SchemaField('project_id', 'STRING', mode='NULLABLE', description='project id'),
        bigquery.SchemaField('project_number', 'STRING', mode='NULLABLE', description='project number'),
        bigquery.SchemaField('project_name', 'STRING', mode='NULLABLE', description='project name')
    ]

job_config = bigquery.LoadJobConfig()
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE_DATA
job_config.schema = table_schema
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.ignore_unknown_values = True
job_config.max_bad_records = 0

## Load the file
# job = client.load_table_from_json(rows, table_ref, job_config=job_config)
# job.result()
