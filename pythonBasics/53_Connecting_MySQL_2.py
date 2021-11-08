import MySQLdb
import schedule
import time
from datetime import datetime
import pandas as pd
import pandas_gbq as pd_gbq
from google.cloud import bigquery
from google.oauth2 import service_account

# Define variables
#project_id = 'bi-team-189611'
#table_id = 'PLM.tbl_opportunities'
project_id = 'poc-appmaker'
table_id = 'PLM.Pipeline_Allocation_temp'   # Temp table where records are extracted from MySQL
table_id2 = 'PLM.Pipeline_Allocation'       # Final table where records are moved from Temp table
source_table =  "`" + project_id + "." + table_id + "`"
target_table =  "`" + project_id + "." + table_id2 + "`"

# Set GCP Credentials
#key_path = 'C:/Dev/fd/bi-team-189611-c78f094e47ef.json'
key_path = 'C:/Dev/bq/PoC Appmaker/poc-appmaker-d4f8ca3f9d79.json'
credentials = service_account.Credentials.from_service_account_file(key_path)

client_ref = bigquery.Client(credentials=credentials,project=credentials.project_id)

def job():
    conn = MySQLdb.connect(
        host='10.80.129.171',
        user='app_maker_rw',
        password='5xxrAJkEfJEf9gf5',
        database='Opportunity_Reporting'
    )
# Extract data from MySQL
    print('Start Extracting from MySQL - ', datetime.now())
    #my_query = ('SELECT SalesRep, TYPE, BPID, GrossValue FROM Vw_Opportunity LIMIT 10;')
    my_query = ('SELECT * FROM Vw_Pipeline_Allocation;')
    df = pd.read_sql_query(my_query, conn)  #Query results are returned in a DataFrame
    conn.close()
    print('Finished Extracting - ', datetime.now())

# Load into BQ temp table
    print('Start loading into BQ - ', datetime.now())
    pd_gbq.to_gbq(df,table_id, project_id, if_exists='replace', credentials=credentials)
    print('Finished loading - ', datetime.now())

# Move data from temp table to final table
    app_query = """ 
    CREATE OR REPLACE TABLE """ + target_table + """ 
    PARTITION BY PartitionDate 
    CLUSTER BY SalesRepEmail, LevelOneReportingManagerEmail, LevelTwoReportingManagerEmail, SalesRepFullName 
    AS SELECT current_date AS PartitionDate, * FROM """ + source_table + """;
    """
    print('Start moving from temp - ', datetime.now())
    query_job = client_ref.query(app_query)  # Make an API request.
    query_job.result()  # Waits for table load to complete.
    print('Finished moving - ', datetime.now())
    print()

print('Job started - ', datetime.now())
schedule.every(1).minutes.do(job)
#job()

while True:
    schedule.run_pending()
    time.sleep(2)
