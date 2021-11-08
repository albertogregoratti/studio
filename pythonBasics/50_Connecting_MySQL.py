import mysql.connector
from google.cloud import bigquery
from google.oauth2 import service_account

# Define variables
# Source: MySQL
'''
pr_db = mysql.connector.connect(
    host='10.80.129.171',
    user='app_maker_rw',
    password='5xxrAJkEfJEf9gf5',
    database='Opportunity_Reporting'
)
'''
pr_db = mysql.connector.connect(
    host='130.211.139.55',
    user='opps_viewer',
    password='opps_viewer',
    database='Opportunity_Reporting'
)
# Target: BQ
project_id = 'bi-team-189611'
dataset_id = 'PLM'
table_id = 'tbl_opportunities'

table_schema = [
        bigquery.SchemaField('SalesRep', 'STRING'),
        bigquery.SchemaField('Type', 'STRING'),
        bigquery.SchemaField('BPID', 'STRING'),
        bigquery.SchemaField('GrossValue', 'NUMERIC')
]

# Set GCP Credentials
key_path = 'C:/Dev/fd/bi-team-189611-c78f094e47ef.json'
credentials = service_account.Credentials.from_service_account_file(key_path)

client_ref = bigquery.Client(credentials=credentials,project=credentials.project_id)
dataset_ref = client_ref.dataset(dataset_id)
#table_ref = dataset_ref.table(table_id)

# Extract data from MySQL
cur = pr_db.cursor()
cur.execute('SELECT SalesRep, Type, BPID, GrossValue FROM Vw_Opportunity LIMIT 10;')
query_result = cur.fetchall()
'''
for x in query_result:
    print(x)
'''
# Load into BQ
job_config = bigquery.LoadJobConfig()
job_config.schema = table_schema
job_config.autodetect = True
job_config.source_format = bigquery.SourceFormat.CSV
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE  # Loading after truncating
#job_config.ignore_unknown_values = True
job_config.max_bad_records = 1

print('Starting loading into BQ')
#load_job = client_ref.load_table_from_dataframe(query_result, dataset_ref.table("table_id"), job_config=job_config, location="EU")    # API request
load_job =client_ref.insert_rows(table_id, job_config=job_config)
#return('Finished loading')
print('Finished loading')