#########################################################
# Export a MySQL table into a .csv file using DataFrame
#########################################################

import MySQLdb
from datetime import datetime
import pandas as pd
from google.oauth2 import service_account


# Set variables
csvfile_out = 'C:/Temp/plm_outfile.csv'

# Set GCP Credentials
key_path = 'C:/Dev/bq/PoC Appmaker/poc-appmaker-d4f8ca3f9d79.json'
credentials = service_account.Credentials.from_service_account_file(key_path)

def job():
    conn = MySQLdb.connect(
        host='10.80.129.171',
        user='app_maker_rw',
        password='5xxrAJkEfJEf9gf5',
        database='Opportunity_Reporting'
    )
# Extract data from MySQL and store query results into a DataFrame
    print('Start Extracting from MySQL - ', datetime.now())
    my_query = ('SELECT SalesRep, TYPE, BPID, GrossValue FROM Vw_Opportunity LIMIT 10;')
    #my_query = ('SELECT * FROM Vw_Opportunity;')
    df = pd.read_sql_query(my_query, conn)  #Query results are returned in a DataFrame
    print('Finished Extracting - ', datetime.now())
    print()
# Export DataFrame content into a .csv file
    print('Start Exporting to csv - ', datetime.now())
    #outfile = open(csvfile_out, 'wt')
    df.to_csv(csvfile_out, sep=";", index=False, decimal=".", header=True)  #DataFrame to_csv method to export in csv
    #outfile.close()
    conn.close()
    print('Finished Exporting - ', datetime.now())
    print()

job()
'''
# Instantiates a client
client_ref1 = storage.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials
project_ref1 = client_ref1.project
'''




